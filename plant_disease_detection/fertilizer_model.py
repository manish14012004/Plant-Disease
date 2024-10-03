import numpy as np
import pandas as pd
from keras.models import load_model

model = load_model('disease_prediction_model.h5')

fertilizer_data = pd.read_csv('fertilizer_info.csv')

disease_name_mapping = {
    "Tomato Bacterial Spot": 0,
    "Tomato Early Blight": 1,
    "Tomato Healthy": 2,
    "Tomato Late Blight": 3,
    "Tomato Septoria Leaf Spot": 4,
    "Tomato Alternaria Canker": 5,
    "Tomato Southern Blight": 6,
    "Tomato Timber Rot": 7,
    "cordana" : 8,
    "healthy" : 9,
    "pestalotiopsis" : 10,
    "sigatoka" : 11
    # Add all other disease names your model handles
}

def preprocess_inputs(prediction, spread_percentage):
    disease_num = disease_name_mapping.get(prediction, -1)
    
    if disease_num == -1:
        raise ValueError(f"Disease name '{prediction}' not recognized.")
    inputs = np.array([[disease_num, spread_percentage]], dtype=np.float32)
    
    return inputs

def predict_fertilizer(prediction, spread_percentage):
    try:
        inputs = preprocess_inputs(prediction, spread_percentage)
        prediction = model.predict(inputs)

        print("Type of model output:", type(prediction))
        print("Contents of model output:", prediction)

        if isinstance(prediction, list):

            prediction = np.array(prediction[0])

        print("Shape of processed model output:", prediction.shape)
        fertilizer_index = np.argmax(prediction)
        
        matching_row = fertilizer_data.iloc[fertilizer_index]
        
        fertilizer_name = matching_row['pesticide_name']
        common_name = matching_row['common_name']
        rei = matching_row['REI']
        phi = matching_row['PHI']
        cause_description = matching_row['what_caused_it']
        
        return fertilizer_name, common_name, rei, phi, cause_description
    
    except ValueError as e:
        # Handle cases where disease name is not recognized
        return "Unknown Fertilizer", "Unknown", "N/A", "N/A", str(e)
    
    except Exception as e:
        # Handle other errors
        return "Unknown Fertilizer", "Unknown", "N/A", "N/A", f"Error: {str(e)}"