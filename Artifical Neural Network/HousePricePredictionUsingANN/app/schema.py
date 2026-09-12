from pydantic import BaseModel
from typing import Literal
class HouseRequest(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: float
    total_rooms: float
    total_bedrooms: float
    population: float
    households: float
    median_income: float 
    ocean_proximity: str