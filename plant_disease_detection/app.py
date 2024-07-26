from flask import Flask, request, render_template, redirect

import os
from werkzeug.utils import secure_filename
from corn_leaf import corn_model_and_predict


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/plant_selection_page')
def plant_selection_page():
    return render_template('plant_selection_page.html')

@app.route('/cultivation_tips')
def cultivation_tips():
    return render_template('cultivation_tips.html')

@app.route('/fertilizer')
def fertilizer():
    return render_template('fertilizer.html')

@app.route('/tomato_disease_detection')
def tomato_disease_detection():
    return render_template('tomato_disease_detection.html')

@app.route('/potato_disease_detection')
def potato_disease_detection():
    return render_template('potato_disease_detection.html')

@app.route('/corn_disease_detection')
def corn_disease_detection():
    return render_template('corn_disease_detection.html')

@app.route('/pepper_disease_detection')
def pepper_disease_detection():
    return render_template('pepper_disease_detection.html')




#corn detection
@app.route('/corn_predict', methods=['POST'])
def corn_predict():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        prediction, probability = corn_model_and_predict(file_path)
        
        return render_template('corn_result.html', prediction=prediction, probability=probability, image_path=file_path)
    
    return redirect(request.url)


if __name__ == '__main__':
    app.run(debug=True)
