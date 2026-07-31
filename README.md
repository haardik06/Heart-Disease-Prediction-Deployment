# ❤️ Heart Disease Prediction System

An end-to-end Machine Learning project that predicts the likelihood of heart disease using patient clinical parameters. The application is built with **Flask**, uses a **Random Forest Classifier** for prediction, exposes a **REST API**, and is ready for deployment on **Render**.

---

# 📌 Objective

The objective of this project is to develop and deploy a Machine Learning model capable of predicting whether a patient is at risk of heart disease based on various medical attributes. The project demonstrates the complete deployment pipeline, including model training, model serialization, Flask API development, GitHub version control, and cloud deployment using Render.

---

# 📂 Project Structure

```
HeartDiseaseDeployment/
│
├── app.py
├── train_model.py
├── heart.csv
├── model.pkl
├── requirements.txt
├── README.md
├── Procfile
├── runtime.txt
├── .gitignore
│
└── templates/
    └── index.html
```

---

# 📊 Dataset

**Heart Disease Dataset**

Source:

https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset

The dataset contains patient health information including:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Rest ECG
- Maximum Heart Rate
- Exercise Induced Angina
- Old Peak
- Slope
- Number of Major Vessels (CA)
- Thal
- Target (Heart Disease)

---

# 🛠 Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Joblib
- HTML
- CSS
- Git
- GitHub
- Render

---

# 🤖 Machine Learning Model

**Algorithm Used**

- Random Forest Classifier

**Train-Test Split**

- Training Data: 80%
- Testing Data: 20%

**Evaluation Metric**

- Accuracy Score

The trained model is serialized using **Joblib** and stored as:

```
model.pkl
```

---

# 🌐 Flask REST API

## Home Route

```
GET /
```

Displays the Heart Disease Prediction web application.

---

## Prediction Route

```
POST /predict
```

### Sample Request

```json
{
  "age": 63,
  "sex": 1,
  "cp": 3,
  "trestbps": 145,
  "chol": 233,
  "fbs": 1,
  "restecg": 0,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 2.3,
  "slope": 0,
  "ca": 0,
  "thal": 1
}
```

### Sample Response

```json
{
  "prediction": "Heart Disease Detected",
  "confidence": 97
}
```

---

# ✨ Features

- Heart Disease Prediction using Machine Learning
- Random Forest Classification Model
- Interactive and Responsive Web Interface
- Flask REST API
- Confidence Score Display
- Error Handling
- Ready for Cloud Deployment
- GitHub Version Control

---

# 🚀 How to Run Locally

## Clone Repository

```bash
git clone https://github.com/haardik06/Heart-Disease-Prediction-Deployment.git
```

## Move into Project Directory

```bash
cd Heart-Disease-Prediction-Deployment
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Train the Model

```bash
python train_model.py
```

## Start the Flask Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

# 📷 Application Workflow

1. User enters patient health details.
2. Flask receives the input.
3. The trained Random Forest model predicts the result.
4. The prediction and confidence score are displayed on the web page.
5. The same prediction can also be accessed through the REST API.

---

# 📦 GitHub Repository

Repository Link:

**https://github.com/haardik06/Heart-Disease-Prediction-Deployment**

---

# ☁️ Render Deployment

Live Application:

**Add your Render deployment URL here after deployment**

Example:

```
https://your-app-name.onrender.com
```

---

# 📈 Results

The application successfully predicts the likelihood of heart disease using patient clinical parameters. The trained Random Forest model provides predictions through both a user-friendly web interface and a REST API. The project demonstrates an end-to-end machine learning deployment workflow from model training to cloud deployment.

---

# 🎯 Conclusion

This project demonstrates the complete lifecycle of a Machine Learning deployment using Flask. It covers data preprocessing, model training, model serialization, REST API development, GitHub version control, and cloud deployment using Render. The application provides an intuitive interface along with an API for heart disease prediction, making it suitable as a practical machine learning deployment project.

---

# 👨‍💻 Author

**Hardik Verma**

GitHub:

https://github.com/haardik06