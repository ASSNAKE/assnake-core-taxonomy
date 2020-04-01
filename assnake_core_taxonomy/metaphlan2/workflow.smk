# rule gen_metaphlan2_db:
#     input: "/mpa_v295_CHOCOPhlAn_201901.tar"
#     output: 
#         bt_index = "mpa_v295_CHOCOPhlAn_201901.1.bt2",
#         pkl = "mpa_v295_CHOCOPhlAn_201901.pkl",
#         fna_bz2 = "mpa_v295_CHOCOPhlAn_201901.fna.bz2"
#     threads: 8
#     conda: 'env_2.9.12.yaml'
#     shell: ("""""")

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
        
