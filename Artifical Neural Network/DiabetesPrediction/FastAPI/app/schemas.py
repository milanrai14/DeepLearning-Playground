from pydantic import BaseModel

class DiabetesRequest(BaseModel): 
    pregnancies: int
    Glucose: int 
    BloodPressure: float
    SkinThickness: int
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int 

