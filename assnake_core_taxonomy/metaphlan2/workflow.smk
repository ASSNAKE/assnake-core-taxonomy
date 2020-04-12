
# rule metaphlan2:
#     input:
#         r1 = wc_config['fastq_gz_R1_wc'],
#         r2 = wc_config['fastq_gz_R2_wc']
#     output: 
#         o = wc_config['mp2_out']
#     params:
#         b =  wc_config['mp2_aligment'],
#         # BOWTIE2DB = config['metaphlan2']['{wildcards.database}']['bt2_index_base'], 
#         INDEX = 'mpa_{database}',

#     log:  wc_config['mp2_log']
#     benchmark:  wc_config['mp2_time']
#     threads: 12
#     conda: 'env_2.9.12.yaml'
#     wrapper: "file://" + os.path.join(config['assnake-core-taxonomy'], 'metaphlan2/wrapper.py')
BOWTIE2DB = config['metaphlan2']['mpa_v296_CHOCOPhlAn_201901']['bt2_index_base']
        
rule metaphlan2_from_sam:
    input:
        bt2_sam = '{fs_prefix}/{df}/mapped/bowtie2__mp2_unal__v2.4.1/metaphlan2/mpa_v296_CHOCOPhlAn_201901/{df_sample}/{preproc}/{df_sample}.sam'
    output: 
        o = wc_config['mp2_out']
    params:
        # BOWTIE2DB = config['metaphlan2'][wildcards.database]['bt2_index_base'], 
        INDEX = 'mpa_{database}',

    log:  wc_config['mp2_log']
    benchmark:  wc_config['mp2_time']
    threads: 2
    # conda: 'env_2.9.12.yaml'
    shell: '''set +eu;source activate mpa;\n nreads=`cat {input.bt2_sam} | wc -l`;\n
    metaphlan {input.bt2_sam} -x {params.INDEX} --bowtie2db {BOWTIE2DB} --input_type sam -o {output.o} --nreads $nreads; set -eu;'''
        
rule rarefication_mp2:
    # cat input.txt | awk 'BEGIN {srand()} !/^$/ { if (rand() <= .01) print $0}' > sample.txt
    input:
        bt2_sam = '{fs_prefix}/{df}/mapped/bowtie2__mp2_unal__v2.4.1/metaphlan2/mpa_v296_CHOCOPhlAn_201901/{df_sample}/{preproc}/{df_sample}.sam'
    output: 
        o              = '{fs_prefix}/{df}/taxa/mp2__{params}__{version}/{database}/{df_sample}/{preproc}/{df_sample}_sbsmpl{proprotion}.mp2'
    params:
        # BOWTIE2DB = config['metaphlan2'][wildcards.database]['bt2_index_base'], 
        INDEX = 'mpa_{database}',
        subsampled_sam = '{fs_prefix}/{df}/taxa/mp2__{params}__{version}/{database}/{df_sample}/{preproc}/{df_sample}_sbsmpl{proprotion}.sam',

    log:  '{fs_prefix}/{df}/taxa/mp2__{params}__{version}/{database}/{df_sample}/{preproc}/log_sbsmpl{proprotion}.txt'
    benchmark:  '{fs_prefix}/{df}/taxa/mp2__{params}__{version}/{database}/{df_sample}/{preproc}/time_sbsmpl{proprotion}.txt'
    threads: 2
    # conda: 'env_2.9.12.yaml'
    shell: '''set +eu;source activate mpa;\n
    cat {input.bt2_sam} | awk 'BEGIN {{srand()}} !/^$/ {{ if (rand() <= {wildcards.proprotion}) print $0}}' > {params.subsampled_sam};\n
    nreads=`cat {params.subsampled_sam} | wc -l`;\n
    metaphlan {params.subsampled_sam} -x {params.INDEX} --bowtie2db {BOWTIE2DB} --input_type sam -o {output.o} --nreads $nreads --nproc {threads}; rm {params.subsampled_sam}; set -eu;'''
