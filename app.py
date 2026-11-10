import streamlit as st
import numpy as np
import pickle

# Load model & scaler
model = pickle.load(open("rf_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("Credit Card Fraud Detection System")
st.write("Enter all 30 features below to check if the transaction is Fraud or Legit.")

# Create inputs for all 30 features
feature_names = [
    "Time", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8",
    "V9", "V10", "V11", "V12", "V13", "V14", "V15", "V16",
    "V17", "V18", "V19", "V20", "V21", "V22", "V23", "V24",
    "V25", "V26", "V27", "V28", "Amount"
]

inputs = []

for feature in feature_names:
    value = st.number_input(f"Enter {feature}", value=0.0, format="%.5f")
    inputs.append(value)

# Convert to numpy array
input_array = np.array(inputs).reshape(1, -1)

# Scale
scaled_input = scaler.transform(input_array)

# Predict
if st.button("Detect Fraud"):
    prediction = model.predict(scaled_input)
    result = "🚨 Fraud Transaction" if prediction[0] == 1 else "✅ Legit Transaction"

    st.subheader("Prediction Result:")
    st.write(result)
