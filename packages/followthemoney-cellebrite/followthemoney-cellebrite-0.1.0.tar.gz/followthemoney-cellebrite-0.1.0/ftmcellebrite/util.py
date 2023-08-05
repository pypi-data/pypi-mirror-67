import logging
from datetime import datetime, date

from banal import ensure_list
from normality import stringify
from followthemoney import model

log = logging.getLogger(__name__)


class TimestampSupport(object):
    """Provides helpers for date and time parsing."""
    TIMESTAMP_FORMATS = (
        '%Y-%m-%dT%H:%M:%S',
        '%Y-%m-%d %H:%M:%S',
        '%Y:%m:%d %H:%M:%S',
        '%Y-%m-%dT%H:%M:%SZ',
        '%Y-%m-%dT%H:%M:%S%z',
        '%Y:%m:%d %H:%M:%SZ',  # exif
        '%Z %Y-%m-%d %H:%M:%S',
        '%Y-%m-%d',
        '%Y%m%d',
    )

    def parse_timestamp(self, raw, fmt=None):
        if isinstance(raw, (datetime, date)):
            return raw
        text = stringify(raw)
        if text is None:
            return
        formats = ensure_list(fmt) or self.TIMESTAMP_FORMATS
        for fmt in formats:
            try:
                if '.' in text and '.' not in fmt:
                    text, _ = text.split('.', 1)
                return datetime.strptime(text, fmt)
            except Exception:
                pass
        log.warning("Could not parse timestamp: %r", raw)
        return raw

    def get_seconds(self, time_str):
        """Get Seconds from time"""
        h, m, s = time_str.split(':')
        return float(h) * 3600 + float(m) * 60 + float(s)


class CellebriteXMLSupport(object):
    NS = "http://pa.cellebrite.com/report/2.0"
    NSMAP = {"ns": NS}

    def _item(self, meta, name):
        query = './ns:item[@name="%s"]/text()' % name
        return meta.xpath(query, namespaces=self.NSMAP)

    def _ns_tag(self, tag):
        return '{{{0}}}{1}'.format(self.NS, tag)

    def _field_values(self, el, name):
        query = './ns:field[@name="%s"]/ns:value/text()' % name
        values = []
        for value in el.xpath(query, namespaces=self.NSMAP):
            value = stringify(value)
            if value is not None:
                values.append(value)
        return list(sorted(values))

    def _models(self, el, name):
        query = ".//ns:model[@type='%s']" % name
        yield from el.xpath(query, namespaces=self.NSMAP)

    def _get_party(self, names, identifiers, proof=None):
        party = model.make_entity('LegalEntity')
        if not names:
            names = identifiers
        party.add('name', names)
        party.add('country', self.country)
        party.add('proof', proof)

        for identifier in sorted(identifiers, key=len, reverse=True):
            prop = 'email' if '@' in identifier else 'phone'
            party.add(prop, identifier)
            if not party.id and party.get(prop):
                party.make_id(self.project_id, identifier)

        if not party.id and names:
            party.make_id(self.project_id, *ensure_list(names))

        return party
