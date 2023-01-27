import torch
import pymysql
import json
import pandas as pd
from sqlalchemy import create_engine
from PIL import Image
import base64
from io import BytesIO
from collections import OrderedDict
from datetime import datetime
from koreanLabel import change

#connect
db = pymysql.connect(host="localhost",user="root",password="cogus123",charset="utf8")
cursor = db.cursor()

model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')
# Image
img = 'gons.png'
# Inference
results = model(img)
# Results, change the flowing to: results.show()

lst = str(results).split()[3:-15]

for i in range(len(lst)):
    lst[i] = lst[i].strip(',')
    if(i%2==0):
        if(int(lst[i])>1):
            lst[i+1] = lst[i+1][:-2]
# print(lst)
results.save()
amount = lst[0::2]
names = lst[1::2]
for i in range(len(names)):
    names[i] = change(names[i])
print(names)
a=[]
cursor.execute('USE project01;')

date = datetime.today().strftime("%Y/%m/%d")
time = datetime.today().strftime("%H:%M:%S")
idSL = "19"
cursor.execute(f'SELECT * FROM images02 WHERE id="{idSL}";')
value1 = cursor.fetchone()
b = {
        'id': value1[0],
        'image_data': value1[1].decode('utf8'),
        'date': value1[2],
        'time': value1[3],
    }
a.append(b)

for i in range(len(names)):
    foodSL = names[i]
    cursor.execute(f'SELECT * FROM food1 WHERE name="{foodSL}";')
    value2 = cursor.fetchone()
    c = {
        'name': value2[0],
        'amount': int(amount[i]),
        'kacl': value2[1],
        'carbo': value2[2],
        'province': value2[3],
        'protein': value2[4]
    }
    a.append(c)

with open('words01.json', 'w', encoding="utf-8") as make_file:
    json.dump(a, make_file, ensure_ascii=False, indent="\t")

with open("runs/detect/exp2/gons.jpg", "rb") as image_file:
    binary_image = image_file.read()
binary_image=base64.b64encode(binary_image)
binary_image=binary_image.decode('UTF-8')
sql = "INSERT INTO images02 (image_data, date, time) VALUES(%s,%s,%s)"

cursor.execute(sql,(binary_image, date, time))

sql1 = "SELECT image_data FROM images02 " 
cursor.execute(sql1)
images=cursor.fetchone()

img_strB = images[0]
img = base64.b64decode(img_strB)
im = Image.open(BytesIO(img))
im.show()

db.commit()
db.close()