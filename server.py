# server.py
from flask import Flask, jsonify, request
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model('mnist_model.h5')

# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get image data from request
    image_data = request.json['image']

    # Preprocess image data
    image_array = np.array(image_data).reshape(1, 28, 28, 1) / 255.0

    # Perform prediction
    predictions = model.predict(image_array)

    # Get the predicted label
    predicted_label = np.argmax(predictions)

    # Return the predicted label
    return jsonify({'predicted_label': predicted_label})

if __name__ == '__main__':
    app.run(debug=True)
