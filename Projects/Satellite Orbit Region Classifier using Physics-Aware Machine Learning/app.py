import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load("orbit_classifier_model.pkl")
scaler = joblib.load("scaler.pkl")

# Map numeric prediction to label
label_map = {0: 'LEO', 1: 'MEO', 2: 'GEO'}

# Physics-informed validator
def is_physically_possible(alt, vel):
    if alt > 45000 or alt < 100:
        return False
    if vel < 2.5 or vel > 9.5:
        return False
    if alt > 36000 and vel < 2.7:
        return False  # Too slow for GEO
    if alt > 36000 and vel > 3.5:
        return False  # Too fast for GEO
    if alt < 2000 and vel < 6.5:
        return False  # Too slow for LEO
    if alt < 1500 and vel > 9.0:
        return False  # Too fast for LEO
    if 2000 < alt < 10000 and vel < 3.8:
        return False  # Too slow for MEO
    if alt > 10000 and vel > 6.5:
        return False  # Too fast for MEO/GEO
    return True

# Streamlit config
st.set_page_config(page_title=" Orbital Classifier", layout="centered")
st.title(" Orbital Region Classifier")
st.markdown("""
A physics-aware ML model that classifies satellites as **LEO**, **MEO**, or **GEO**  
based on their **altitude**, **velocity**, and **inclination**.

Built for real-world space situational awareness 
""")
st.divider()

# User input
altitude = st.slider(" Altitude (km)", 100, 45000, 500)
velocity = st.slider(" Velocity (km/s)", 2.5, 9.5, 7.5, step=0.01)
inclination = st.slider(" Inclination (°)", 0, 180, 98)

# Predict
if st.button(" Predict Orbit Type"):
    if not is_physically_possible(altitude, velocity):
        st.error(" Physically Invalid Orbit Configuration!")
        st.markdown("""
        ###  Why Invalid?
        - Velocity too **low** or too **high** for this altitude  
        - Would result in **orbit decay**, **overshoot**, or **instability**

        Please enter values that correspond to a **stable Earth orbit**.
        """)
    else:
        features = np.array([[altitude, velocity, inclination]])
        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)[0]
        orbit_type = label_map[prediction]

        st.success(f" Predicted Orbit Type: **{orbit_type}**")

        # Confidence
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(features_scaled)[0]
            st.markdown("###  Model Confidence:")
            for i, label in label_map.items():
                st.write(f"{label}: {proba[i]*100:.2f}%")

st.divider()
st.caption("Developed by Suparna • M.Tech AI • Trained with real physics + ML ")

