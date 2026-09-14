from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get('/')
def home(): 
    return{
        "message": "House Price Prediction Using the ANN"
    }