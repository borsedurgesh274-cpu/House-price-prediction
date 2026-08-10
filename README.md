🏠 House Price Prediction Dataset

This repository contains the dataset used for the House Price Prediction machine learning project.

📊 Dataset Overview

The dataset contains 5,010 records and 9 columns related to residential property characteristics and house prices.

Columns

Column

Description

Area_sqft

Property area in square feet

Bedrooms

Number of bedrooms

Bathrooms

Number of bathrooms

Age_years

Age of the property in years

Parking_spaces

Number of available parking spaces

Location

Property location

Property_Type

Type of residential property

Furnishing

Furnishing status

Price

House price / target variable

🎯 Machine Learning Target

Target Variable: Price

The dataset can be used to build a regression model that predicts house prices based on property characteristics.

🔧 Recommended Data Science Workflow

Load the CSV dataset using Pandas

Perform data quality checks

Remove duplicate records

Handle missing values

Perform Exploratory Data Analysis (EDA)

Analyze numerical and categorical features

Apply feature preprocessing

Encode categorical variables

Split data into training and testing sets

Train regression models

Evaluate models using MAE, RMSE, and R²

Apply hyperparameter tuning

Save the final model using Joblib

Deploy the model using Streamlit

🤖 Suggested Models

Linear Regression

Random Forest Regressor

XGBoost Regressor

📈 Evaluation Metrics

The following regression metrics can be used:

MAE (Mean Absolute Error)

RMSE (Root Mean Squared Error)

R² Score

🛠️ Technologies

Python

Pandas

NumPy

Matplotlib

Seaborn

Scikit-learn

XGBoost

Joblib

Streamlit

📁 Repository Structure

House-Price-Prediction/
│
├── data/
│   └── house_prices.csv
│
├── model.pkl
├── app.py
├── requirements.txt
└── README.md

🚀 Streamlit Deployment

After creating the trained model.pkl, the Streamlit application can be launched with:

pip install -r requirements.txt
streamlit run app.py

The application allows users to enter property details and receive an estimated house price.

📌 Project Purpose

This dataset is designed for educational and portfolio purposes and demonstrates an end-to-end machine learning workflow from data preprocessing and model training to deployment.

👨‍💻 Author

Durgesh Borse

Data Analytics | Data Science | Machine Learning | Power BI
