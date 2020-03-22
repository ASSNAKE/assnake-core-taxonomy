from scipy.spatial import distance
from sklearn.manifold import MDS
from sklearn.manifold import LocallyLinearEmbedding
import pandas as pd
# from skbio.stats.composition import *
from scipy.spatial.distance import pdist, squareform

import ecopy


def diversity(otu_table):
    methods = ['shannon' , 'gini-simpson', 'simpson' , 'dominance',  'spRich', 'even']
    index = list(otu_table.index)
    
    methods_res = {}
    for m in methods:
        div = ecopy.diversity(otu_table, method=m, breakNA=True)
#         methods_res.append(list(div))
        methods_res.update({m:list(div)})
    
    div_pd = pd.DataFrame(methods_res, columns=methods)
    div_pd.index = otu_table.index

    return div_pd
