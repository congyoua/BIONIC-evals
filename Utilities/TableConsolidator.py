import pandas as pd
from pathlib import Path
from functools import reduce

p = Path(r"C:\Users\Youan\Desktop\CTables")
if __name__ == '__main__':
    CO, MO, FP = pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

    files = [x for x in sorted(p.iterdir()) if x.is_file() and not x.name.startswith(".")]

    for x in files:

        if "Coannotation_" in x.name:
            table = pd.read_csv(x, delimiter="\t", header=[0, 1, 2], index_col=[0])
            CO = table if CO.empty else CO.combine_first(table)
        elif "FunctionalPrediction_" in x.name:
            table = pd.read_csv(x, delimiter="\t", header=[0, 1, 2], index_col=[0])
            MO = table if MO.empty else MO.combine_first(table)
        elif "ModuleDetection_" in x.name:
            table = pd.read_csv(x, delimiter="\t", header=[0, 1, 2], index_col=[0])
            FP = table if FP.empty else FP.combine_first(table)

    CO = CO.sort_index(level=2, axis=1)
    MO = MO.sort_index(level=2, axis=1)
    FP = FP.sort_index(level=2, axis=1)
    Combined = pd.concat([CO,MO,FP], axis=1)
    print(Combined)
    Combined.to_csv(p / Path(f"Combined_results.tsv"), sep="\t")
