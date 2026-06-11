import streamlit as st
import pandas as pd
import sys
import os

# Fix import path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, project_root)

from src.predict import predict_churn

# Page Title
st.set_page_config(
    page_title="Telecom Churn Prediction",
    page_icon="📱"
)

st.title("📱 Telecom Customer Churn Prediction")

st.write(
    "Predict whether a telecom customer is likely to churn."
)

st.info(
    "Categorical values are encoded as numeric categories used during model training."
)

# Inputs
age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=35
)

tenure_months = st.number_input(
    "Tenure Months",
    min_value=0,
    max_value=120,
    value=12
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=500.0
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=5000.0
)

# Dropdowns
gender = st.selectbox(
    "Gender (Encoded)",
    [0, 1, 2]
)

region_circle = st.selectbox(
    "Region Circle (Encoded)",
    [0, 1, 2, 3, 4]
)

plan_type = st.selectbox(
    "Plan Type (Encoded)",
    [0, 1]
)

# Predict Button
if st.button("Predict Churn"):

    customer_data = {
        "gender": gender,
        "age": age,
        "region_circle": region_circle,
        "connection_type": 1,
        "plan_type": plan_type,
        "contract_type": 1,
        "base_plan_category": 1,
        "tenure_months": tenure_months,
        "monthly_charges": monthly_charges,
        "total_charges": total_charges,
        "avg_data_gb_month": 10,
        "avg_voice_mins_month": 300,
        "sms_count_month": 50,
        "overage_charges": 0,
        "is_family_plan": 0,
        "is_multi_service": 0,
        "network_issues_3m": 0,
        "dropped_call_rate": 1,
        "avg_data_speed_mbps": 50,
        "num_complaints_3m": 0,
        "num_complaints_12m": 1,
        "call_center_interactions_3m": 1,
        "last_complaint_resolution_days": 2,
        "app_logins_30d": 20,
        "selfcare_transactions_30d": 5,
        "auto_pay_enrolled": 1,
        "late_payment_flag_3m": 0,
        "avg_payment_delay_days": 0,
        "arpu": 500,
        "segment_value": 1,
        "nps_score": 8,
        "service_rating_last_6m": 4,
        "received_competitor_offer_flag": 0,
        "retention_offer_accepted_flag": 0
    }

    prediction, probability = predict_churn(customer_data)

    st.subheader("Prediction Result")

    st.write(
        f"Churn Probability: {probability:.2%}"
    )

    if prediction == 1:
        st.error("⚠ Customer Likely To Churn")

        st.subheader("Retention Strategy")

        st.write("• Assign Dedicated Relationship Manager")
        st.write("• Offer Premium Loyalty Discount")
        st.write("• Provide Free Data Booster")
        st.write("• Prioritize Complaint Resolution")

    else:
        st.success("✅ Customer Likely To Stay")