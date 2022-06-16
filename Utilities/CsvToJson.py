import json
import os
from pathlib import Path
import pandas as pd

# Conversion tools for FunctionalPrediction

p = Path(r'D:\_EvaluationStandards-20220525T082452Z-001\_EvaluationStandards\FunctionalPrediction')
files = [x for x in p.iterdir() if x.is_file() and not x.name.startswith(".")]
for x in files:
    with Path(x).open("rb") as f:
        csv_content = pd.read_csv(f, delimiter=",", header=None).groupby(0).agg({1: lambda x: list(x)})
        json_content = json.loads(csv_content.to_json()[5:-1])
        with open(os.path.splitext(str(x))[0] + '.json', 'w', encoding='utf-8') as outfile:
            json.dump(json_content, outfile, ensure_ascii=False, indent=4)
