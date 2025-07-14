import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image

# Load model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("satellite_classifier_model.h5")
    return model

model = load_model()

# Class names from EuroSAT dataset (10 classes)
class_names = [
    'Annual Crop', 'Forest', 'Herbaceous Vegetation', 'Highway', 'Industrial',
    'Pasture', 'Permanent Crop', 'Residential', 'River', 'Sea/Lake'
]

# Page config
st.set_page_config(page_title="Satellite Image Classifier", layout="centered")
st.title("EuroSAT Land Cover Classifier")
st.markdown("""
Upload a satellite image and get its predicted land use category  
based on the **EuroSAT dataset** and a fine-tuned **MobileNetV2** model.
""")

st.divider()

# Image upload
uploaded_file = st.file_uploader(" Upload a satellite image (RGB)", type=["jpg", "jpeg", "png", "tiff", "tif"])

# Prediction logic
def predict(image):
    image = image.resize((128, 128))
    img_array = np.array(image) / 255.0  # normalize
    img_array = np.expand_dims(img_array, axis=0)  # batch dimension
    preds = model.predict(img_array)
    pred_class = class_names[np.argmax(preds)]
    confidence = np.max(preds)
    return pred_class, confidence

# Display
if uploaded_file:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption=" Uploaded Image", use_column_width=True)

    if st.button("Predict"):
        with st.spinner("Classifying..."):
            label, conf = predict(image)
            st.success(f" Predicted Class: **{label}**")
            st.markdown(f" Confidence: `{conf*100:.2f}%`")

st.divider()
st.caption("Built with using MobileNetV2 + EuroSAT | Suparna Reddy")

