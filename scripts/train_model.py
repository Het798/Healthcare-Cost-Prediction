# scripts/train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import joblib

# Load data
df = pd.read_csv('../data/insurance.csv')

# Encode categorical features
df = pd.get_dummies(df, columns=['region'], drop_first=True)
df['sex'] = df['sex'].map({'male': 1, 'female': 0})
df['smoker'] = df['smoker'].map({'yes': 1, 'no': 0})

# Split into features and target
X = df.drop('charges', axis=1)
y = df['charges']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=4, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, '../models/xgb_healthcare_model.pkl')
