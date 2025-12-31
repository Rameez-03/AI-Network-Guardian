import pandas as pd
import numpy as np
import time

def generate_dummy_data(num_records=1000):
    """
    Generate synthetic network traffic data.
    """
    print("Generating dummy data...")
    
    # Normal traffic
    normal_records = int(num_records * 0.95)
    anomalous_records = num_records - normal_records
    
    data = {
        'ts': time.time() - np.random.randint(0, 3600, num_records), # Past hour
        'id.orig_h': ['192.168.1.{}'.format(np.random.randint(1, 20)) for _ in range(num_records)],
        'id.resp_h': ['10.0.0.{}'.format(np.random.randint(1, 255)) for _ in range(num_records)],
        'orig_bytes': np.concatenate([
            np.random.normal(500, 100, normal_records), # Normal
            np.random.normal(10000, 2000, anomalous_records) # Anomaly (Exfiltration)
        ]),
        'resp_bytes': np.random.normal(500, 100, num_records),
        'duration': np.concatenate([
            np.random.exponential(1, normal_records),
            np.random.exponential(10, anomalous_records) # Long duration
        ]),
        'proto': np.random.choice(['tcp', 'udp'], num_records)
    }
    
    df = pd.DataFrame(data)
    
    # Ensure non-negative
    df['orig_bytes'] = df['orig_bytes'].abs()
    df['resp_bytes'] = df['resp_bytes'].abs()
    
    return df

def read_zeek_log(filepath):
    """
    Read Zeek log file or generate dummy data if file doesn't exist.
    """
    if filepath and pathlib.Path(filepath).exists():
        # Simplified reader for standard Zeek JSON
        try:
            return pd.read_json(filepath, lines=True)
        except ValueError:
            # Fallback for TSV if needed, but assuming JSON for now as per blueprint preference or default
            pass
            
    # Fallback to dummy data
    return generate_dummy_data()

import pathlib
