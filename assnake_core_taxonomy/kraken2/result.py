import os
from assnake.core.Result import Result
from assnake.core.inputs.IlluminaSampleInput import IlluminaSampleInput

result = Result.from_location(
    name = 'kraken2', 
    description='K mer based taxonomy annotation of reads',
    result_type = 'Report',
    input_type='illumina_sample',
    with_presets=False,
    requires = [IlluminaSampleInput],
    target_wc = '{fs_prefix}/{df}/taxa/kraken2/k2_standard_08gb_20240112/{preproc}/{df_sample}_report.txt',
    location=os.path.dirname(os.path.abspath(__file__)))
