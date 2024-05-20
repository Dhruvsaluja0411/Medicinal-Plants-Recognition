# from flask import Flask, request, render_template
# from predict import predict_plant
# import os

# app = Flask(__name__, template_folder='templates')

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     if request.method == 'POST':
#         # Get the uploaded file
#         file = request.files['file']
#         # Save the file
#         filename = os.path.join('uploads', file.filename)
#         file.save(filename)
#         # Perform prediction
#         plant_name, confidence = predict_plant(filename)
#         return f"Predicted Plant: {plant_name} with confidence: {confidence:.2f}"

# if __name__ == '__main__':
#     app.run(debug=True)

# app.py

from flask import Flask, request, render_template
from predict import predict_plant
from plant_info import get_plant_info
import os

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the uploaded file
        file = request.files['file']
        # Save the file
        filename = os.path.join('uploads', file.filename)
        file.save(filename)
        # Perform prediction
        plant_name, confidence = predict_plant(filename)
        # Get additional plant information
        plant_info = get_plant_info(plant_name)
        return render_template('result.html', plant_name=plant_name, confidence=confidence, plant_info=plant_info)

if __name__ == '__main__':
    app.run(debug=True)
