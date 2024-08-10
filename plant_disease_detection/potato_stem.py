import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
from keras.applications.vgg19 import preprocess_input

potato_stem = load_model('potato_stem.keras')

ref = {
 0: 'potato_sclerotinia_timber_rot',
 1: 'potato_phytophthora infestans',
 2: 'potato_rhizoctonia',
 } # Add all your classes here

def potato_stem_model_and_predict(img_path):
    img = load_img(img_path, target_size=(256, 256))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    
    prediction = potato_stem.predict(img_array)
    class_idx = np.argmax(prediction)
    probability = np.max(prediction)
    
    return ref[class_idx], probability