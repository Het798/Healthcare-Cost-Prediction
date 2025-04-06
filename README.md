# 🏥 Healthcare Cost Prediction

This project predicts individual medical charges based on patient information such as age, BMI, smoking status, and region. It uses regression models to understand cost drivers in healthcare.

## 📊 Project Overview

- Performed Exploratory Data Analysis (EDA)
- Engineered and encoded relevant features
- Trained and compared Linear Regression vs XGBoost
- Analyzed prediction errors and feature importance
- Saved final model for reuse

## 📈 Results

| Model              | RMSE       | R² Score |
|--------------------|------------|----------|
| Linear Regression  | $5,796.28  | 0.7836   |
| XGBoost Regressor  | $4,311.38  | 0.8803 ✅ |

## 🧠 Key Features Used
- Age, sex, BMI, number of children
- Smoker (strongest cost driver)
- Region (one-hot encoded)
- Interactions like BMI × smoking status

## 🗂 Project Structure


## 🚀 How to Run

1. Clone the repo  
```bash
git clone https://github.com/yourusername/Healthcare-Cost-Prediction.git
