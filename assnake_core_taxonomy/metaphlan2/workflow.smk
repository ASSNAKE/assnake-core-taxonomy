
# BOWTIE2DB = config['metaphlan2']['mpa_v296_CHOCOPhlAn_201901']['bt2_index_base']
BOWTIE2DB = config['metaphlan2']['mpa_v30_CHOCOPhlAn_201901']['bt2_index_base']

        
rule metaphlan3:
    input:
        r1 = wc_config['fastq_gz_R1_wc'],
        r2 = wc_config['fastq_gz_R2_wc'] 
    output:
        o     = '{fs_prefix}/{df}/taxa/mp3__{preset}__{version}/{database}/{df_sample}/{preproc}/{df_sample}.rel_ab_w_read_stats.tsv',
        b2out = '{fs_prefix}/{df}/taxa/mp3__{preset}__{version}/{database}/{df_sample}/{preproc}/{df_sample}.bowtie2.bz2',
    threads: 8
    params:
        INDEX = 'mpa_{database}'
    conda: 'env_3.0.0.yaml'
    shell: ('''metaphlan {input.r1},{input.r2} --input_type fastq \
       --add_viruses -t rel_ab_w_read_stats\
       -x {params.INDEX} --bowtie2db {BOWTIE2DB} --nproc {threads}\
       -o {output.o} --bowtie2out {output.b2out};''')
    
rule metaphlan3_relab:
    input:
        b2out = '{fs_prefix}/{df}/taxa/mp3__{preset}__{version}/{database}/{df_sample}/{preproc}/{df_sample}.bowtie2.bz2',
    output:
        o     = '{fs_prefix}/{df}/taxa/mp3__{preset}__{version}/{database}/{df_sample}/{preproc}/{df_sample}.rel_ab.tsv'
    params:
        INDEX = 'mpa_{database}'
    threads: 8
    conda: 'env_3.0.0.yaml'
    shell: ('''metaphlan {input.b2out} --input_type bowtie2out \
       -x {params.INDEX} --bowtie2db {BOWTIE2DB} --add_viruses -t rel_ab --nproc {threads} -o {output.o};''')


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
