import os
from assnake.core.Result import Result
from assnake.core.inputs.Phyloseq import Phyloseq
from assnake_core_taxonomy.kraken2_export_table.result import Kraken2FeatureTable


result = Result.from_location(
    name = 'kraken2-create-phyloseq', 
    description='K mer based taxonomy annotation of reads',
    result_type = '',
    input_type='',
    with_presets=False,
    requires = [Kraken2FeatureTable], 
    produces = [Phyloseq],
    target_wc = '{fs_prefix}/{df}/feature_tables/{sample_set}/{ft_name}/phyloseq.rds',
    location=os.path.dirname(os.path.abspath(__file__)))
