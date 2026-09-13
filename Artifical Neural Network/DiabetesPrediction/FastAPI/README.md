🩺 Diabetes Prediction API

A FastAPI backend for predicting diabetes using a trained Artificial Neural Network (ANN) model.

This project is part of an end-to-end Machine Learning/Deep Learning workflow where a trained ANN model is integrated into a REST API using FastAPI.

🚀 Project Overview

The API accepts patient health information and uses a trained ANN model to predict whether the patient is likely to have diabetes.

The model returns:

Prediction — 0 or 1
Probability — confidence/probability produced by the model

Example response:

{
  "prediction": 1,
  "probability": 0.7253420352935791
}

Where:

0 → Not Diabetic
1 → Diabetic
🧠 Machine Learning Model

The backend uses an Artificial Neural Network (ANN) trained on the Diabetes dataset.

Input Features

The model expects the following 8 features:

Feature	Description
pregnancies	Number of pregnancies
Glucose	Plasma glucose concentration
BloodPressure	Diastolic blood pressure
SkinThickness	Triceps skin fold thickness
Insulin	2-Hour serum insulin
BMI	Body Mass Index
DiabetesPedigreeFunction	Diabetes pedigree function
Age	Age of the patient
📁 Project Structure
DiabetesPrediction/
│
├── FastAPI/
│   │
│   ├── app/
│   │   ├── main.py
│   │   ├── schemas.py
│   │   ├── model_loader.py
│   │   ├── recommender.py
│   │   └── model/
│   │       ├── best_ann_model.keras
│   │       ├── scaler.pkl
│   │       └── columns.pkl
│   │
│   ├── requirements.txt
│   └── venv/
│
└── README.md

Adjust the filenames if your actual project uses different module names.

🛠️ Technologies Used
Python
TensorFlow
Keras
FastAPI
Uvicorn
Pydantic
Scikit-learn
NumPy
Joblib

🔮 Prediction Endpoint
POST /predict

The endpoint accepts patient information in JSON format.

Request
{
  "pregnancies": 6,
  "Glucose": 148,
  "BloodPressure": 72,
  "SkinThickness": 35,
  "Insulin": 169.5,
  "BMI": 33.6,
  "DiabetesPedigreeFunction": 0.627,
  "Age": 50
}
Response
{
  "prediction": 1,
  "probability": 0.7253420352935791
}