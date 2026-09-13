from fastapi import FastAPI,  HTTPException

app = FastAPI()

@app.get('/')
def home():
    return{
        "message": "Diabetes Prediction Using Artificial Neural Network (ANN)"
    }