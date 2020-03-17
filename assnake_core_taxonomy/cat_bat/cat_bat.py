cat_bat_db = config['CAT_BAT_DB']
cat_bat_taxa = config['CAT_BAT_TAXA']



rule cat_bat_contigs_new:
    input:
        fa             = '{fs_prefix}/{df}/assembly/{sample_set}/{assembler}__{assembler_version}__{params}/final_contigs__{mod}.fa'
    output:
        classification = '{fs_prefix}/{df}/assembly/{sample_set}/{assembler}__{assembler_version}__{params}/final_contigs__{mod}_CAT/out.CAT.contig2classification.txt'
    params:
        wd             = '{fs_prefix}/{df}/assembly/{sample_set}/{assembler}__{assembler_version}__{params}/final_contigs__{mod}_CAT/',
        prefix         = '{fs_prefix}/{df}/assembly/{sample_set}/{assembler}__{assembler_version}__{params}/final_contigs__{mod}_CAT/out.CAT',
    threads: 16
    conda: 'cat_bat_env.yaml'
    shell: ('''mkdir -p {params.wd}; \n
            CAT contigs -c {input.fa} -d {cat_bat_db} -t {cat_bat_taxa} --index_chunks 1 --I_know_what_Im_doing --top 25 --out_prefix {params.prefix} -n {threads};''')

rule add_names2:
    input:
        classification = '{fs_prefix}/{df}/assembly/{sample_set}/{assembler}__{assembler_version}__{params}/final_contigs__{mod}_CAT/out.CAT.contig2classification.txt'
    output:
        names          = '{fs_prefix}/{df}/assembly/{sample_set}/{assembler}__{assembler_version}__{params}/final_contigs__{mod}_CAT/contig2classification_names_official.txt'
    conda: 'cat_bat_env.yaml'
    shell: ('''CAT add_names -i {input.classification} -o {output.names} -t {cat_bat_taxa} --only_official''')
