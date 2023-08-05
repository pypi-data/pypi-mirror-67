import click
from followthemoney.cli.cli import cli
from followthemoney.cli.util import write_object

from ftmcellebrite.cellebrite import CellebriteConverter


@cli.command('import-cellebrite', help="Import Cellebrite XML report")
@click.option('-i', '--infile', type=click.Path(exists=True), required=True)
@click.option('-o', '--outfile', type=click.File('w'), default='-')  # noqa
@click.option('--owner', help="Owner's name")
@click.option('--country', help="2 letter country code")
def import_cellebrite(infile, outfile, owner, country):
    try:
        converter = CellebriteConverter(infile, owner, country)
        for entity in converter.convert():
            if entity.id is not None:
                write_object(outfile, entity)
    except BrokenPipeError:
        raise click.Abort()
