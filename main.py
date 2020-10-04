from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def key():
    message = 'Hello World'
    obj = jsonify(response = message)
    return obj

if __name__ == '__main__':
    app.run(port=5000)

