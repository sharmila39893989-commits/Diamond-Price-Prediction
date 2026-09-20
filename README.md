# 💎 Diamond Price Prediction

## 📌 Project Description

This project predicts the price of a diamond using Machine Learning Regression.

The model takes diamond characteristics as input and predicts the estimated diamond price.

## 📊 Dataset

The dataset contains information about diamonds.

### Input Features

* Carat
* Cut
* Color
* Clarity
* Depth
* Table
* X
* Y
* Z

### Target

* Price

## 🔍 Data Analysis

The following analysis was performed:

* Dataset shape
* Dataset information
* Statistical summary
* Missing value analysis
* Duplicate value analysis
* Numerical and categorical column analysis
* Price distribution
* Carat vs Price
* Cut vs Price
* Color vs Price
* Clarity vs Price
* Correlation analysis

## 🤖 Machine Learning

Regression algorithms used:

1. Linear Regression
2. Random Forest Regression

## 📈 Model Evaluation

The models are evaluated using:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

## 🌐 Streamlit Application

A Streamlit web application is created for predicting diamond prices.

Users can enter the diamond details and click the **Predict Diamond Price** button to get the estimated price.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Streamlit
* GitHub

## 📁 Project Files

```text
Diamond_Price_Prediction/
│
├── Diamond_Price_Prediction.ipynb
├── diamonds.csv
├── diamond_model.pkl
├── feature_columns.pkl
├── app.py
├── requirements.txt
└── README.md
```

## ▶️ How to Run

### Install Required Libraries

```bash
pip install -r requirements.txt
```

### Run Streamlit Application

```bash
streamlit run app.py
```

## 🎯 Project Goal

The goal of this project is to build a Machine Learning Regression model for diamond price prediction and deploy the model as a Streamlit web application.
