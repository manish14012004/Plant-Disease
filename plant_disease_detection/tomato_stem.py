import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
from keras.applications.vgg19 import preprocess_input

tomato_stem = load_model('tomato_stem.h5')

ref = {
 0: 'Tomato Alternaria Canker',
 1: 'Tomato Early Blight',
 2: 'Tomato Late Blight',
 3: 'Tomato Southern Blight',
 4: 'Tomato Timber Rot',
 } # Add all your classes here

def tomato_stem_model_and_predict(img_path):
    img = load_img(img_path, target_size=(256, 256))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    
    prediction = tomato_stem.predict(img_array)
    class_idx = np.argmax(prediction)
    probability = np.max(prediction)
    
    return ref[class_idx], probability