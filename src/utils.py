import joblib
import os

def load_model(path: str):
    base_path = os.path.dirname(os.path.dirname(__file__))  # get project root
    full_path = os.path.join(base_path, path)

    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Model file not found at: {full_path}")

    return joblib.load(full_path)
