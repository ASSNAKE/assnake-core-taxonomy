KRAKEN2_DATABASE = '/mnt/disk1/DATABASES/kraken2/k2_standard_08gb_20240112'

def collect_kraken2_reports(wildcards):

    reports = []
    report_wc = '{fs_prefix}/{df}/taxa/kraken2/k2_standard_08gb_20240112/{preproc}/{df_sample}_report.txt'

    fastqc_list = []
    sample_set_loc = '{fs_prefix}/{df}/sample_collections/{sample_set}/sample_set.tsv'.format(
        df = wildcards.df, 
        fs_prefix = wildcards.fs_prefix, 
        sample_set = wildcards.sample_set
    )
    sample_set = pd.read_csv(sample_set_loc, sep = '\t')
    for s in sample_set.to_dict(orient='records'):
        reports.append(
            report_wc.format(
                df = s['df'], 
                fs_prefix = s['fs_prefix'], 
                df_sample = s['df_sample'], 
                preproc = s['preproc']
            )
        )
    return reports

rule kraken2_export_table:
    input:
        sample_set = '{fs_prefix}/{df}/sample_collections/{sample_set}/sample_set.tsv',
        reports = collect_kraken2_reports
    output:
        otu    = '{fs_prefix}/{df}/taxa/kraken2-collections/k2_standard_08gb_20240112/{sample_set}/otu.tsv',
        taxa    = '{fs_prefix}/{df}/taxa/kraken2-collections/k2_standard_08gb_20240112/{sample_set}/taxa.tsv',
    params:
        reports_comma_separated = lambda w, input: ",".join(input.reports),
    threads: 1
    shell:
        """
        kraken2_2otu --files {params.reports_comma_separated}  --otu_output {output.otu} --tax_output {output.taxa}
        """