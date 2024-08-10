from flask import Flask, request, render_template, redirect
from flask import send_from_directory
import os
from werkzeug.utils import secure_filename
from corn_leaf import corn_model_and_predict
from corn_stem import corn_stem_model_and_predict
from potato_stem import potato_stem_model_and_predict
from tomato_leaf import tomato_model_and_predict
from tomato_stem import tomato_stem_model_and_predict

from potato_stem import potato_stem_model_and_predict

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
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

@app.route('/learn_more')
def learn_more_page():
    return render_template('learn_more.html')



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
        file_path = app.config['UPLOAD_FOLDER'] + filename
        file.save(file_path)
        
        prediction, probability = corn_model_and_predict(file_path)

        image_path = 'uploads/' + filename
        
        return render_template('corn_result.html', prediction=prediction, probability=probability, image_path=image_path)
    
    return redirect(request.url)

#corn stem detection

@app.route('/corn_stem_predict', methods=['POST'])
def corn_stem_predict():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        filename = secure_filename(file.filename)
        file_path = app.config['UPLOAD_FOLDER'] + filename
        file.save(file_path)
        
        prediction, probability = corn_stem_model_and_predict(file_path)

        image_path = 'uploads/' + filename
        
        return render_template('corn_result.html', prediction=prediction, probability=probability, image_path=image_path)
    
    return redirect(request.url)
 



#tomato detection
@app.route('/tomato_predict', methods=['POST'])
def tomato_predict():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        filename = secure_filename(file.filename)
        file_path = app.config['UPLOAD_FOLDER'] + filename
        file.save(file_path)
        
        prediction, probability = tomato_model_and_predict(file_path)

        image_path = 'uploads/' + filename
        
        return render_template('tomato_result.html', prediction=prediction, probability=probability, image_path=image_path)
    
    return redirect(request.url)

#tomato stem detection

@app.route('/tomato_stem_predict', methods=['POST'])
def tomato_stem_predict():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)
    
    if file:
        filename = secure_filename(file.filename)
        file_path = app.config['UPLOAD_FOLDER'] + filename
        file.save(file_path)

        prediction, probability = tomato_stem_model_and_predict(file_path)

        image_path = 'uploads/' + filename

        return render_template('tomato_result.html', prediction=prediction, probability=probability, image_path=image_path)
    
    return redirect(request.url)

#potato detection
@app.route('/potato_predict', methods=['POST'])
def potato_predict():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        filename = secure_filename(file.filename)
        file_path = app.config['UPLOAD_FOLDER'] + filename
        file.save(file_path)
        
        prediction, probability = potato_model_and_predict(file_path)

        image_path = 'uploads/' + filename
        
        return render_template('potato_result.html', prediction=prediction, probability=probability, image_path=image_path)
    
    return redirect(request.url)

#potato_stem detection
@app.route('/potato_stem_predict', methods=['POST'])
def potato_stem_predict():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)
    
    if file:
        filename = secure_filename(file.filename)
        file_path = app.config['UPLOAD_FOLDER'] + filename
        file.save(file_path)

        prediction, probability = potato_stem_model_and_predict(file_path)

        image_path = 'uploads/' + filename

        return render_template('potato_result.html', prediction=prediction, probability=probability, image_path=image_path)
                                #above html page to be changed
    return redirect(request.url)



if __name__ == '__main__':
    app.run(debug=True)
