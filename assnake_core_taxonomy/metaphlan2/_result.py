import click, os
from assnake.core.Result import Result

result = Result.from_location(name='metaphlan',
                              description='Taxonomic annotation based on marker genes with MetaPhlan 3',
                              result_type='taxonomy',
                              location=os.path.dirname(os.path.abspath(__file__)),
                              input_type='illumina_sample',
                              additional_inputs=[
                                  click.option('--preset', help='Preset to use. Available presets: ', default='def'),
                                  click.option('--version', help='Version of metaphlan to use', default='v3.0.0'),
                                  click.option('--database', help='Metaphlan database to use', required=True, default='v30_CHOCOPhlAn_201901')
                              ])
