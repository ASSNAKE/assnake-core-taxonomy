import click
import glob
import os
from assnake.core.sample_set import generic_command_individual_samples, generate_result_list
from assnake.core.command_builder import sample_set_construction_options, add_options
from assnake.core.result import Result
from assnake.core.config import read_assnake_instance_config

from assnake.utils.general import compute_crc32_of_dumped_dict

from pathlib import Path
import zlib
import json
import shutil

instance_config = read_assnake_instance_config()
presets = []
if instance_config is not None:
    presets = [p.split('/')[-1].replace('.json', '')
                  for p in glob.glob(os.path.join(instance_config['assnake_db'], 'params/metaphlan/*.json'))]
additional_options = [
    click.option(
        '--params', 
        help='Preset to use. Available presets: ' + str([p.split('.')[0] for p in presets]), 
        required=False, 
        default = 'def'
        ),
    click.option(
        '--database',
        help='Metaphlan database to use',
        required=True,
        # default='v296_CHOCOPhlAn_201901',
        default='v30_CHOCOPhlAn_201901',
    )
]

@click.command('metaphlan', short_help='Taxonomic annotation based on marker genes with MetaPhlan 3')
@add_options(sample_set_construction_options)
@add_options(additional_options)
@click.pass_obj
def mp3_invocation(config, **kwargs):
    wc_str = '{fs_prefix}/{df}/taxa/mp3__{params}__v3.0.0/{database}/{df_sample}/{preproc}/{df_sample}.tsv'
    sample_set, sample_set_name = generic_command_individual_samples(config,  **kwargs)
    config['requests'] += generate_result_list(sample_set, wc_str, **kwargs)
    config['requested_results'] += [{'result': 'metaphlan3', 'sample_set': sample_set, 'preprocessing': False}]


this_dir = os.path.dirname(os.path.abspath(__file__))



result = Result.from_location(name='metaphlan', location=this_dir, input_type='illumina_sample',
                              additional_inputs=None, invocation_command=mp3_invocation)
