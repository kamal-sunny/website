from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get("name", "")
    return jsonify({"message": f"Hello, {name}! Welcome to your first deployed site!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
