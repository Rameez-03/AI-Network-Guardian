import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

# CONFIG
DATA_PATH = '../data/processed_csv/training_data.csv'
MODEL_PATH = '../models/traffic_classifier.pkl'

def train_model():
    print("Loading dataset...")
    
    # ---------------------------------------------------------
    # NOTE: Since you don't have a dataset yet, we create a 
    # dummy one here to ensure the script runs.
    # REPLACE THIS with loading your real CICIDS2017 CSV later.
    # ---------------------------------------------------------
    data = {
        'packet_length': [60, 1500, 60, 1500, 40, 9999, 50, 20],  # 9999 is anomaly
        'protocol_type': [6, 6, 17, 17, 6, 6, 17, 6],
        'src_port': [80, 443, 53, 53, 22, 666, 80, 21],
        'dst_port': [12345, 12346, 5678, 5679, 1111, 9999, 3333, 22],
        'label': [0, 0, 0, 0, 0, 1, 0, 1]  # 0 = Safe, 1 = Threat
    }
    df = pd.DataFrame(data)
    # ---------------------------------------------------------

    X = df.drop('label', axis=1)
    y = df['label']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    # Initialize AI (Random Forest is great for behavior analysis)
    clf = RandomForestClassifier(n_estimators=100)
    
    print("Training AI model...")
    clf.fit(X_train, y_train)

    # Evaluate
    preds = clf.predict(X_test)
    print(f"Model Accuracy: {accuracy_score(y_test, preds)}")
    print(classification_report(y_test, preds))

    # Save the brain
    joblib.dump(clf, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    train_model()
