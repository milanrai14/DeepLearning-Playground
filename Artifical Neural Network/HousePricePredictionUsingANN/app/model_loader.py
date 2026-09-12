import joblib
from keras.losses import MeanSquaredError
from keras.models import load_model

# Inside your loader function or at the top level:
model = load_model("model\model_ann.h5", custom_objects={'mse': MeanSquaredError()})
#Load preprocessing objects 
scaler = joblib.load("model/scaler.pkl")
columns = joblib.load("model/colums.plk")