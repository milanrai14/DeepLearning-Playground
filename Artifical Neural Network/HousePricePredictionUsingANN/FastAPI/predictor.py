from model_loader import model, columns, scaler
import pandas as pd 

def predict_house_price(data):
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
    input_data['ocean_proximity_<1H OCEAN '] = 0


    if data.ocean_proximity == 'INLAND':
        input_data['ocean_proximity_INLAND'] = 1
    elif data.ocean_proximity == 'ISLAND':
        input_data['ocean_proximity_ISLAND'] = 1
    elif data.ocean_proximity == 'NEAR BAY':
        input_data['ocean_proximity_NEAR BAY'] = 1
    elif data.ocean_proximity == 'NEAR OCEAN':
        input_data['ocean_proximity_NEAR OCEAN'] = 1
    elif data.ocean_proximity == "<1H OCEAN":
        input_data['ocean_proximity_<1H OCEAN '] = 1
    else:
        raise ValueError( "Invalid ocean_proximity. " "Use: <1H OCEAN, INLAND, ISLAND, NEAR BAY, NEAR OCEAN" )

    #Convet to dataframe
    input_df = pd.DataFrame([input_data])

    #Arrange the colims in traning order
    input_df = input_df.reindex(
        columns= columns,
        fill_value=0
    )
    #Scale input 
    input_scaled = scaler.tranform(input_df)

    #predict
    prediction = model.predict(
        input_scaled,
        verbose = 0
    )
    return float(prediction[0][0])







