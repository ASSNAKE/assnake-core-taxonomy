import pandas as pd
import os

def load_metaphlan2(self, samples = None, preprocessing = 'raw'):
    if samples is None:
        samples = self.sample_sets[preprocessing].to_dict(orient='records')
    else:
        if not isinstance(samples, list):
            samples = samples.to_dict(orient='records')


    mp2_wc = '{fs_prefix}/{df}/taxa/mp2__def__v2.96.1/v296_CHOCOPhlAn_201901/{df_sample}/{preproc}/{df_sample}.mp2'
    mp2_all = []
    for s in samples:
        mp2_loc = mp2_wc.format(
            fs_prefix = s['fs_prefix'].rstrip('\/'),
            df = s['df'],
            preproc = s['preproc'],
            df_sample = s['df_sample']
        )
        if os.path.isfile(mp2_loc):
            try:
                mp2 = pd.read_csv(mp2_loc, sep='\t', header = 3, index_col = False)
                mp2['df_sample']=s['df_sample']
                mp2_all.append(mp2)
            except:
                print('ERROR LOADING:', mp2_loc)

    mp2_all = pd.concat(mp2_all)
    mp2_all = mp2_all.pivot(index='df_sample', columns = '#clade_name', values = 'relative_abundance')
    return mp2_all

def filter_metaphlan2(mp2, level = 'g__', zeroes_in_samples = 0.5):
    levels = ['k__', 'p__', 'c__', 'o__', 'f__', 'g__', 's__', 't__']

    ind = levels.index(level)
    columns = mp2.columns
    cols = []
    for col in columns:
        if not (levels[ind] in col and levels[ind+1] not in col):
            cols.append(col)
            

    mp2_all_order = mp2.drop(cols, axis=1)
    mp2_all_order = mp2_all_order.fillna(0)
    mp2_all_order = mp2_all_order.div(mp2_all_order.sum(axis=1), axis=0)

    mp2_all_order_sub = mp2_all_order.loc[:, (mp2_all_order == 0).mean(0) < zeroes_in_samples ]

    return mp2_all_order_sub