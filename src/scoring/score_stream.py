import sys
import pathlib
import pandas as pd
import datetime

# Add src to path
sys.path.append(str(pathlib.Path(__file__).parent.parent))

from utils.config import load_config
from utils.io import load_model
from ingest.zeek_reader import read_zeek_log
from features.build_windows import build_features

def score_stream():
    print("Starting live scoring...")
    
    # 1. Load Config & Model
    config = load_config("configs/default.yaml")
    model_path = config['paths']['models']['baselines'] + "/iso_forest.pkl"
    
    if not pathlib.Path(model_path).exists():
        print(f"Error: Model not found at {model_path}. Run Phase 3 first.")
        return

    model = load_model(model_path)
    print("Model loaded.")
    
    # 2. Ingest "Live" Data (Simulated)
    # We generate a new batch of dummy data. 
    # In a real system, this would tail a log file or read from a stream.
    print("Ingesting live traffic...")
    df = read_zeek_log(None) # Generates dummy data
    
    # 3. Build Features
    features = build_features(df, window_size=config['window_size'])
    
    # 4. Predict
    feature_cols = ['bytes_sum', 'duration_mean', 'pkt_count']
    X = features[feature_cols]
    
    predictions = model.predict(X)
    features['anomaly'] = predictions
    
    # 5. Alert
    anomalies = features[features['anomaly'] == -1]
    
    if not anomalies.empty:
        print(f"Detected {len(anomalies)} anomalies!")
        
        log_path = config['paths']['logs']['alerts']
        with open(log_path, "a") as f:
            for index, row in anomalies.iterrows():
                timestamp = datetime.datetime.now().isoformat()
                alert_msg = (
                    f"[{timestamp}] [ALERT] Anomaly detected! "
                    f"Source IP: {row['id.orig_h']}, "
                    f"Bytes: {row['bytes_sum']:.2f}, "
                    f"Duration: {row['duration_mean']:.2f}, "
                    f"Pkts: {row['pkt_count']}"
                )
                print(alert_msg)
                f.write(alert_msg + "\n")
        print(f"Alerts written to {log_path}")
    else:
        print("No anomalies detected.")

if __name__ == "__main__":
    score_stream()
