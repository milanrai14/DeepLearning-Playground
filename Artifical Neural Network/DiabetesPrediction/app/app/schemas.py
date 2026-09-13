from pydantic import BaseModel

class DibetesRequest(BaseModel): 
    pregnancies: int
    Glucose: int 
    BloodPressure: float
    SkinThickness: int
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int 
    
