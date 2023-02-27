import argparse
import io
import os
from PIL import Image
import datetime
import saveImageData
import saveImage9
import saveData
import saveSum
import saveIdImpo
import saveImage9
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
   user="dnalsdl"
   jfile = request.get_json()
   print(jfile)
   # names=[]
   # amounts=[]
   # image_data1=jfile[0]['image_data']
   # for i in range(1,len(jfile)):
   #    names.append(jfile[i]['name'])
   #    amounts.append(jfile[i]['amount'])
   # jfile[0]['image_data']

   # saveImage9.saveImage(image_data1, user)

   # # saveData.saveData(image_data1)
   # # saveSum.saveSum(names, amounts)
   return send_file("saveData.json")

@app.route('/loadWeekData', methods=['GET'])
def gragh():
   # if request.method == "GET":
   # saveIdImpo.saveIdImpo(names,amounts,user)
   return send_file("saveData.json")

@app.route('/loadUserData', methods=['GET'])
def loadUserData():

   return jsonify({
      "name": "윤종식",
      "height": 170,
      "weight": 100,
      "kcal": 3000,
      "carbo": 200,
      "province": 200,
      "protein": 200
    })

@app.route('/login', methods=['POST'])
def login():
   if request.method == "POST":
      # file = request.files["login"]
      jfile = request.get_json()
   return jsonify({
      "status" : "success"
    })

@app.route('/loadNineImages', methods=['GET'])
def load9Images():

   # jfile = request.args.to_dict()
   # user=jfile['id']
   # saveImage9.saveImage(user)
   return send_file("saveImage9.json")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask app exposing yolov5 models")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    args = parser.parse_args()
    
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='foodRecog.pt')
    model.eval()
    app.run(host="0.0.0.0", port=5000)  # debug=True causes Restarting with stat