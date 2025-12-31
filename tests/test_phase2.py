import sys
import os
import pathlib

# Add src to path
sys.path.append(str(pathlib.Path(__file__).parent.parent / "src"))

from ingest.zeek_reader import read_zeek_log
from features.build_windows import build_features
from utils.io import save_parquet
from utils.config import load_config

def test_phase2():
    print("Testing Phase 2...")
    
    # 1. Load Config
    config = load_config("configs/default.yaml")
    print("Config loaded.")
    
    # 2. Ingest (Dummy Data)
    df = read_zeek_log(None)
    print(f"Ingested {len(df)} records.")
    print(df.head())
    
    # 3. Build Features
    features = build_features(df, window_size=config['window_size'])
    print(f"Built {len(features)} feature vectors.")
    print(features.head())
    
    # 4. Save
    save_parquet(features, config['paths']['data']['features'] + "/train_features.parquet")
    print("Test passed!")

if __name__ == "__main__":
    test_phase2()
