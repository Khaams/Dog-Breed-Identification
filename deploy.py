from flask import Flask, render_template, request, session
import pickle
from keras.models import load_model
import os
import numpy as np
import cv2
from werkzeug.utils import secure_filename
from flask import send_from_directory

app = Flask(__name__)
# load the model
model = load_model('model/CNN_base.h5')
# WSGI Application
# Defining upload folder path
UPLOAD_FOLDER = os.path.join('staticFiles', 'uploads')
# # Define allowed files
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Provide template folder name
# The default folder name should be "templates" else need to mention custom folder name for template path
# The default folder name for staticFiles files should be "staticFiles" else need to mention custom folder for staticFiles path
app = Flask(__name__, static_folder='staticFiles')
# Configure upload folder for Flask application
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = 'This is your secret key to utilize session in Flask'

IMG_SIZE =150
@app.route('/')
def home():
    result = ''
    user_image = os.path.join(app.config['UPLOAD_FOLDER'], 'loading_goat.jpg')
    return render_template('index.html', **locals())


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    uploaded_img = request.files['uploaded-file']
    img_filename = secure_filename(uploaded_img.filename)

    # Upload file to database (defined uploaded folder in staticFiles path)
    uploaded_img.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))

    # Storing uploaded file path in flask session
    session['uploaded_img_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], img_filename)

    # Use the model to guess the breed from image
    img = cv2.imread(os.path.join(app.config['UPLOAD_FOLDER'], img_filename), cv2.IMREAD_COLOR)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    X = np.array(img).reshape(-1, IMG_SIZE, IMG_SIZE, 3)
    result = model.predict(X)

    user_image = os.path.join(app.config['UPLOAD_FOLDER'], img_filename)
    return render_template('index.html', **locals())

@app.route('/show_image')
def displayImage():
    # Retrieving uploaded file path from session
    img_file_path = session.get('uploaded_img_file_path', None)
    # Display image in Flask application web page
    return render_template('show_image.html', user_image=img_file_path)

if __name__ == '__main__':
    app.run(debug=True)