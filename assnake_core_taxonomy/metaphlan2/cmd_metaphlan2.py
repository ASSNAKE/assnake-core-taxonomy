import assnake.api.loaders
import assnake.api.sample_set
from tabulate import tabulate
import click, glob
from assnake.cli.cli_utils import sample_set_construction_options, add_options, generic_command_individual_samples, generate_result_list

parameters = [p.split('/')[-1].replace('.json', '') for p in glob.glob('/data11/bio/databases/ASSNAKE/params/mp2/*.json')]

@click.command('metaphlan2', short_help='Taxonomic annoatation based on marker genes')
@add_options(sample_set_construction_options)
@click.option('--params', help='Parameters to use', default='def', type=click.STRING )
@click.pass_obj
def mp2_invocation(config, **kwargs):
    # # check if database initialized
    # if config.get('metaphlan2', None) is None:
    #     click.secho('Metaphlan2 not initialized!', fg='red')
    #     click.echo('run ' + click.style('assnake init metaphlan2', bg='blue') + ' and follow instructions')
    #     exit()
    wc_str = '{fs_prefix}/{df}/reads/{preproc}__metaphlan2_{params}/{sample}_R1.fastq.gz'
    sample_set, sample_set_name = generic_command_individual_samples(config, **kwargs)
    config['requests'] += generate_result_list(sample_set, wc_str, **kwargs)
