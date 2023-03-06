from flask import Flask, jsonify, request

from werkzeug.utils import secure_filename
import json

import os

from pdf import extract_text
from ai import process_text, process_description

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


@app.route('/description', methods=['POST'])
def brochure():

    req_body = request.get_json()

    text = req_body.get('description')
    features = req_body.get('features')

    ai_response = process_description(text, features)

    return ai_response

@app.route('/upload', methods=['POST'])
def upload():

    uploaded_file = request.files['brochure']

    text = extract_text(uploaded_file)

    response_text = process_text(text)

    response = json.loads(response_text)

    uploaded_file.save(
        f'uploads/{secure_filename(response.get("address"))}.pdf')

    return response


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
