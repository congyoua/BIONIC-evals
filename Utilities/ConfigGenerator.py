from pathlib import Path
import pandas as pd

root = '/scratch/congyoua/BIONIC/'
p = Path('/scratch/congyoua/BIONIC/Configs')

Coannotation = pd.read_csv(Path(root + 'standards(Coannotation).csv').open("rb"), header=None)
ModuleDetection = pd.read_csv(Path(root + 'standards(ModuleDetection).csv').open("rb"), header=None)
FunctionalPrediction = pd.read_csv(Path(root + 'standards(FunctionalPrediction).csv').open("rb"), header=None)

Features = pd.read_csv(Path(root + 'datasets(Features).csv').open("rb"), header=None)
Networks = pd.read_csv(Path(root + 'datasets(Networks).csv').open("rb"), header=None)

Feature_Config = """{
    "networks": [],
    "features": [
        {
            "name": "XX",
            "path": "YY",
            "delimiter": "ZZ"
        }
    ],
    "standards": [
        {
            AA
        }
    ],
    "consolidation": "baseline"
}"""
Network_Config = """{
    "networks": [
        {
            "name": "XX",
            "path": "YY",
            "delimiter": " "
        }
    ],
    "features": [],
    "standards": [
        {
            AA
        }
    ],
    "consolidation": "baseline"
}"""


# Generate config for features when mode is true, vice versa
def generate_config(path, name, mode):
    # Coannotation
    for i in range(len(Coannotation)):
        text = Feature_Config if mode else Network_Config
        text = text.replace("XX", name)
        text = text.replace("YY", root + "Datasets/FeatureMatrix/tabular_datasets/" + path) if mode else text.replace("YY", root + "Datasets/" + path)
        new_path = root + "Standards/" + Coannotation.iloc[:, 0][i]
        if mode:
            if ".csv" in path:
                text = text.replace("ZZ", ",")
            elif ".tsv" in path:
                text = text.replace("ZZ", "\\t")

        str = f""""name": "{Coannotation.iloc[:, 1][i]}",
            "task": "coannotation",
            "path": "{new_path}",
            "delimiter": ","
        """
        text = text.replace("AA", str)
        with (Path(p) / Path(f"Coannotation_{name}_{Coannotation.iloc[:, 1][i]}.json")).open("w") as f:
            f.write(text)
            f.close()
    # ModuleDetection
    for i in range(len(ModuleDetection)):
        text = Feature_Config if mode else Network_Config
        text = text.replace("XX", name)
        text = text.replace("YY", root + "Datasets/FeatureMatrix/tabular_datasets/" + path) if mode else text.replace("YY", root + "Datasets/" + path)
        new_path = root + "Standards/" + ModuleDetection.iloc[:, 0][i]
        if mode:
            if ".csv" in path:
                text = text.replace("ZZ", ",")
            elif ".tsv" in path:
                text = text.replace("ZZ", "\\t")

        str = f""""name": "{ModuleDetection.iloc[:, 1][i]}",
            "task": "module_detection",
            "path": "{new_path}",
            "samples": 10,
            "methods": [
                "average",
                "single",
                "complete"
            ],
            "metrics": [
                "euclidean",
                "cosine"
            ],
            "thresholds": 500
        """
        text = text.replace("AA", str)
        with (Path(p) / Path(f"ModuleDetection_{name}_{ModuleDetection.iloc[:, 1][i]}.json")).open("w") as f:
            f.write(text)
            f.close()
    # FunctionalPrediction
    for i in range(len(FunctionalPrediction)):
        text = Feature_Config if mode else Network_Config
        text = text.replace("XX", name)
        text = text.replace("YY", root + "Datasets/FeatureMatrix/tabular_datasets/" + path) if mode else text.replace("YY", root + "Datasets/" + path)
        new_path = root + "Standards/" + FunctionalPrediction.iloc[:, 0][i]
        if mode:
            if ".csv" in path:
                text = text.replace("ZZ", ",")
            elif ".tsv" in path:
                text = text.replace("ZZ", "\\t")

        str = f""""name": "{FunctionalPrediction.iloc[:, 1][i]}",
            "task": "function_prediction",
            "path": "{new_path}",
            "test_size": 0.1,
            "folds": 5,
            "trials": 10,
            "gamma": {{
        "minimum": 1e-6,
                "maximum": 1e-1,
                "samples": 10
            }},
            "regularization": {{
        "minimum": 1e-3,
                "maximum": 1e4,
                "samples": 30
            }}
        """
        text = text.replace("AA", str)
        with (Path(p) / Path(f"FunctionalPrediction_{name}_{FunctionalPrediction.iloc[:, 1][i]}.json")).open("w") as f:
            f.write(text)
            f.close()


# Features
if __name__ == "__main__":
    for i in range(len(Features)):
        generate_config(Features.iloc[:, 0][i], Features.iloc[:, 1][i], True)
    for i in range(len(Networks)):
        generate_config(Networks.iloc[:, 0][i], Networks.iloc[:, 1][i], False)
