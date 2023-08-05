import logging
import lxml.etree as ET

from followthemoney import model

from ftmcellebrite.util import (
    TimestampSupport, CellebriteXMLSupport
)

log = logging.getLogger(__name__)
OUTGOING = 'Outgoing'


class CellebriteConverter(TimestampSupport, CellebriteXMLSupport):
    def __init__(self, file_path, owner_name, country):
        self.file_path = file_path
        self.country = country
        if not self.check_if_cellebrite_report():
            raise ValueError("Not a Cellebrite Report: %s" % file_path)
        owner = model.make_entity('LegalEntity')
        owner.make_id('owner', owner_name)
        owner.add('name', owner_name)
        owner.add('country', country)
        self.owner = owner
        self.project_id = self.parse_metadata()

    def convert(self):
        yield self.owner
        yield from self.parse_content()

    def check_if_cellebrite_report(self):
        with open(self.file_path, 'r') as fp:
            data = fp.read(1024 * 16)
            namespace = 'xmlns="%s"' % self.NS
            if namespace in data:
                return True
        return False

    def parse_metadata(self):
        file_path = self.file_path
        owner = self.owner
        context = ET.iterparse(str(file_path), events=('end', ),
                               recover=True, tag=self._ns_tag('metadata'))
        project_id = None
        for event, meta in context:
            project = meta.getparent()
            project_id = project_id or project.get('id')
            if project is not None and project.tag != self._ns_tag('project'):
                meta.clear()
                break
            identities = set()
            identities.update(self._item(meta, 'DeviceInfoUniqueID'))
            identities.update(self._item(meta, 'IMEI'))
            identities.update(self._item(meta, 'DeviceInfoUnitIdentifier'))
            if len(identities) and not owner.id:
                owner.make_id(project_id, *sorted(identities))
            owner.add('name', self._item(meta, 'DeviceInfoOwnerName'))
            owner.add('email', self._item(meta, 'DeviceInfoAppleID'))
            owner.add('phone', self._item(meta, 'MSISDN'))
            meta.clear()
        del context

        return project_id

    def parse_content(self):
        # We're using iterparse instead of xpaths to reduce memory usage.
        # iterparse parses the file top to bottom and emits `start` and `end`
        # events when it encounters the start or end of a tag. We want to clear
        # a tag and its children once we are done processing the tag but not
        # before that.
        context = ET.iterparse(str(self.file_path), events=('start', 'end'),
                               recover=True)
        # stores children tags to be cleared after the parent we are interested
        # in is processed
        elements_to_clear = []
        # id of the element being processed currently
        element_being_processed = None
        for event, el in context:
            parent = el.getparent()
            if parent is not None and parent.tag == self._ns_tag('modelType'):
                type_ = el.get('type')
                if type_ in ('Call', 'Chat', 'Note', 'SMS', 'Contact'):
                    if event == 'start':
                        # Set the element being processed
                        element_being_processed = el.get('id')
                        continue
                    else:
                        if type_ == 'Call':
                            yield from self.parse_calls(el)
                        elif type_ == 'Chat':
                            yield from self.parse_messages(el)
                        elif type_ == 'Note':
                            yield from self.parse_notes(el)
                        elif type_ == 'SMS':
                            yield from self.parse_sms(el)
                        elif type_ == 'Contact':
                            yield from self.parse_contacts(el)
                        # We're done with processing an element. Clear it and
                        # its children elements
                        while elements_to_clear:
                            el = elements_to_clear.pop(0)
                            el.clear()
            if event == 'end':
                if element_being_processed is not None:
                    # we are yet to process the parent element; don't clear
                    # the child element yet.
                    elements_to_clear.append(el)
                else:
                    # No element is being processed right now; it's safe to
                    # clear the element
                    el.clear()
        del context

    def parse_parties(self, parties):
        for party in parties:
            names = self._field_values(party, 'Name')
            identifiers = self._field_values(party, 'Identifier')
            yield self._get_party(names, identifiers)

    def parse_calls(self, call):
        entity = model.make_entity('Call')
        entity.make_id(self.project_id, call.get('id'))

        for timestamp in self._field_values(call, 'TimeStamp'):
            entity.add('date', self.parse_timestamp(timestamp))

        for duration in self._field_values(call, 'Duration'):
            entity.add('duration', self.get_seconds(duration))

        call_types = self._field_values(call, 'Type')
        if OUTGOING in call_types:
            entity.add('caller', self.owner)
            entity.add('callerNumber', self.owner.get('phone'))
        else:
            entity.add('receiver', self.owner)
            entity.add('receiverNumber', self.owner.get('phone'))

        for party in self.parse_parties(self._models(call, 'Party')):
            if OUTGOING in call_types:
                entity.add('receiver', party)
                entity.add('receiverNumber', party.get('phone'))
            else:
                entity.add('caller', party)
                entity.add('callerNumber', party.get('phone'))
            yield party

        yield entity

    def parse_messages(self, thread):
        """Message Parsing"""
        ns = self.NSMAP
        thread_id = thread.get('id')
        thread_name = self._field_values(thread, 'Name')
        thread_description = self._field_values(thread, 'Description')
        last_message = None
        for message in self._models(thread, 'InstantMessage'):
            message_id = message.get('id')
            entity = model.make_entity('Message')
            entity.make_id(self.project_id, thread_id, message_id)
            for timestamp in self._field_values(message, 'TimeStamp'):
                entity.add('date', self.parse_timestamp(timestamp))
            entity.add('subject', self._field_values(message, 'Subject'))
            entity.add('threadTopic', thread_name)
            entity.add('threadTopic', thread_description)
            senders = message.xpath('./ns:modelField[@name="From"]/ns:model[@type="Party"]', namespaces=ns)  # noqa
            for sender in self.parse_parties(senders):
                entity.add('sender', sender)
                yield sender

            receivers = message.xpath('./ns:modelField[@name="To"]/ns:model[@type="Party"]', namespaces=ns)  # noqa
            for receiver in self.parse_parties(receivers):
                entity.add('recipients', receiver)
                yield receiver

            status = self._field_values(message, 'Status')
            if 'Read' in status:
                entity.add('recipients', self.owner)
            elif 'Sent' in status:
                entity.add('sender', self.owner)

            entity.add('bodyText', self._field_values(message, 'Body'))

            # Re-use body text as subject if we don't have one
            if not entity.get('subject'):
                entity.add('subject', entity.get('bodyText'))

            # attachments = message.xpath(
            #     './ns:multiModelField[@name="Attachments"]/'
            #     'ns:model[@type="Attachment"]/ns:field[@name="Filename"]'
            #     '/ns:value/text()', namespaces=ns
            # )
            # entity.add('metadata', {'attachments': attachments})

            entity.add('inReplyToMessage', last_message)
            last_message = entity
            yield entity

    def parse_contacts(self, contact):
        name = self._field_values(contact, 'Name')
        numbers = []
        for el in self._models(contact, 'PhoneNumber'):
            numbers.extend(self._field_values(el, 'Value'))
        yield self._get_party(name, numbers)

    def parse_notes(self, note):
        entity = model.make_entity('PlainText')
        entity.make_id(self.project_id, note.get('id'))
        entity.add('title', self._field_values(note, 'Title'))
        entity.add('summary', self._field_values(note, 'Summary'))
        entity.add('bodyText', self._field_values(note, 'Body'))
        for timestamp in self._field_values(note, 'Creation'):
            entity.add('date', self.parse_timestamp(timestamp))
        yield entity

    def parse_sms(self, sms):
        entity = model.make_entity('Message')
        entity.make_id(self.project_id, sms.get('id'))
        entity.add('bodyText', self._field_values(sms, 'Body'))
        for timestamp in self._field_values(sms, 'TimeStamp'):
            entity.add('date', self.parse_timestamp(timestamp))
        for party in self._models(sms, 'Party'):
            name = self._field_values(party, 'Name')
            number = self._field_values(party, 'Identifier')
            party_entity = self._get_party(name, number)
            yield party_entity
            if 'From' in self._field_values(party, 'Role'):
                entity.add('sender', party_entity)
            else:
                entity.add('recipients', party_entity)
        yield entity
