import assnake.api.loaders 
import assnake
from tabulate import tabulate
import click, glob

parameters = [p.split('/')[-1].replace('.json', '') for p in glob.glob('/data11/bio/databases/ASSNAKE/params/mp2/*.json')]

@click.command('metaphlan2', short_help='Taxonomic annoatation based on marker genes')

@click.option('--df','-d', help='Name of the dataset', required=True )
@click.option('--preproc','-p', help='Preprocessing to use' )
@click.option('--samples-to-add','-s', 
                help='Samples from dataset to process', 
                default='', 
                metavar='<samples_to_add>', 
                type=click.STRING )
@click.option('--params', help='Parameters id to use. Available parameter sets: ' + str(parameters), required=False, default = 'def')


@click.pass_obj

def mp2_invocation(config, df, preproc, samples_to_add, params):
    # # check if database initialized
    # if config.get('metaphlan2', None) is None:
    #     click.secho('Metaphlan2 not initialized!', fg='red')
    #     click.echo('run ' + click.style('assnake init metaphlan2', bg='blue') + ' and follow instructions')
    #     exit()

    samples_to_add = [] if samples_to_add == '' else [c.strip() for c in samples_to_add.split(',')]
    df = assnake.api.loaders.load_df_from_db(df)
    ss = assnake.SampleSet.SampleSet(df['fs_prefix'], df['df'], preproc, samples_to_add=samples_to_add)

    click.echo(tabulate(ss.samples_pd[['fs_name', 'reads', 'preproc']].sort_values('reads'), 
        headers='keys', tablefmt='fancy_grid'))
    res_list = ss.get_locs_for_result('mp2')
    if config.get('requests', None) is None:
        config['requests'] = res_list
    else:
        config['requests'] += res_list