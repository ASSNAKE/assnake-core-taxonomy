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
        )
]
@click.command('metaphlan2', short_help='Taxonomic annoatation based on marker genes')
@add_options(sample_set_construction_options)
@add_options(additional_options)
@click.pass_obj
def mp2_invocation(config, **kwargs):
    # # check if database initialized
    # if config.get('metaphlan2', None) is None:
    #     click.secho('Metaphlan2 not initialized!', fg='red')
    #     click.echo('run ' + click.style('assnake init metaphlan2', bg='blue') + ' and follow instructions')
    #     exit()

    wc_str = '{fs_prefix}/{df}/taxa/mp2__def__v2.96.1/v296_CHOCOPhlAn_201901/{df_sample}/{preproc}/{df_sample}.mp2'
    sample_set, sample_set_name = generic_command_individual_samples(config,  **kwargs)
    config['requests'] += generate_result_list(sample_set, wc_str, **kwargs)
    config['requested_results'] += [{'result': 'metaphlan2', 'sample_set': sample_set}]
