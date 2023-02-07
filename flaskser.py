import argparse
import io
import os
from PIL import Image
import datetime
import saveex
import save9
import savesum
import base64
from io import BytesIO
import json
import jsonify
import torch
from flask import Flask, render_template, request, redirect, send_file
from flask_cors import CORS
from koreanLabel import change

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

DATETIME_FORMAT = "%Y-%m-%d_%H-%M-%S-%f"

@app.route('/')
def web():
    return "main page"

@app.route('/predict', methods=['POST'])
def predict():
   if request.method == "POST":
      # if "file" not in request.files:
      #     return redirect(request.url)
      file = request.files["file"]
      print(file)
      # if not file:
      #     return
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
      # print(names)

      results.render()  # updates results.imgs with boxes and labels
      now_time = datetime.datetime.now().strftime(DATETIME_FORMAT)
      img_savename = f"fla/{now_time}.png"
      Image.fromarray(results.ims[0]).save(img_savename)
      a = saveex.saveex(img_savename,names,amounts)
      # return results
   return send_file("words01.json")
   # return a

@app.route('/save', methods=['POST'])
def save():
   print("hi")
   # file = request.files["file"]
   # print(file)
   jfile = request.get_json()
   # print(jfile)

   image_date1=jfile[0]['image_data']
   print(image_date1)
   # print(jfile['image_data'])
   # a=save.save(img_savename,names,amounts)
   img = base64.b64decode(image_date1)
   im = Image.open(BytesIO(img))
   im.show()

   # Image.open(image_date1)
   return 

# @app.route('/graph', methods=['POST'])
# def gragh():
#    if request.method == "POST":
#       a=savesum.savesum()
#    return send_file("words03.json")

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