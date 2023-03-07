import argparse
import io
import os
from PIL import Image
import datetime
import saveImageData
import saveImage9
import loadUserData
import userGraghJson
import persentData
import upUserData
import saveSum
import saveIdImpo
import saveImage9
import join
import base64
from io import BytesIO
import json
import torch
from flask import Flask, render_template, request, redirect, send_file, jsonify
from flask_cors import CORS
from koreanLabel import change

app = Flask(__name__)
# cors = CORS(app, resources={r"/*": {"origins": "*"}})
CORS(app)
DATETIME_FORMAT = "%Y-%m-%d_%H-%M-%S-%f"

@app.route('/')
def web():
   return "main page"

@app.route('/predict', methods=['POST'])
def predict():
   if request.method == "POST":
      file = request.files["file"]
      img_bytes = file.read()
      img = Image.open(io.BytesIO(img_bytes))
      results = model(img)
        
      lst = str(results).split()[3:-15]

      for i in range(len(lst)):
         lst[i] = lst[i].strip(',')
         if(i%2==0):
            if(int(lst[i])>1):
               lst[i+1] = lst[i+1][:-2]
      amounts = lst[0::2]
      names = lst[1::2]
      for i in range(len(names)):
         names[i] = change(names[i])

      results.render()  # updates results.imgs with boxes and labels
      now_time = datetime.datetime.now().strftime(DATETIME_FORMAT)
      img_savename = f"fla/{now_time}.png"
      Image.fromarray(results.ims[0]).save(img_savename)
      saveImageData.saveImageData(img_savename,names,amounts)
   return send_file("saveImageData.json")

@app.route('/save', methods=['POST'])
def save():
   jfile = request.get_json()
   user=request.args.to_dict()['id']
   names=[]
   amounts=[]
   image_data1=jfile['image_data']

   for i in range(0,len(jfile['foodData'])):
      names.append(jfile['foodData'][i]['name'])
      amounts.append(jfile['foodData'][i]['amount'])

   # saveData.saveData(image_data1)
   # saveSum.saveSum(names, amounts)
   saveImage9.saveImage(user, image_data1)
   saveIdImpo.saveIdImpo(user, names, amounts)
   return 'True'

@app.route('/weekData2/<id>', methods=['GET'])
def gragh(id):
   if request.method == "GET":
      userGraghJson.userGraghJson(id)
      return send_file("saveUserData.json")
   
@app.route('/persentData/<id>', methods=['GET'])
def persent(id):
   if request.method == "GET":
      persentData.persentData(id)
      return send_file("persentData.json")


@app.route('/load9Images/<id>', methods=['GET'])
def load9Images(id):
   if request.method == "GET":
      saveImage9.loadImage(id)
      return send_file("saveImage9.json")

@app.route('/userData2/<id>', methods=['GET'])
def UserData(id):
   if request.method == "GET":
      loadUserData.loadUserData(id)
      return send_file("test.json")
   
@app.route('/updateUserData/<id>', methods=['POST'])
def updateUserData(id):
   if request.method == "POST":
      jfile = request.get_json()
      id=jfile['id']
      name=jfile['name']
      height=jfile['height']
      weight=jfile['weight']
      kcal=jfile['kcal']
      carbo=jfile['carbo']
      protein=jfile['protein']
      fat=jfile['fat']
      a=upUserData.upUserData(id, name, height, weight, kcal, carbo, protein, fat)
      return jsonify({
         "status" : a
      })

@app.route('/join', methods=['POST'])
def join1():
   if request.method == "POST":
      jfile = request.get_json()
      id=jfile['id']
      name=jfile['name']
      height=jfile['height']
      weight=jfile['weight']
      kcal=jfile['kcal']
      carbo=jfile['carbo']
      protein=jfile['protein']
      fat=jfile['fat']
      a=join.join(id, name, height, weight, kcal, carbo, protein, fat)
      return jsonify({
         "status" : a
      })

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask app exposing yolov5 models")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    args = parser.parse_args()
    
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='foodRecog.pt')
    model.eval()
    app.run(host="0.0.0.0", port=5000)  # debug=True causes Restarting with stat