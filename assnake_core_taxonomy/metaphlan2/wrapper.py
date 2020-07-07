__author__ = "Dmitry Fedorov"
__copyright__ = "Copyright 2020, Dmitry Fedorov"
__email__ = "fedorov.de@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell

BOWTIE2DB = snakemake.config['metaphlan2'][snakemake.params.INDEX]['bt2_index_base']

shell('''metaphlan {input.r1},{input.r2} --input_type fastq \
       --add_viruses -t rel_ab_w_read_stats\
       -x {params.INDEX} --bowtie2db {BOWTIE2DB} --nproc {threads}\
       -o {output.o} --bowtie2out {output.b2out};''' )
