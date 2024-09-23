from flask import Flask, jsonify
from flask_cors import CORS
import os

# Create a Flask application
app = Flask(__name__)

# Enable CORS for all domains on all routes
CORS(app)

# Create an API endpoint for /api/test
@app.route('/api/test', methods=['GET'])
def test_api():
    return jsonify({'message': 'Hello from Flask!'})

# Create a root route to prevent 404 on the main page
@app.route('/')
def home():
    return "Welcome to the Flask App hosted on Azure!"

if __name__ == '__main__':
    # Retrieve the port number from the environment variable or default to 80
    port = int(os.environ.get('PORT', 80))
    # Run the application on all available interfaces
    app.run(host='0.0.0.0', port=port)
