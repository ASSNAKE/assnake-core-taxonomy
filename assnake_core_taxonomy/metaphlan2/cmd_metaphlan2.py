import click, glob, os
from assnake.core.sample_set import generic_command_individual_samples, generate_result_list
from assnake.core.command_builder import sample_set_construction_options, add_options
from assnake.core.result import Result

parameters = [p.split('/')[-1].replace('.json', '') for p in glob.glob('/data11/bio/databases/ASSNAKE/params/mp2/*.json')]
additional_options = [
    click.option(
        '--params', 
        help='Preset to use. Available presets: ' + str(parameters), 
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

@click.command('metaphlan3', short_help='Taxonomic annoatation based on marker genes with MetaPhlan 3')
@add_options(sample_set_construction_options)
@add_options(additional_options)
@click.pass_obj
def mp3_invocation(config, **kwargs):
    wc_str = '{fs_prefix}/{df}/taxa/mp3__{params}__v3.0.0/{database}/{df_sample}/{preproc}/{df_sample}.tsv'
    sample_set, sample_set_name = generic_command_individual_samples(config,  **kwargs)
    config['requests'] += generate_result_list(sample_set, wc_str, **kwargs)
    config['requested_results'] += [{'result': 'metaphlan3', 'sample_set': sample_set}]



## NEEDS REWRITE AND OPTIMIZATOINS DUE TO THE WAY RAREFICATION WORKS     
@click.command('metaphlan2', short_help='Taxonomic annoatation based on marker genes')
@add_options(sample_set_construction_options)
@add_options(additional_options)
@click.pass_obj
def mp2_invocation(config, **kwargs):
    wc_str = '{fs_prefix}/{df}/taxa/mp2__{params}__v3.0/{database}/{df_sample}/{preproc}/{df_sample}.mp2'
    sample_set, sample_set_name = generic_command_individual_samples(config,  **kwargs)
    config['requests'] += generate_result_list(sample_set, wc_str, **kwargs)
    config['requested_results'] += [{'result': 'metaphlan2', 'sample_set': sample_set}]

parameters = [p.split('/')[-1].replace('.json', '') for p in glob.glob('/data11/bio/databases/ASSNAKE/params/mp2/*.json')]
additional_options = [
    click.option(
        '--params', 
        help='Parameters id to use. Available parameter sets: ' + str(parameters), 
        required=False, 
        default = 'def'
        )
]
@click.command('metaphlan2-rarefication', short_help='Taxonomic annoatation based on marker genes')
@add_options(sample_set_construction_options)
@add_options(additional_options)
@click.pass_obj
def mp2_rare_invocation(config, **kwargs):
    
    sample_set, sample_set_name = generic_command_individual_samples(config,  **kwargs)
    props = ['0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9']
    for p in props:
        wc_str = '{{fs_prefix}}/{{df}}/taxa/mp2__{{params}}__v2.96.1/{{database}}/{{df_sample}}/{{preproc}}/{{df_sample}}_sbsmpl{prop}.mp2'.format(prop = p)
        config['requests'] += generate_result_list(sample_set, wc_str, **kwargs)
    config['requested_results'] += [{'result': 'metaphlan2', 'sample_set': sample_set}]


