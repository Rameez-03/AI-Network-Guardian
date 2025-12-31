import sys
import pathlib
import pandas as pd
from sklearn.ensemble import IsolationForest

# Add src to path to allow imports
sys.path.append(str(pathlib.Path(__file__).parent.parent))

from utils.config import load_config
from utils.io import load_parquet, save_model

def train_model():
    print("Starting model training...")
    
    # 1. Load Config
    config = load_config("configs/default.yaml")
    
    # 2. Load Data
    features_path = config['paths']['data']['features'] + "/train_features.parquet"
    if not pathlib.Path(features_path).exists():
        print(f"Error: Features file not found at {features_path}. Run Phase 2 first.")
        return

    df = load_parquet(features_path)
    print(f"Loaded {len(df)} training records.")
    
    # 3. Preprocessing
    # Drop non-feature columns (IP, Timestamp)
    # We only want behavioral features: bytes_sum, duration_mean, pkt_count
    feature_cols = ['bytes_sum', 'duration_mean', 'pkt_count']
    X = df[feature_cols]
    
    # 4. Train Isolation Forest
    print(f"Training Isolation Forest (contamination={config['contamination']})...")
    clf = IsolationForest(
        contamination=config['contamination'],
        random_state=42,
        n_jobs=-1
    )
    clf.fit(X)
    
    # 5. Save Model
    model_path = config['paths']['models']['baselines'] + "/iso_forest.pkl"
    save_model(clf, model_path)
    print("Training complete.")

if __name__ == "__main__":
    train_model()
