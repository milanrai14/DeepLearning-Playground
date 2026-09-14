# 🩺 Diabetes Prediction API

A **FastAPI backend** for predicting diabetes using a trained **Artificial Neural Network (ANN)** model.

This project is part of an end-to-end Machine Learning/Deep Learning workflow where a trained ANN model is integrated into a REST API using **FastAPI**.

---

## 🚀 Project Overview

The API accepts patient health information and uses a trained ANN model to predict whether the patient is likely to have diabetes.

The model returns:

* **Prediction** — `0` or `1`
* **Probability** — confidence/probability produced by the model

Example response:

```json
{
  "prediction": 1,
  "probability": 0.7253420352935791
}
```

Where:

* `0` → Not Diabetic
* `1` → Diabetic

---

## 🧠 Deep Learning Model

The backend uses an **Artificial Neural Network (ANN)** trained on the Diabetes dataset.

### Input Features

The model expects the following 8 features:

| Feature                    | Description                  |
| -------------------------- | ---------------------------- |
| `pregnancies`              | Number of pregnancies        |
| `Glucose`                  | Plasma glucose concentration |
| `BloodPressure`            | Diastolic blood pressure     |
| `SkinThickness`            | Triceps skin fold thickness  |
| `Insulin`                  | 2-Hour serum insulin         |
| `BMI`                      | Body Mass Index              |
| `DiabetesPedigreeFunction` | Diabetes pedigree function   |
| `Age`                      | Age of the patient           |


---

## 🛠️ Technologies Used

* Python
* TensorFlow
* Keras
* FastAPI
* Uvicorn
* Pydantic
* Scikit-learn
* NumPy
* Joblib
---

## 📚 API Documentation

FastAPI automatically provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can use Swagger UI to test the prediction endpoint directly from your browser.

---

## 🔮 Prediction Endpoint

### POST `/predict`

The endpoint accepts patient information in JSON format.

### Request

```json
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
```

### Response

```json
{
  "prediction": 1,
  "probability": 0.7253420352935791
}
```

---

## 🔄 Prediction Workflow

The backend follows this pipeline:

```text
Client
   │
   ▼
FastAPI
   │
   ▼
Pydantic Validation
   │
   ▼
Input Features
   │
   ▼
Saved Scaler
   │
   ▼
ANN Model (.keras)
   │
   ▼
Prediction
   │
   ▼
Probability
   │
   ▼
JSON Response
```

---

## 📦 Requirements

Example `requirements.txt`:

```text
fastapi
uvicorn
tensorflow
keras
numpy
pandas
scikit-learn
joblib
pydantic
```

For reproducible deployment, it is recommended to pin the versions used during development.

---

## 🧪 Example Test Data

### Higher-risk example

```json
{
  "pregnancies": 6,
  "Glucose": 170,
  "BloodPressure": 80,
  "SkinThickness": 35,
  "Insulin": 200,
  "BMI": 35.0,
  "DiabetesPedigreeFunction": 0.8,
  "Age": 50
}
```

### Lower-risk example

```json
{
  "pregnancies": 1,
  "Glucose": 89,
  "BloodPressure": 66,
  "SkinThickness": 23,
  "Insulin": 94,
  "BMI": 28.1,
  "DiabetesPedigreeFunction": 0.167,
  "Age": 21
}
```

---

## 🎯 Project Goal

The main goal of this project is to understand how a **Deep Learning model can be deployed as a production-style API**.

The workflow covers:

```text
Data
 ↓
Data Preprocessing
 ↓
Train/Test Split
 ↓
Feature Scaling
 ↓
ANN Model
 ↓
Model Evaluation
 ↓
Model Saving
 ↓
FastAPI
 ↓
REST API
 ↓
Prediction
```

---

## 📌 Important Note

This project is intended for **educational and demonstration purposes**.

The prediction produced by the model should not be considered a medical diagnosis. Real medical decisions should be made by qualified healthcare professionals.

---

## 👨‍💻 Author

**Milan Rai**

AI/ML Learner | Python | Machine Learning | Deep Learning | FastAPI
