import assnake.api.loaders
import assnake 
from tabulate import tabulate
import click, glob, os
from assnake.utils import download_from_url, update_config, load_config_file
import tarfile


@click.command('metaphlan2-db', short_help='Initialize database for Metaphlan2')
@click.option('--db-location','-d', help='Where to store Metaphlan2 database. It will take approximately 3.5 Gb of disk space. mpa_v296_CHOCOPhlAn_201901 will be downloaded', required=False )
@click.pass_obj

def mp2_init(config, db_location):

    db_url = 'https://bitbucket.org/biobakery/metaphlan2/downloads/mpa_v296_CHOCOPhlAn_201901.tar'
    if db_location is None: # If no path is provided use default
        config = load_config_file()
        db_location = os.path.join(config['assnake_db'], 'metaphlan2')

    os.makedirs(db_location, exist_ok=True)
    download_from_url(db_url, os.path.join(db_location, 'mpa_v296_CHOCOPhlAn_201901.tar'))

    tf = tarfile.open(os.path.join(db_location, 'mpa_v296_CHOCOPhlAn_201901.tar'))
    tf.extractall(os.path.join(db_location, 'mpa_v296_CHOCOPhlAn_201901'))

    update_config({'metaphlan2':{'mpa_v296_CHOCOPhlAn_201901': db_location}})