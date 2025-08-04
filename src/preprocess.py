# src/preprocess.py

import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Correct type hint and use raw string (r"...") to avoid path errors
def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def encode_data(df: pd.DataFrame):
    df_encoded = df.copy()
    encoders = {}

    for col in df_encoded.select_dtypes(include='object').columns:
        le = LabelEncoder()
        df_encoded[col] = le.fit_transform(df_encoded[col])
        encoders[col] = le

    return df_encoded, encoders
