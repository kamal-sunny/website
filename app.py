from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

# Serve the HTML file
@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get("name", "")
    return jsonify({"message": f"Hello, {name}! Welcome to your first deployed site!"})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
