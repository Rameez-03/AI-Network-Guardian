import pandas as pd
import numpy as np

def build_features(df, window_size=60):
    """
    Aggregate flows into time windows and calculate features.
    """
    print("Building features...")
    
    # Ensure timestamp is datetime
    if not np.issubdtype(df['ts'].dtype, np.datetime64):
        df['ts'] = pd.to_datetime(df['ts'], unit='s')
        
    # Set index to timestamp for resampling
    df = df.set_index('ts')
    
    # Group by Source IP and Time Window
    # We use a trick to group by both: resample time, then group by IP
    # But standard way is groupby([pd.Grouper(freq=f'{window_size}s'), 'id.orig_h'])
    
    grouped = df.groupby([pd.Grouper(freq=f'{window_size}s'), 'id.orig_h'])
    
    features = grouped.agg(
        bytes_sum=('orig_bytes', lambda x: x.sum() + df.loc[x.index, 'resp_bytes'].sum()),
        duration_mean=('duration', 'mean'),
        pkt_count=('orig_bytes', 'count') # Proxy for packet count
    ).reset_index()
    
    # Fill NA
    features = features.fillna(0)
    
    print(f"Generated {len(features)} feature vectors.")
    return features
