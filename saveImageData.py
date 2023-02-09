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

def saveImageData(img_path,names,amounts):
    db = pymysql.connect(host="localhost",user="root",password="cogus123",charset="utf8")
    cursor = db.cursor()

    img = img_path
    cursor.execute('USE project01;')

    with open(img, "rb") as image_file:
        binary_image = image_file.read()
    binary_image=base64.b64encode(binary_image)
    binary_image=binary_image.decode('UTF-8')

    a=[]
    b = {
            'image_data': binary_image,
        }
    a.append(b)
    for i in range(len(names)):
        foodSL = names[i]
        cursor.execute(f'SELECT * FROM food WHERE name="{foodSL}";')
        value2 = cursor.fetchone()
        c = {
            'id': value2[0],
            'name': value2[1],
            'amount': int(amounts[i]),
            'kacl': value2[2],
            'carbo': value2[3],
            'province': value2[4],
            'protein': value2[5]
        }
        a.append(c)
    with open('saveImageData.json', 'w', encoding="utf-8") as make_file:
        a=json.dump(a,make_file, ensure_ascii=False)

    db.commit()
    db.close()
    return a
# names=["곤드레밥","김치볶음밥"]
# amounts=["2","1"]
# saveex("runs\detect\exp\gons.jpg",names, amounts)