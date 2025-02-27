from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load your trained ML model
model = 'Crop_Yield_model3.pkl'
with open(model, 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the form
    data = request.json
    features = [
        float(data['rainfall']),
        float(data['soil_quality']),
        float(data['farm_size']),
        float(data['sunlight']),
        float(data['fertilizer'])
    ]

    # Predict using the model
    prediction = model.predict([features])
    output = round(prediction[0], 2)

    return jsonify({'prediction': output})

if __name__ == '__main__':
    app.run(debug=True)