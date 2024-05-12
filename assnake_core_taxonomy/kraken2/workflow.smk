KRAKEN2_DATABASE = '/mnt/disk1/DATABASES/kraken2/k2_standard_08gb_20240112'

rule kraken2:
    input:
        r1 = "{fs_prefix}/{df}/reads/{preproc}/{sample}_R1.fastq.gz",
        r2 = "{fs_prefix}/{df}/reads/{preproc}/{sample}_R2.fastq.gz"
    output:
        out    = '{fs_prefix}/{df}/taxa/kraken2/k2_standard_08gb_20240112/{preproc}/{sample}.txt',
        report = '{fs_prefix}/{df}/taxa/kraken2/k2_standard_08gb_20240112/{preproc}/{sample}_report.txt'
    threads: 10
    conda: 'kraken2'
    shell:
        """
        kraken2 --db {KRAKEN2_DATABASE} --paired --use-names --gzip-compressed --threads {threads} --report {output.report} --output {output.out}  {input.r1}  {input.r2};
        """