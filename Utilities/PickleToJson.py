import pickle
import json
import os
from pathlib import Path


# Conversion tools for ModuleDetection

def set_encoder(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError


p = Path(r'D:\_EvaluationStandards-20220525T082452Z-001\_EvaluationStandards\ModuleDetection')
files = [x for x in p.iterdir() if x.is_file() and not x.name.startswith(".")]
for x in files:
    with Path(x).open("rb") as f:
        pickle_content = pickle.load(f)
        json_content = json.loads(json.dumps(pickle_content, default=set_encoder))
        with open(os.path.splitext(str(x))[0] + '.json', 'w', encoding='utf-8') as outfile:
            json.dump(json_content, outfile, ensure_ascii=False, indent=4)
