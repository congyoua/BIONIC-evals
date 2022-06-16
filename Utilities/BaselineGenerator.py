import json
import operator
from functools import reduce

import numpy as np
import networkx as nx
from pathlib import Path

# Baseline Genes list Generator
if __name__ == '__main__':
    lst = []

    # co
    p = Path(r'D:\BIONIC\Standards\GeneCoannotation')
    files = [x for x in sorted(p.iterdir()) if x.is_file() and not x.name.startswith(".")]
    for x in files:
        if ".csv" in x.name:
            standard = list(nx.read_weighted_edgelist(x, delimiter=",").nodes())
            lst.append(standard)

    # Mo
    p = Path(r'D:\BIONIC\Standards\ModuleDetection')
    files = [x for x in sorted(p.iterdir()) if x.is_file() and not x.name.startswith(".")]
    for x in files:
        if ".json" in x.name:
            with Path(x).open("r") as f:
                standard = json.loads(f.read())
                standard = reduce(operator.iconcat, standard.values(), [])
                lst.append(standard)

    # FP
    p = Path(r'D:\BIONIC\Standards\FunctionalPrediction')
    files = [x for x in sorted(p.iterdir()) if x.is_file() and not x.name.startswith(".")]
    for x in files:
        if ".json" in x.name:
            with Path(x).open("r") as f:
                standard = json.loads(f.read())
                standard = list(standard.keys())
                lst.append(standard)

    lst = reduce(np.union1d, lst)
    with open(r'D:\BIONIC\baseline_genes_list.txt', 'w') as f:
        f.write('\n'.join(str(item).strip() for item in lst))
