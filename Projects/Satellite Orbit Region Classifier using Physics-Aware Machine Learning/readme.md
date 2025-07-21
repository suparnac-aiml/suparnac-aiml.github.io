name: Satellite Orbit Region Classifier using Physics-Aware Machine Learning    
description: >    
  A machine learning project that classifies satellites into LEO, MEO, or GEO orbital regions using physics-informed data features. Includes a robust Streamlit app for user interaction, validation, and demonstration.    
    
author: Suparna (M.Tech AI)    

 
# ----------------------------------------    
# Project Overview    
# ----------------------------------------    
project_title: "Satellite Orbit Region Classifier using Physics-Aware Machine Learning"        
summary: |       
  This project leverages machine learning principles and physics constraints to classify satellite orbits into:    
    - Low Earth Orbit (LEO)    
    - Medium Earth Orbit (MEO)    
    - Geostationary Orbit (GEO)    

  Users predict the orbital region for satellites based on altitude, velocity, and inclination. The workflow includes:    
    - Physics-guided synthetic data generation   
    - Handling class imbalance in training data    
    - Model training with SVM and class weighting    
    - Validation using physics rule-based checks    
    - Interactive prediction (and validation) through a Streamlit web app    
  
# ----------------------------------------    
# Directory Structure    
# ----------------------------------------    
structure: |    
  .
  ├── satellite_orbital_classification_dataset.csv    
  ├── orbit_classifier_model.pkl    
  ├── scaler.pkl    
  ├── app.py    
  ├── satellite_orbital_classification.ipynb    
  ├── README.md    
 

# ----------------------------------------     
# Requirements    
# ----------------------------------------    
requirements:    
  - python >=3.8    
  - numpy   
  - pandas    
  - scikit-learn     
  - seaborn       
  - matplotlib    
  - streamlit    
  - joblib    

# ----------------------------------------      
# Usage    
# ----------------------------------------    
installation: |     
  
  1. Install dependencies    

  2. (Optional) Train the model and generate dataset by re-running the code    
 
run_streamlit_app: |    
  1. Run the Streamlit app:   
     ```    
     streamlit run app.py    
     ```    
  2. Set satellite parameters (Altitude, Velocity, Inclination) using interactive sliders.    
  3. The app predicts the orbital class (LEO, MEO, GEO), checks for physical validity, and displays a result.    
  4. If parameters are unphysical, an error with explanation is given.    

# ----------------------------------------    
# Features    
# ----------------------------------------    
features:   
  - Synthetic dataset generated using physical constraints    
  - Handles real-world data imbalance    
  - SVM classifier with automated class weighting    
  - Physics-aware validation for robust predictions    
  - Intuitive web interface (Streamlit) for experimentation    
  - Explainable error reporting for invalid entries   
 
# ----------------------------------------    
# Model Details    
# ----------------------------------------    
model_details:    
  input_features:    
    - altitude_km: "Satellite altitude above sea level (km)"     
    - velocity_kmps: "Orbital velocity (km/s)"    
    - inclination_deg: "Inclination with respect to the Earth's equator (degrees)"    
  output_classes:    
    - 0: "LEO (Low Earth Orbit)"     
    - 1: "MEO (Medium Earth Orbit)"    
    - 2: "GEO (Geostationary Orbit)"    
  classifier: "scikit-learn SVC (Support Vector Machine) with class_weight='balanced'"    
  evaluation_metrics:    
    - confusion_matrix    
    - precision    
    - recall    
    - f1-score    
    - accuracy    

