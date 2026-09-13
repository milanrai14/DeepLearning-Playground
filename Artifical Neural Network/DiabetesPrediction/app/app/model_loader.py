import joblib
from tensorflow.keras.models import load_model

model = load_model("..\model\best_ann_model.keras")
scaler = joblib.load("../model/scaler.pkl")
columns = joblib.load("../model/columns.pkl")