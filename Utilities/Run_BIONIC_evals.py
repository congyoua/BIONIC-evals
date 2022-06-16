import argparse
from pathlib import Path
from bioniceval.main import evaluate


def main_(trial):
    p = Path(r"D:\BIONIC\Configs")
    files = [f for f in sorted(p.iterdir()) if f.is_file() and not f.name.startswith(".") and ".json" in f.name]
    evaluate(files[trial])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--trial", type=int, required=True)
    args = parser.parse_args()
    main_(args.trial)
