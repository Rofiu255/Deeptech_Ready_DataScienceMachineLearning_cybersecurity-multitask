# app.py
import streamlit as st
import pandas as pd
from src.preprocess import encode_data
from src.utils import load_model
from src.task_config import task_configs

st.set_page_config(page_title="Cybersecurity Threat Predictor", layout="wide")

st.title("🔐 Cybersecurity Threat Intelligence Predictor")

# Input form
st.subheader("📋 Enter Incident Details Below:")

with st.form("cyber_form"):
    year = st.number_input("Year", min_value=2000, max_value=2030, value=2023)
    country = st.text_input("Country", value="USA")
    industry = st.selectbox("Industry", ["Healthcare", "Finance", "Education", "Retail", "Technology", "Government"])
    attack_type = st.selectbox("Attack Type", ["Ransomware", "Phishing", "DDoS", "Malware", "Data Breach"])
    severity = st.selectbox("Severity", ["Low", "Medium", "High", "Critical"])
    records_affected = st.number_input("Records Affected", min_value=0, value=100000)
    target_industry = st.selectbox("Target Industry", ["Healthcare", "Finance", "Education", "Retail", "Technology", "Government"])
    financial_loss = st.number_input("Financial Loss (in Million $)", min_value=0.0, value=25.5)
    num_users = st.number_input("Number of Affected Users", min_value=0, value=500000)
    attack_source = st.selectbox("Attack Source", ["Internal", "External", "Third-party"])
    vulnerability_type = st.selectbox("Security Vulnerability Type", ["Phishing", "SQL Injection", "Zero-day", "Misconfiguration"])
    defense = st.selectbox("Defense Mechanism Used", ["Firewall", "Antivirus", "SIEM", "2FA", "Endpoint Detection"])
    resolution_time = st.number_input("Incident Resolution Time (in Hours)", min_value=0, value=12)

    submit = st.form_submit_button("🔮 Predict")

if submit:
    new_sample = {
        'Year': year,
        'Country': country,
        'Industry': industry,
        'Attack Type': attack_type,
        'Severity': severity,
        'Records Affected': records_affected,
        'Target Industry': target_industry,
        'Financial Loss (in Million $)': financial_loss,
        'Number of Affected Users': num_users,
        'Attack Source': attack_source,
        'Security Vulnerability Type': vulnerability_type,
        'Defense Mechanism Used': defense,
        'Incident Resolution Time (in Hours)': resolution_time
    }

    df = pd.DataFrame([new_sample])
    df_encoded, _ = encode_data(df)

    st.subheader("📊 Predictions")

    for task_key, config in task_configs.items():
        model = load_model(config['model_path'])

        try:
            # Ensure model features match input
            expected_cols = model.feature_names_in_
            for col in set(expected_cols) - set(df_encoded.columns):
                df_encoded[col] = 0
            df_aligned = df_encoded[expected_cols]

            prediction = model.predict(df_aligned)
            st.success(f"✅ **{task_key.upper()}** ({config['task_type']}): **{prediction[0]}**")
        except Exception as e:
            st.error(f"❌ Prediction failed for {task_key}: {e}")
