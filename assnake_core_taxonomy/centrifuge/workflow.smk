# CENTRIFUGE_INDEX = config["centrifuge"]["index"]
# fna_db_dir = config['fna_db_dir']
#index : '/data5/bio/databases/centrifuge/p+h+v/p+h+v'

rule centr_krona:
    input:classification = 'datasets/{df}/taxa/{preproc}/centr__{params}/{df_sample}/{df_sample}_classification.tsv'
    output: krona = 'datasets/{df}/taxa/{preproc}/centr__{params}/{df_sample}/{df_sample}_krona.tsv'
    params: wd = 'datasets/{df}/taxa/{preproc}/centr__{params}/{df_sample}/'
    # conda: 'env_v1.0.4_beta.yaml'
    run:
        shell('tail -n +2 {input.classification} | cut -f 1,3 > {output.krona}')
        shell('''cd {params.wd} \n /data5/bio/runs-fedorov/tools/krona/bin/ktImportTaxonomy ./{wildcards.df_sample}_krona.tsv -o krona.html''')

CENTRIFUGE_INDEX = '/data11/bio/databases/centrifuge/h+p+v+c/hpvc'
rule centrifuge:
    input: 
        r1 = '{fs_prefix}/{df}/reads/{preproc}/{df_sample}_R1.fastq.gz',
        r2 = '{fs_prefix}/{df}/reads/{preproc}/{df_sample}_R2.fastq.gz',
        # params = "params/centr/{params}.json"
    output:
        report =         '{fs_prefix}/{df}/taxa/centr__{params}__v1.0.4_beta/{database}/{df_sample}/{preproc}/{df_sample}_report.tsv',
        classification = '{fs_prefix}/{df}/taxa/centr__{params}__v1.0.4_beta/{database}/{df_sample}/{preproc}/{df_sample}_classification.tsv',
        krak =           '{fs_prefix}/{df}/taxa/centr__{params}__v1.0.4_beta/{database}/{df_sample}/{preproc}/{df_sample}_krak.tsv', 
    threads:  12
    log:                 '{fs_prefix}/{df}/taxa/centr__{params}__v1.0.4_beta/{database}/{df_sample}/{preproc}/log.txt'
    benchmark:           '{fs_prefix}/{df}/taxa/centr__{params}__v1.0.4_beta/{database}/{df_sample}/{preproc}/benchmark.txt'
    conda: 'env_v1.0.4_beta.yaml'
    shell: ('''centrifuge -k 1 --mm --min-hitlen 22 -f -x {CENTRIFUGE_INDEX} -1 {input.r1} -2 {input.r2} -p {threads} -S {output.classification} --report-file {output.report} -q >{log} 2>&1; \n
          centrifuge-kreport -x {CENTRIFUGE_INDEX} {output.classification} > {output.krak}''')


rule centrifuge_fasta:
    input: 
        fa = os.path.join(fna_db_dir,'{path}/{seq_set_id}.fa')
        # params = "params/centr/{params}.json"
    output:
        report =         os.path.join(fna_db_dir,'{path}/{seq_set_id}_centr__{params}/report.tsv'),
        classification = os.path.join(fna_db_dir,'{path}/{seq_set_id}_centr__{params}/classification.tsv'),
        krak =           os.path.join(fna_db_dir,'{path}/{seq_set_id}_centr__{params}/krak.tsv'), 
    threads:  12
    log:       os.path.join(fna_db_dir,'{path}/{seq_set_id}_centr__{params}/log.txt')
    benchmark: os.path.join(fna_db_dir,'{path}/{seq_set_id}_centr__{params}/benchmark.txt')
    conda: 'env_v1.0.4_beta.yaml'
    shell:
        ('''centrifuge -k 1 --mm --min-hitlen 120 -f -x {CENTRIFUGE_INDEX} -U {input.fa} -p {threads} -S {output.classification} --report-file {output.report} >{log} 2>&1; \n
         centrifuge-kreport -x {CENTRIFUGE_INDEX} {output.classification} > {output.krak}''')