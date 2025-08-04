import pandas as pd
from src.preprocess import encode_data
from src.utils import load_model
from src.task_config import task_configs

def predict_all_tasks(new_sample: dict):
    # Convert sample input to DataFrame
    df = pd.DataFrame([new_sample])

    # Encode features
    df_encoded, _ = encode_data(df)

    for task_key, config in task_configs.items():
        model = load_model(config['model_path'])

        try:
            # Align columns with expected by the model
            expected_columns = model.feature_names_in_
            missing_cols = set(expected_columns) - set(df_encoded.columns)
            for col in missing_cols:
                df_encoded[col] = 0  # fill missing columns with zero
            df_aligned = df_encoded[expected_columns]

            # Make prediction
            prediction = model.predict(df_aligned)
            print(f"\n✅ Prediction for {task_key.upper()} ({config['task_type']}): {prediction[0]}")
        except Exception as e:
            print(f"\n❌ Failed to predict {task_key}: {e}")

if __name__ == "__main__":
    new_sample_input = {
        'Year': 2023,
        'Country': 'USA',
        'Industry': 'Healthcare',
        'Attack Type': 'Ransomware',
        'Severity': 'High',
        'Records Affected': 100000,
        'Target Industry': 'Government',
        'Financial Loss (in Million $)': 25.5,
        'Number of Affected Users': 500000,
        'Attack Source': 'External',
        'Security Vulnerability Type': 'Phishing',
        'Defense Mechanism Used': 'Firewall',
        'Incident Resolution Time (in Hours)': 12
    }

    predict_all_tasks(new_sample_input)
