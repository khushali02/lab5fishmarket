from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__, static_folder='static')


# Load the model
with open('fish_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
@app.route('/predict', methods=['POST'])
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from the request
        data = request.get_json()
        
        # Convert input data to floats
        length1 = float(data.get('length1', 0))
        length2 = float(data.get('length2', 0))
        length3 = float(data.get('length3', 0))
        height = float(data.get('height', 0))
        width = float(data.get('width', 0))
        
        # Debugging statements
        print(f"Input data: Length1={length1}, Length2={length2}, Length3={length3}, Height={height}, Width={width}")
        
        # Make prediction
        prediction = model.predict(np.array([[length1, length2, length3, height, width]]))
        
        # Debugging statement
        print(f"Prediction: {prediction[0]}")
        
        # Return prediction as JSON
        return jsonify({'weight': prediction[0]})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
