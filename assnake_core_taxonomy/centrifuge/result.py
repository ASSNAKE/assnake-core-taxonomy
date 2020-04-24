import click, glob, os
from assnake.core.sample_set import generic_command_individual_samples, generate_result_list
from assnake.cli.cli_utils import sample_set_construction_options, add_options
from assnake.core.result import Result

parameters = [p.split('/')[-1].replace('.json', '') for p in glob.glob('/data11/bio/databases/ASSNAKE/params/mp2/*.json')]
additional_options = [
    click.option(
        '--params', 
        help='Parameters id to use. Available parameter sets: ' + str(parameters), 
        required=False, 
        default = 'def'
        ),
    click.option(
        '--database', 
        help='Database to use', 
        required=False, 
        default = 'h_p_v_c'
        )
]
@click.command('centrifuge', short_help='Taxonomic annoatation based on k-mers')
@add_options(sample_set_construction_options)
@add_options(additional_options)
@click.pass_obj
def centrifuge_invocation(config, **kwargs):
    wc_str = '{fs_prefix}/{df}/taxa/centr__{params}__v1.0.4_beta/{database}/{df_sample}/{preproc}/{df_sample}_report.tsv'
    sample_set, sample_set_name = generic_command_individual_samples(config,  **kwargs)
    config['requests'] += generate_result_list(sample_set, wc_str, **kwargs)
    config['requested_results'] += [{'result': 'centrifuge', 'sample_set': sample_set}]