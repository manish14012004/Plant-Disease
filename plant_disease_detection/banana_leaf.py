import numpy as np
import cv2
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
from keras.applications.vgg19 import preprocess_input

# Load your model
banana_leaf = load_model('banana_leaf.keras')

# Dictionary for class references
ref ={
 0: 'Banana Cordana',
 1: 'Banana Healthy',
 2: 'Banana Pestalotiopsis',
 3: 'Banana Sigatoka',
 } 

# Function to calculate disease spread percentage
def calculate_disease_spread(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Convert to grayscale
    gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

    # Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply binary threshold to segment diseased area
    _, thresholded = cv2.threshold(blurred, 120, 255, cv2.THRESH_BINARY_INV)

    # Calculate total area and diseased area
    total_area = np.size(thresholded)
    diseased_area = np.sum(thresholded == 255)

    # Calculate percentage of diseased area and round it to one decimal place
    disease_spread_percentage = (diseased_area / total_area) * 100

    return round(disease_spread_percentage, 1)

# Function to predict disease and categorize spread percentage
def banana_model_and_predict(img_path):
    # Load and preprocess the image
    img = load_img(img_path, target_size=(256, 256))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    
    # Get the prediction from the model
    prediction = banana_leaf.predict(img_array)
    class_idx = np.argmax(prediction)
    
    # Calculate the disease spread percentage
    spread_percentage = calculate_disease_spread(img_path)
    
    # Categorize the spread percentage
    if 10 <= spread_percentage <= 30:
        category = "Low"
    elif 31 <= spread_percentage <= 60:
        category = "Moderate"
    elif 61 <= spread_percentage <= 90:
        category = "High"
    else:
        category = "Very High"
    
    return ref[class_idx], spread_percentage, category
