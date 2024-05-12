import os
from assnake.core.Result import Result
from assnake.core.inputs.FeatureTableInput import FeatureTableInput
from assnake.core.inputs.IlluminaSampleInput import IlluminaSampleInput
from assnake.core.inputs.SampleCollectionInput import SampleCollectionInput

class Kraken2FeatureTable(FeatureTableInput):
    "Feature Table produced by DADA2 algorithm"
    metadata_filename = 'metadata.yaml'
    # source_wc_string = '{fs_prefix}/{df}/taxa/kraken2-collections/k2_standard_08gb_20240112/{sample_set}_report.txt'


result = Result.from_location(
    name = 'kraken2-export-table', 
    description='K mer based taxonomy annotation of reads',
    result_type = 'Report',
    input_type='illumina_sample',
    with_presets=False,
    requires = [SampleCollectionInput],
    produces = [Kraken2FeatureTable],
    target_wc = '{fs_prefix}/{df}/taxa/kraken2-collections/k2_standard_08gb_20240112/{sample_set}.tsv',
    location=os.path.dirname(os.path.abspath(__file__)))
