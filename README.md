# AI Network Guardian

## 1. Architectural Overview

**Objective:**  
Build a Python-based Network Intrusion Detection System (NIDS) using unsupervised learning (Isolation Forest) to detect behavioral anomalies such as beaconing and data exfiltration.

**Pipeline:**
- **Input:** Zeek `conn.log` (JSON) or PCAP files  
- **Processing:** Aggregate flows into time-windowed statistics  
- **Model:** Isolation Forest (learns normal behavior)  
- **Output:** Alert stream for anomalous traffic  

## 2. Technical Constraints & Stack

- **Language:** Python 3.10+  
- **Libraries:** `pandas`, `scikit-learn`, `scapy`, `joblib`  
- Must support streaming-style processing without memory leaks  
- Clean, modular, PEP 8–compliant code  

## 3. Required Directory Structure

```text
AI_Network_Guardian/
├── configs/
│   └── default.yaml
├── data/
│   ├── raw/
│   ├── features/
│   └── labels/
├── models/
│   └── baselines/
├── src/
│   ├── ingest/
│   │   └── zeek_reader.py
│   ├── features/
│   │   └── build_windows.py
│   ├── models/
│   │   └── train_anomaly.py
│   ├── scoring/
│   │   └── score_stream.py
│   └── utils/
│       ├── config.py
│       └── io.py
├── requirements.txt
└── README.md
```
## 4. Execution Roadmap

Phase 1: Create directories, dependencies, and config file.  
Phase 2: Parse Zeek logs and aggregate traffic by source IP and time window.  
Phase 3: Train Isolation Forest on normal behavior and save the model.  
Phase 4: Score new traffic and log alerts for anomalies.

## 5. Definition of Done

1. Project scaffold builds successfully.  
2. Model training outputs a valid .pkl file.  
3. Scoring detects synthetic data exfiltration.  
4. No hardcoded paths; all config-driven.

## Setup
1. Install requirements: `pip install -r requirements.txt`
2. (Windows users) Install Npcap: https://npcap.com/

## How to Run
1. **Train the AI**: Run `python src/train_model.py`. This creates the "brain" (model.pkl).
2. **Start Protection**: Run `python src/live_detect.py`.

## Data
- The project currently uses dummy data in `train_model.py`.
- To make it real, download the **CICIDS2017** dataset, convert it to CSV, and load it in the training script.
