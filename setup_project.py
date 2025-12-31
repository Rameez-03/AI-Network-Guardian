import os
import pathlib

def create_structure():
    # Define the directory structure
    directories = [
        "configs",
        "data/raw",
        "data/features",
        "data/labels",
        "models/baselines",
        "src/ingest",
        "src/features",
        "src/models",
        "src/scoring",
        "src/utils",
        "logs"
    ]

    # Create directories
    for directory in directories:
        path = pathlib.Path(directory)
        path.mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {path}")

    # Define files to create (empty placeholders)
    files = [
        "src/ingest/zeek_reader.py",
        "src/features/build_windows.py",
        "src/models/train_anomaly.py",
        "src/scoring/score_stream.py",
        "src/utils/config.py",
        "src/utils/io.py",
        "configs/default.yaml",
        "logs/alerts.log"
    ]

    for file_path in files:
        path = pathlib.Path(file_path)
        if not path.exists():
            path.touch()
            print(f"Created file: {path}")
        else:
            print(f"File already exists: {path}")

if __name__ == "__main__":
    create_structure()
