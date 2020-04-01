rule gen_metaphlan2_db:
    input: 
          fna = config['metaphlan2']['mpa_v296_CHOCOPhlAn_201901']['fna']
    output: 
        bt_index = config['metaphlan2']['mpa_v296_CHOCOPhlAn_201901']['bt2_index_base']+'.1.bt2'
    params: bt_index_base = config['metaphlan2']['mpa_v296_CHOCOPhlAn_201901']['bt2_index_base']
    threads: 24
    conda: 'env_2.9.12.yaml'
    shell: ("""bowtie2-build --threads {threads} -f {input.fna} {params}""")

rule metaphlan2:
    input:
        r1 = wc_config['fastq_gz_R1_wc'],
        r2 = wc_config['fastq_gz_R2_wc']
    output: 
        o = wc_config['mp2_out']
    params:
        b =  wc_config['mp2_aligment'],
        MPA_PKL = config['MetaPhlAn2']['mpa_v29'], # '/data5/bio/databases/MetaPhlAn2/mpa_v29_CHOCOPhlAn_201901/mpa_v29_CHOCOPhlAn_201901.pkl'
        BOWTIE2DB = config['MetaPhlAn2']['mpa_v29_bt'], # '/data5/bio/databases/MetaPhlAn2/mpa_v29_CHOCOPhlAn_201901'
        INDEX = 'v29_CHOCOPhlAn_201901',
        task_id = config['task_id'] if 'task_id' in config.keys() else None,

    log:  wc_config['mp2_log']
    benchmark:  wc_config['mp2_time']
    threads: 12
    conda: 'env_2.9.12.yaml'
    wrapper: "file://" + os.path.join(config['assnake-core-taxonomy'], 'metaphlan2/wrapper.py')
        
