# Import Required Libraries

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

print("=" * 50)
print("Heart Disease Prediction Model")
print("=" * 50)

# -------------------------------
# Load Dataset
# -------------------------------

df = pd.read_csv("heart.csv")

print("\nFirst Five Records:\n")
print(df.head())

# -------------------------------
# Dataset Information
# -------------------------------

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

# -------------------------------
# Numerical Features
# -------------------------------

print("\nNumerical Features:\n")

numerical_features = df.drop("target", axis=1).columns.tolist()

print(numerical_features)

# -------------------------------
# Target Variable
# -------------------------------

print("\nTarget Variable:")

print("target")

# -------------------------------
# Missing Values
# -------------------------------

print("\nMissing Values:\n")

print(df.isnull().sum())

# -------------------------------
# Separate Features and Target
# -------------------------------

X = df.drop("target", axis=1)

y = df["target"]

# -------------------------------
# Train-Test Split
# -------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Samples :", len(X_train))

print("Testing Samples :", len(X_test))

# -------------------------------
# Build Random Forest Model
# -------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# -------------------------------
# Train Model
# -------------------------------

model.fit(X_train, y_train)

# -------------------------------
# Prediction
# -------------------------------

y_pred = model.predict(X_test)

# -------------------------------
# Accuracy
# -------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy : {:.2f}%".format(accuracy * 100))

# -------------------------------
# Save Model
# -------------------------------

joblib.dump(model, "model.pkl")

print("\nModel Saved Successfully!")

print("\nFile Created : model.pkl")