import pandas as pd

def read_krak_node(df, node_name):
    reads = df.loc[df[5] == node_name][1]
    if len(reads) == 0:
        reads = 0
    else:
        reads = int(reads)
    return reads


def general_taxa_one(s):
    loc_wc = pipeline + 'datasets/{df}/taxa/{preproc}/centr__{params}/{sample}/{sample}_krak.tsv'
    
    loc = loc_wc.format(df = s['df'], 
                            preproc=s['preproc'], 
                            sample = s['fs_name'],
                            params = 'def')
    
    if os.path.isfile(loc):
        try:
            centr_krak = pd.read_csv(loc, sep='\t', header=None)
            uncl = read_krak_node(centr_krak, 'unclassified')
            vir = read_krak_node(centr_krak, '  Viruses')
            homo = read_krak_node(centr_krak,
                                      '                                                              Homo sapiens')
            bacteria = read_krak_node(centr_krak, '    Bacteria')
            archaea = read_krak_node(centr_krak, '    Archaea')
            other = read_krak_node(centr_krak, 'root') - vir - homo - bacteria - archaea

            total = uncl + vir + bacteria + archaea + homo + other
            composition = {'sample': s['fs_name'],
                               'uncl': uncl,
                               'vir': vir,
                               'bacteria': bacteria,
                               'archaea': archaea,
                               'homo': homo,
                               'other': other,
                               'total': total}
            return composition
        except:
            print('error' + loc)
            return None
    else:
        return None

def get_general_taxa_comp_krak_style(samples):
    loc_wc = '{fs_prefix}/{df}/taxa/{preproc}/centr__{params}/{sample}/{sample}_krak.tsv'
    comp = []
    
    for s in samples:
        loc = loc_wc.format(df = s['df'], 
                            fs_prefix = s['fs_prefix'],
                            preproc=s['preproc'], 
                            sample = s['fs_name'],
                            params = 'def1')
        if os.path.isfile(loc):
            try:
                centr_krak = pd.read_csv(loc, sep='\t', header=None)
                uncl = read_krak_node(centr_krak, 'unclassified')
                vir = read_krak_node(centr_krak, '  Viruses')
                homo = read_krak_node(centr_krak,
                                      '                                                              Homo sapiens')
                bacteria = read_krak_node(centr_krak, '    Bacteria')
                archaea = read_krak_node(centr_krak, '    Archaea')
                other = read_krak_node(centr_krak, 'root') - vir - homo - bacteria - archaea

                total = uncl + vir + bacteria + archaea + homo + other
                composition = {'sample': s['fs_name'],
                               'uncl': uncl,
                               'vir': vir,
                               'bacteria': bacteria,
                               'archaea': archaea,
                               'homo': homo,
                               'other': other,
                               'total': total}
                comp.append(composition)
            except:
                print('error' + loc)
        else:
            print('NO FILE: ', loc)
    return comp