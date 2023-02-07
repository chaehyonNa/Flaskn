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

def saveex(img_path,names,amounts):
    db = pymysql.connect(host="localhost",user="root",password="cogus123",charset="utf8")
    cursor = db.cursor()

    img = img_path
    cursor.execute('USE project01;')
    date = datetime.today().strftime("%Y/%m/%d")
    time = datetime.today().strftime("%H:%M:%S")

    with open(img, "rb") as image_file:
        binary_image = image_file.read()
    binary_image=base64.b64encode(binary_image)
    binary_image=binary_image.decode('UTF-8')
    sql = "INSERT INTO images02 (image_data, date, time) VALUES(%s,%s,%s)"
    cursor.execute(sql,(binary_image, date, time))

    a=[]

    cursor.execute('SELECT id FROM project01.images02 ORDER BY id desc LIMIT 1;')
    value1 = cursor.fetchone()
    # print(value1)
    cursor.execute(f'SELECT * FROM images02 WHERE id="{value1[0]}";')
    value1 = cursor.fetchone()
    # print(value1)
    b = {
            'id': value1[0],
            'image_data': value1[1].decode('utf8'),
            'date': value1[2],
            'time': value1[3],
        }
    a.append(b)

    # sql1 = "SELECT image_data FROM images02 " 
    # cursor.execute(sql1)
    # images=cursor.fetchone()
    # img_strB = images[0]
    # img = base64.b64decode(img_strB)
    # im = Image.open(BytesIO(img))
    # im.show()

    db.commit()
    db.close()
    return a
# names=["곤드레밥","김치볶음밥"]
# amounts=["2","1"]
# saveex("runs\detect\exp\gons.jpg",names, amounts)