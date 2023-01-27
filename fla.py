import argparse
import io
import os
from PIL import Image
import datetime
import save9
import saveex
import json
import jsonify
import torch
from flask import Flask, render_template, request, redirect, send_file
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

DATETIME_FORMAT = "%Y-%m-%d_%H-%M-%S-%f"

@app.route('/')
def web():
    return "main page"

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == "POST":
        b=saveex.saveex()
    return b

@app.route('/recent', methods=['POST'])
def recent():
   if request.method == "POST":
      a=save9.save9()
   return a


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask app exposing yolov5 models")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    args = parser.parse_args()
    
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')
    model.eval()
    app.run(host="0.0.0.0", port=5000)  # debug=True causes Restarting with stat