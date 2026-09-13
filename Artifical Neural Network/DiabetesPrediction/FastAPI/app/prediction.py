import numpy as np

from model_loader import model, scaler, columns


def predict_diabetes(
    pregnancies,
    glucose,
    blood_pressure,
    skin_thickness,
    insulin,
    bmi,
    diabetes_pedigree_function,
    age
):

    input_data = np.array([[
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        diabetes_pedigree_function,
        age
    ]])

    # Scale input using the same scaler used during training
    input_scaled = scaler.transform(input_data)

    # Make prediction
    prediction_probability = model.predict(input_scaled, verbose=0)[0][0]

    # Convert probability to class
    prediction = 1 if prediction_probability >= 0.5 else 0

    return {
        "prediction": prediction,
        "probability": float(prediction_probability)
    }