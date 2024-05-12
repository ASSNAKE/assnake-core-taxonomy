KRAKEN2_DATABASE = '/mnt/disk1/DATABASES/kraken2/k2_standard_08gb_20240112'

rule kraken2_create_phyloseq:
    input:
        ft_meta = '{fs_prefix}/{df}/feature_tables/{sample_set}/{ft_name}/metadata.yaml',
        otu    = '{fs_prefix}/{df}/taxa/kraken2-collections/k2_standard_08gb_20240112/{sample_set}/otu.tsv',
        taxa    = '{fs_prefix}/{df}/taxa/kraken2-collections/k2_standard_08gb_20240112/{sample_set}/taxa.tsv',
    output:
        ps     = '{fs_prefix}/{df}/feature_tables/{sample_set}/{ft_name}/phyloseq.rds',
    threads: 10
    shell:
        """
        Rscript -e " \
        library(phyloseq); \
        library(Biostrings); \
        counts <- read.table('{input.otu}', header = T); \
        rownames(counts) <- counts[, 'Sample']; \
        counts <- counts[, -which(names(counts) == 'Sample')]; \
        taxa <- read.table('{input.taxa}', header = T, sep='\\t'); \
        taxa[, 'TaxID'] <- paste0('X', taxa[, 'TaxID']); \
        rownames(taxa) <- taxa[, 'TaxID']; \
        taxa <- taxa[, -which(names(taxa) == 'TaxID')]; \
        ps <- phyloseq(otu_table(counts, taxa_are_rows = FALSE), tax_table(as.matrix(taxa))); \
        saveRDS(ps, '{output.ps}'); \
        "
        """