# src/preprocess.py

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from typing import Tuple, Dict

def load_data(path: str) -> pd.DataFrame:
    """Load data from a CSV file."""
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found at path: {path}")
    except Exception as e:
        raise Exception(f"Error loading CSV file: {e}")

def encode_data(df: pd.DataFrame) -> Tuple[pd.DataFrame, Dict[str, LabelEncoder]]:
    """
    Encode all object-type columns in a DataFrame using LabelEncoder.

    Returns:
        - Encoded DataFrame
        - Dictionary of encoders for each encoded column
    """
    df_encoded = df.copy()
    encoders: Dict[str, LabelEncoder] = {}

    for col in df_encoded.select_dtypes(include='object').columns:
        le = LabelEncoder()
        df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))
        encoders[col] = le

    return df_encoded, encoders
