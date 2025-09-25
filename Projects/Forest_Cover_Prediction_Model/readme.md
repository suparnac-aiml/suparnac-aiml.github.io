# Forest Cover Type Prediction   

## About the Project    
This project aims to accurately predict forest cover types for given land patches based on environmental and cartographic features. Forest cover classification is crucial for sustainable forest management, conservation planning, wildfire risk assessment, and ecological monitoring. Automated prediction models can help forest departments and environmental agencies make informed decisions about land use and biodiversity protection.   

The importance of this project lies in its application to forest management efforts in places like Roosevelt National Forest and other similar forested regions. Using machine learning models to classify forest cover types reduces manual effort and enhances accuracy and timeliness of forest data monitoring. This is especially useful in the era of rapid climate change and increased wildfire events, where adaptive and proactive forest management becomes essential.    

## About the Dataset   
The dataset originates from the Roosevelt National Forest in northern Colorado. It consists of 15,120 samples of 30m by 30m land patches, each labeled with one of seven forest cover types:    

- 1 - Spruce/Fir   
- 2 - Lodgepole Pine   
- 3 - Ponderosa Pine   
- 4 - Cottonwood/Willow     
- 5 - Aspen   
- 6 - Douglas-fir   
- 7 - Krummholz   

Features include continuous environmental variables such as elevation, aspect, slope, distances to hydrology, roadways, and fire points, and hillshade indices at multiple times of day. Additionally, there are four categorical binary wilderness area indicators and forty soil type binary indicators representing various geological classifications.    

The dataset is clean, balanced across classes, and contains no missing values, making it well suited for supervised machine learning classification approaches.    

## Dependencies    
The following Python packages are required to run the code:   

- pandas   
- numpy   
- scikit-learn   
- matplotlib   
- seaborn   
- joblib (for model saving/loading)   

Install them via pip:   

pip install pandas numpy scikit-learn matplotlib seaborn joblib     

## Results Comparison and Key Points   
- Random Forest classifier achieved ~85.7% accuracy on the test set, outperforming Gradient Boosting (~79% accuracy).   
- Random Forest showed strong per-class precision and recall, especially for Ponderosa Pine, Cottonwood/Willow, Aspen, Douglas-fir, and Krummholz classes.   
- Gradient Boosting had comparatively lower recall and f1 scores.   
- Confusion matrix analysis revealed Random Forest made fewer overall misclassifications.   

These results highlight Random Forest’s strong performance on high-dimensional ecological data with mixed continuous and categorical variables.   

## Future Implementations   
- Implement K-fold cross-validation to obtain more robust model performance estimates beyond a single train/test split.    
- Increase training epochs and tune hyperparameters (e.g., tree depth, learning rate) using grid search or Bayesian optimization to boost accuracy.   
- Perform feature correlation analysis to remove redundant or highly correlated features, reducing dimensionality and improving model generalization.   
- Experiment with alternative gradient boosting frameworks like XGBoost, LightGBM, or CatBoost for potentially better performance.   
- Develop deployment pipelines including model serialization, API creation, and integration with real-time forest monitoring systems.   
- Explore deep learning approaches leveraging remote sensing imagery for forest cover classification.   

---

