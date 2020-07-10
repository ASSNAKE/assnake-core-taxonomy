import click, glob, os
from assnake.core.config import update_instance_config

@click.command('metaphlan2-db', short_help='Initialize database for Metaphlan2')
@click.option('--db-location','-d', help='Where to store Metaphlan2 database. It will take approximately 3.5 Gb of disk space', required=True )
@click.option('--index-version','-i', help='Version of Metaphlan2 database. mpa_v296_CHOCOPhlAn_201901 will be downloaded', required=False, default = 'mpa_v30_CHOCOPhlAn_201901' )

def mp2_init(db_location, index_version):

    update_instance_config({'metaphlan2':{index_version: {
        'bt2_index_base': os.path.join(db_location, index_version),
        }}})

