# AI Network Guardian

## Setup
1. Install requirements: `pip install -r requirements.txt`
2. (Windows users) Install Npcap: https://npcap.com/

## How to Run
1. **Train the AI**: Run `python src/train_model.py`. This creates the "brain" (model.pkl).
2. **Start Protection**: Run `python src/live_detect.py`.

## Data
- The project currently uses dummy data in `train_model.py`.
- To make it real, download the **CICIDS2017** dataset, convert it to CSV, and load it in the training script.
