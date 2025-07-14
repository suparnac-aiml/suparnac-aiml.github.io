Satellite Image Classification using EuroSAT + MobileNetV2


Overview:

This project classifies satellite images into 10 land cover classes using the EuroSAT dataset and a MobileNetV2 model fine-tuned through transfer learning.
It includes training code and the ability to deploy the trained model using Streamlit for real-time prediction.

Dataset:

EuroSAT Dataset (RGB version)
- 27,002 images
- 10 land cover classes
- Resized to 128x128
- 80% used for training (21,602 images)
- 20% used for validation (5,400 images)

Model Architecture:

- Base Model: MobileNetV2 (pretrained on ImageNet, include_top=False)
- Layers Added:
    • GlobalAveragePooling2D
    • Dense(128) with ReLU
    • Dense(10) with Softmax
- Base model frozen (not trainable)
- Optimizer: Adam
- Loss Function: sparse_categorical_crossentropy
- Metric: Accuracy

Training Output:

- Epochs: 5
- Training Accuracy: ~90%
- Loss: Reduced from 0.61 to ~0.31
- Time per Epoch: ~24 seconds (on GPU)
- Model Saved: satellite_classifier_model.h5

Requirements:

- Python 3.8+
- TensorFlow 2.x
- NumPy
- PIL (Pillow)
- Streamlit

To Train:

    python satellite_classifier_model.py

To Launch Streamlit App:

    streamlit run app.py --server.maxUploadSize=1024

Note: Supports jpg, jpeg, png, tif, and tiff image formats.

Output via Web App:

- Upload an RGB satellite image
- Model predicts and displays land cover class
- Shows confidence percentage

Author:

Suparna C
July 2025
