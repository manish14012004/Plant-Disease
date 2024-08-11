import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
from keras.applications.vgg19 import preprocess_input

corn_leaf = load_model('corn_leaf.h5')

ref = {
 0: 'Corn Cercospora Leaf Spot',
 1: 'Corn Common Rust',
 2: 'Corn Northern Leaf Blight',
 3: 'Corn Healthy',
 } # Add all your classes here

def corn_model_and_predict(img_path):
    img = load_img(img_path, target_size=(256, 256))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    
    prediction = corn_leaf.predict(img_array)
    class_idx = np.argmax(prediction)
    probability = np.max(prediction)
    
    return ref[class_idx], probability