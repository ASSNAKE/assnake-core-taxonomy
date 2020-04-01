import assnake.api.loaders
import assnake 
from tabulate import tabulate
import click, glob, os
from assnake.utils import download_from_url, update_config, load_config_file
import tarfile
import bz2

@click.command('metaphlan2-db', short_help='Initialize database for Metaphlan2')
@click.option('--db-location','-d', help='Where to store Metaphlan2 database. It will take approximately 3.5 Gb of disk space. mpa_v296_CHOCOPhlAn_201901 will be downloaded', required=False )
@click.pass_obj

def mp2_init(config, db_location):

    db_url = 'https://bitbucket.org/biobakery/metaphlan2/downloads/mpa_v296_CHOCOPhlAn_201901.tar'
    if db_location is None: # If no path is provided use default
        config = load_config_file()
        db_location = os.path.join(config['assnake_db'], 'metaphlan2')

    click.echo('Downloading mpa_v296_CHOCOPhlAn_201901 database to: ' + db_location)
    os.makedirs(db_location, exist_ok=True)
    download_from_url(db_url, os.path.join(db_location, 'mpa_v296_CHOCOPhlAn_201901.tar'))

    click.echo('Extracting Metaphlan2 database from archive')
    tf = tarfile.open(os.path.join(db_location, 'mpa_v296_CHOCOPhlAn_201901.tar'))
    tf.extractall(os.path.join(db_location, 'mpa_v296_CHOCOPhlAn_201901'))

    # uncompress sequences
    bz2_file = os.path.join(db_location, 'mpa_v296_CHOCOPhlAn_201901', "mpa_v296_CHOCOPhlAn_201901.fna.bz2")
    fna_file = os.path.join(db_location, 'mpa_v296_CHOCOPhlAn_201901', "mpa_v296_CHOCOPhlAn_201901.fna")

    if not os.path.isfile(fna_file):
        print('\n\nDecompressing {} into {}\n'.format(bz2_file, fna_file))

        with open(fna_file, 'wb') as fna_h, bz2.BZ2File(bz2_file, 'rb') as bz2_h:
            for data in iter(lambda: bz2_h.read(100 * 1024), b''):
                fna_h.write(data)

    update_config({'metaphlan2':{'mpa_v296_CHOCOPhlAn_201901': db_location}})