__author__ = "Dmitry Fedorov"
__copyright__ = "Copyright 2019, Dmitry Fedorov"
__email__ = "fedorov.de@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell

BOWTIE2DB = snakemake.config['metaphlan2'][snakemake.params.INDEX]['bt2_index_base']

shell('''metaphlan2.py --bowtie2db {BOWTIE2DB} -x {snakemake.params.INDEX}  \
         {snakemake.input.r1},{snakemake.input.r2} --input_type fastq --bowtie2out {snakemake.params.b} \
         --nproc {snakemake.threads} > {snakemake.output.o}''' )
