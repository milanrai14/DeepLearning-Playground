from model_loader import model

def get_house_prediction(data):
    #Create Dictionary
    input_data = {}

    input_data["longitude"] = data.longitude 
    input_data["latitude"] = data.latitude 
    input_data["housing_median_age"] = data.housing_median_age
    input_data["total_rooms"] = data.total_rooms 
    input_data["total_bedrooms"] = data.total_bedrooms 
    input_data["population"] = data.population 
    input_data["households"] = data.households 
    input_data["median_income"] = data.median_income
    input_data['ocean_proximity_INLAND'] = 0
    input_data['ocean_proximity_ISLAND'] = 0
    input_data['ocean_proximity_NEAR BAY'] = 0
    input_data['ocean_proximity_NEAR OCEAN'] = 0
    

