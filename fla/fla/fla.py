import argparse
import io
import os
from PIL import Image
import datetime
import torch
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

DATETIME_FORMAT = "%Y-%m-%d_%H-%M-%S-%f"

@app.route('/')
def web():
    return "main page"

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        print(file)
        if not file:
            return

        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes))
        results = model(img)
        print(results)
        
        results.render()  # updates results.imgs with boxes and labels
        now_time = datetime.datetime.now().strftime(DATETIME_FORMAT)
        img_savename = f"fla/static/{now_time}.png"
        Image.fromarray(results.ims[0]).save(img_savename)
        # return results
        print(img_savename[3:])

    # return render_template("index.html")
    return img_savename[3:]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask app exposing yolov5 models")
    parser.add_argument("--port", default=8081, type=int, help="port number")
    args = parser.parse_args()
    

    model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')
    # model = torch.hub.load('ultralytics/yolov5', 'custom', path='runs/train/gon_yolov5s_results8/weights/best.pt')
    model.eval()
    app.run(host="0.0.0.0", port=8081)  # debug=True causes Restarting with stat