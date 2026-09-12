from fastapi import FastAPI, HTTPException
from schema import HouseRequest
from predictor import predict_house_price
app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "House Price Prediction"
    }

#Prediction route 
@app.post("/predict")
def predict(data: HouseRequest): 
    try:
        predicted_price = predict_house_price(data)
        return{
            "Predicted_house_value": predicted_price
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))