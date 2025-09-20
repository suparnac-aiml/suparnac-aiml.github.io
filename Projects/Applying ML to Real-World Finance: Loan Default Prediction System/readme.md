# Personal Loan Prediction System

## Project Overview    
This repository contains a machine learning project aimed at predicting whether a bank customer will accept a personal loan offer. Using financial and demographic data, multiple models were developed and evaluated to provide the most accurate loan acceptance predictions.    

## Dataset    
The project utilizes the Bank Personal Loan Modelling dataset which includes the following features:    

- `ID`: Unique customer identifier (removed in preprocessing)    
- `Age`: Customer age in years    
- `Experience`: Years of professional experience    
- `Income`: Annual income of the customer    
- `ZIP Code`: Customer’s postal code (removed in preprocessing)    
- `Family`: Number of family members    
- `CCAvg`: Average monthly credit card spending    
- `Education`: Education level (1: Undergrad, 2: Graduate, 3: Advanced/Professional)    
- `Mortgage`: Value of house mortgage (if any)    
- `Personal Loan`: Target variable (0: No loan accepted, 1: Loan accepted)    
- `Securities Account`: Whether the customer has securities account (binary)    
- `CD Account`: Whether the customer has certificate of deposit (binary)    
- `Online`: Online banking status (binary)    
- `CreditCard`: Whether the customer has a credit card (binary)    

       
 
## Features   
- Data loading and cleaning   
- Handling missing data and feature engineering   
- Exploratory Data Analysis (EDA) with visualizations   
- Model building using Logistic Regression, Decision Tree, and Random Forest   
- Model evaluation with accuracy, precision, recall, F1-score, and confusion matrices   
- Selection of the best performing model based on F1-score   



## Results   

- Logistic Regression achieved the best performance with ~95% accuracy and strong recall.   
- Income, credit history, and education proved significant features influencing loan acceptance.   
- Business insights and recommendations are included for real-world application.   
   
## Future Work

- Incorporate more features like employment history and credit score   
- Explore ensemble methods like XGBoost or neural networks   
- Build a web app for real-time loan eligibility prediction   
- Implement explainable AI for better decision transparency   



