import joblib
import pandas as pd
from scapy.all import sniff
from feature_extractor import TrafficFeatureExtractor
import datetime

# Load the trained brain
MODEL_PATH = '../models/traffic_classifier.pkl'
try:
    clf = joblib.load(MODEL_PATH)
    print("AI Model Loaded Successfully.")
except:
    print("Error: No model found. Run 'train_model.py' first!")
    exit()

extractor = TrafficFeatureExtractor()

def process_live_packet(packet):
    # 1. Extract features from the raw packet
    features = extractor.process_packet(packet)
    
    if features:
        # 2. Prepare data for the AI (must match training format)
        df_input = pd.DataFrame([features])
        
        # 3. Predict
        prediction = clf.predict(df_input)[0]
        
        # 4. Act
        if prediction == 1:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            alert_msg = f"[ALERT] {timestamp} | Threat Detected! Source: {features.get('src_port')} -> Dest: {features.get('dst_port')}"
            print(alert_msg)
            
            # Log it
            with open("../logs/threat_log.txt", "a") as f:
                f.write(alert_msg + "\n")
        else:
            # Optional: Print safe traffic to see it working
            # print(f"[Safe] Pkt Len: {features['packet_length']}")
            pass

print("Starting Network Sniffer... (Press Ctrl+C to stop)")
# Sniff packets on the default interface (store=0 saves memory)
sniff(prn=process_live_packet, store=0)
