from tensorflow.keras.models import load_model
import joblib

#load ANN model 
model = load_model("model\model_ann.h5")

#Load preprocessing objects 
scaler = joblib.load("model/scaler.pkl")
columns = joblib.load("model/colums.plk")