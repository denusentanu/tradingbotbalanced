from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Dashboard Active"

@app.route('/status')
def status():
    with open('../log/latest.json') as f:
        data = json.load(f)
    return jsonify(data)