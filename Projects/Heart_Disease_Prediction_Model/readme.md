# Heart Disease Prediction Project    

This project aims to build a machine learning system that predicts the presence of heart disease in patients based on their clinical and physiological data. By analyzing key health features, the system helps identify individuals at risk, enabling early intervention.    

## Dataset Format

- The data is provided in CSV format.   
- Original features include:    
  - Age (numeric)   
  - Sex (binary)   
  - Chest pain type (nominal categorical)   
  - Resting blood pressure (numeric)   
  - Serum cholesterol (numeric)   
  - Fasting blood sugar (binary)   
  - Resting electrocardiogram results (nominal categorical)   
  - Maximum heart rate achieved (numeric)   
  - Exercise induced angina (binary)   
  - ST depression induced by exercise relative to rest (numeric)   
  - The slope of the peak exercise ST segment (nominal categorical)   
  - Target variable indicating presence (1) or absence (0) of heart disease   

## Dependencies   

- Python 3.x   
- pandas   
- scikit-learn   
- matplotlib   
- seaborn   

## One-Hot Encoding

Categorical features such as chest pain type, resting ECG, and ST slope are one-hot encoded. This conversion creates separate binary columns for each category, avoiding misleading the model into assuming any ordinal relationship between categories, which improves model performance.   
## Models Used and Results

- Logistic Regression: Achieved approximately 86% accuracy.   
- Random Forest Classifier: Improved accuracy to about 92%, better capturing complex relationships in data.   

The Random Forest model was selected as the best performing model based on accuracy and classification metrics.   

## Key points summarizing the heart disease prediction analysis:

- Data preprocessing included converting categorical features to numeric, scaling, and splitting into training and test sets.   
- Logistic Regression achieved 86% accuracy, demonstrating a solid baseline for binary classification.   
- A Random Forest model improved accuracy to over 92%, showing better performance by capturing complex feature interactions.   
- Feature importance analysis from Random Forest highlights the most influential patient attributes for predicting heart disease risk.   
- The Random Forest improved accuracy by approximately 6% compared to Logistic Regression.   
- Precision, recall, and F1-score for detecting heart disease (class 1) also improved by around 7%.   
- Confusion matrix values for Random Forest:   
	*	True Negatives: 154   
	*	False Positives: 14   
	*	False Negatives: 13   
	*	True Positives: 176   
This numerical summary shows that Random Forest provides more reliable heart disease prediction, reducing both false negatives and false positives significantly compared to Logistic Regression.   

---
