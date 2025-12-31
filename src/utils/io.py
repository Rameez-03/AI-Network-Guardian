import pandas as pd
import joblib
import pathlib

def save_parquet(df, filepath):
    """
    Save DataFrame to Parquet.
    """
    path = pathlib.Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, index=False)
    print(f"Saved data to {path}")

def load_parquet(filepath):
    """
    Load DataFrame from Parquet.
    """
    return pd.read_parquet(filepath)

def save_model(model, filepath):
    """
    Save model to Pickle.
    """
    path = pathlib.Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)
    print(f"Saved model to {path}")

def load_model(filepath):
    """
    Load model from Pickle.
    """
    return joblib.load(filepath)
