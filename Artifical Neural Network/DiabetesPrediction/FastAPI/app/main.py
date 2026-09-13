from fastapi import FastAPI
from schemas import DiabetesRequest
from prediction import predict_diabetes

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Diabetes Prediction Using Artificial Neural Network (ANN)"
    }


@app.post("/predict")
def predict(request: DiabetesRequest):

    result = predict_diabetes(
        pregnancies=request.pregnancies,
        glucose=request.Glucose,
        blood_pressure=request.BloodPressure,
        skin_thickness=request.SkinThickness,
        insulin=request.Insulin,
        bmi=request.BMI,
        diabetes_pedigree_function=request.DiabetesPedigreeFunction,
        age=request.Age
    )

    return result