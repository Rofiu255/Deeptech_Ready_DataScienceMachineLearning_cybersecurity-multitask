# src/train_model.py

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import classification_report, mean_squared_error
from src.preprocess import load_data, encode_data
from src.utils import save_model
from src.task_config import task_configs

def train_task(task_key):
    config = task_configs[task_key]
    target_col = config['target']
    model_path = config['model_path']
    task_type = config['task_type']

    df = load_data("data/Global_Cybersecurity_Threats_2015-2024.csv")
    df_encoded, encoders = encode_data(df)

    X = df_encoded.drop(columns=[target_col])
    y = df_encoded[target_col]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y if task_type == "classification" else None)

    if task_type == "classification":
        model = RandomForestClassifier()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        print(f"\n=== {task_key.upper()} CLASSIFICATION REPORT ===")
        print(classification_report(y_test, y_pred))

    else:
        model = RandomForestRegressor()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print(f"\n=== {task_key.upper()} REGRESSION MSE ===")
        print(f"MSE: {mse:.2f}")

    save_model(model, model_path)

if __name__ == "__main__":
    for task_key in task_configs.keys():
        train_task(task_key)
