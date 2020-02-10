
import assnake.api.loaders
import assnake.api.sample_set
from tabulate import tabulate
import click, glob

@click.command('metaphlan2_db', short_help='Initialize database for Metaphlan2')
@click.pass_obj

def mp2_initialization(config, df, preproc, samples_to_add, params):
    # check if database initialized
    click.echo('IN INIT COMMAND')
    