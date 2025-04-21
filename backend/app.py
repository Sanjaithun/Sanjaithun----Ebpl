from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app) 
model = joblib.load(r"E:\NAAN MUDHALVAN\PROJECT  OCC1\backend\model.pkl")

location_map = {
    'Chennai': 0,
    'Bangalore': 1,
    'Hyderabad': 2,
    'Mumbai': 3
}

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = data['features']

        area = float(features[0])
        bedrooms = int(features[1])
        bathrooms = int(features[2])
        location = location_map.get(features[3], 0)  # default to 0

        input_features = [[area, bedrooms, bathrooms, location]]
        prediction = model.predict(input_features)

        return jsonify({'price': round(prediction[0], 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
