
rule metaphlan2:
    input:
        r1 = wc_config['fastq_gz_R1_wc'],
        r2 = wc_config['fastq_gz_R2_wc']
    output: 
        o = wc_config['mp2_out']
    params:
        b =  wc_config['mp2_aligment'],
        # BOWTIE2DB = config['metaphlan2']['{wildcards.database}']['bt2_index_base'], 
        INDEX = 'mpa_{database}',

    log:  wc_config['mp2_log']
    benchmark:  wc_config['mp2_time']
    threads: 12
    conda: 'env_2.9.12.yaml'
    wrapper: "file://" + os.path.join(config['assnake-core-taxonomy'], 'metaphlan2/wrapper.py')
        
