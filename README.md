# Diamonds-Price-Prediction

### This project leverages machine learning to predict diamond prices based on various features such as carat, cut, clarity, color. The goal is to develop a highly accurate model using multiple techniques and provide a user-friendly interface for predictions.

![diamond_predict](https://github.com/user-attachments/assets/5d180755-b82f-4d18-9ed4-5df903e589d3)

# Project Workflow

### Data Preprocessing

  Clean the dataset by handling missing values, removing outliers, and normalizing features. </br>
  Feature engineering includes encoding categorical variables (e.g., cut, clarity) and scaling numeric ones (e.g., carat). </br>

### Exploratory Data Analysis (EDA)

  Visualize data distributions and correlations between features using libraries like Matplotlib and Seaborn. </br>
  Key insights include relationships between carat and price, cut and price. </br> 
  Outlier detection is implemented to improve model accuracy. </br>

### Model Selection:

  Several machine learning models are implemented </br>
  Linear Regression: Provides a baseline model using simple linear relationships between features and price. </br>
  Decision Tree Regressor: Captures non-linear relationships between features. </br>
  Random Forest Regressor: An ensemble method that improves prediction performance by averaging multiple decision trees. </br>
  XGBoost: Optimized gradient boosting algorithm used for further refinement. </br>


### Evaluation & Model Tuning

  Models are evaluated using metrics like Root Mean Square Error (RMSE) and R² scores. </br>
  Hyperparameter tuning and cross-validation are applied to optimize model performance.

### Deployment

  A web application built with Flask allows users to input diamond characteristics and get instant price predictions. </br>
  Deployed using a simple UI to facilitate easy interaction with the trained machine learning models.

### Tools & Technologies
  Programming Language : Python </br>
  Libraries : Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, XGBoost, Flask </br>
  Deployment : Flask for web app, HTML/CSS for frontend </br>
