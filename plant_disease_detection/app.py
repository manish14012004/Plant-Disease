from flask import Flask, request, render_template, redirect
from flask import Flask, render_template, make_response
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
import os

from werkzeug.utils import secure_filename
from corn_leaf import corn_model_and_predict
from corn_stem import corn_stem_model_and_predict
from potato_stem import potato_stem_model_and_predict
from tomato_leaf import tomato_model_and_predict
from tomato_stem import tomato_stem_model_and_predict
from pepper_stem import pepper_stem_model_and_predict
from banana_leaf import banana_model_and_predict
from fertilizer_model import predict_fertilizer


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

@app.route('/banana_disease_detection')
def banana_disease_detection():
    return render_template('banana_disease_detection.html')

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
        
        return render_template('result.html', prediction=prediction, probability=probability, image_path=image_path)
    
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
        
        return render_template('result.html', prediction=prediction, probability=probability, image_path=image_path)
    
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
        
        prediction, spread_percentage, category = tomato_model_and_predict(file_path)

        image_path = 'uploads/' + filename
        
        return render_template('result.html', prediction=prediction, spread_percentage=spread_percentage, category=category, image_path=image_path)
    
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

        return render_template('result.html', prediction=prediction, probability=probability, image_path=image_path)
    
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
        
        return render_template('result.html', prediction=prediction, probability=probability, image_path=image_path)
    
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

        return render_template('result.html', prediction=prediction, probability=probability, image_path=image_path)
                                
    return redirect(request.url)

#pepper_leaf detection
@app.route('/pepper_predict', methods=['POST'])
def pepper_predict():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        filename = secure_filename(file.filename)
        file_path = app.config['UPLOAD_FOLDER'] + filename
        file.save(file_path)
        
        prediction, probability = pepper_model_and_predict(file_path)

        image_path = 'uploads/' + filename
        
        return render_template('result.html', prediction=prediction, probability=probability, image_path=image_path)
    
    return redirect(request.url)

#pepper_stem detection
@app.route('/pepper_stem_predict', methods=['POST'])
def pepper_stem_predict():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)
    
    if file:
        filename = secure_filename(file.filename)
        file_path = app.config['UPLOAD_FOLDER'] + filename
        file.save(file_path)

        prediction, probability = pepper_stem_model_and_predict(file_path)

        image_path = 'uploads/' + filename

        return render_template('result.html', prediction=prediction, probability=probability, image_path=image_path)
                                
    return redirect(request.url)

#banana leaf detection
@app.route('/banana_predict', methods=['POST'])
def banana_predict():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        filename = secure_filename(file.filename)
        file_path = app.config['UPLOAD_FOLDER'] + filename
        file.save(file_path)
        
        prediction, spread_percentage, category = banana_model_and_predict(file_path)

        image_path = 'uploads/' + filename
        
        return render_template('result.html', prediction=prediction, spread_percentage=spread_percentage, category=category, image_path=image_path)
    
    return redirect(request.url)

#New route for fertilizer prediction
@app.route('/fertilizer_predict', methods=['POST'])
def fertilizer_predict():
    # Retrieve the disease name and spread percentage from the form
    prediction = request.form['disease_name']
    spread_percentage = request.form['spread_percentage']
  
    # Use the model to predict fertilizer details
    fertilizer_name, common_name, rei, phi, cause_description = predict_fertilizer(prediction, spread_percentage)

    # Render the fertilizer_ml.html template with the prediction results
    return render_template('fertilizer_ml.html', 
                           fertilizer_name=fertilizer_name,
                           common_name=common_name,
                           rei=rei,
                           phi=phi,
                           cause_description=cause_description,
                           prediction=prediction, 
                           spread_percentage=spread_percentage,
                           )



if __name__ == '__main__':
    app.run(debug=True)
