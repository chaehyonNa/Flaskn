import torch
import pymysql
import json
from flask import jsonify
import pandas as pd
from sqlalchemy import create_engine
from PIL import Image
import base64
from io import BytesIO
from collections import OrderedDict
from datetime import datetime
from koreanLabel import change


def saveImage(user, image_data1):
    db = pymysql.connect(host="localhost",user="root",password="cogus123",charset="utf8")
    cursor = db.cursor()
    cursor.execute('USE project01;')
    a=[]
    date = datetime.today().strftime("%Y/%m/%d_%H:%M:%S")
    
    sql = "INSERT idImage901 SET user=%s, date=%s, image_data=%s"
    cursor.execute(sql, (user, date, image_data1))

    sql2 =  f'SELECT date FROM project01.idImage901 WHERE user="{user}" ORDER BY date desc LIMIT 10; '
    cursor.execute(sql2)
    num1 = cursor.fetchall()
    
    if len(num1)>9:
        sql="DELETE FROM idImage901 WHERE date = %s"
        cursor.execute(sql,(str(num1[9][0])))

    db.commit()
    db.close()
    return a

def loadImage(user):
    db = pymysql.connect(host="localhost",user="root",password="cogus123",charset="utf8")
    cursor = db.cursor()
    cursor.execute('USE project01;')
    a=[]

    sql2 =  f'SELECT image_data FROM project01.idImage901 WHERE user="{user}" ORDER BY date desc LIMIT 9 ; '
    cursor.execute(sql2)
    images = list(cursor.fetchall())
    num1=9-len(images)
    # print(images[8])
    for i in images:
        b = {

                'image_data': i[0].decode('utf8')
                
            }
        a.append(b)
    for i in range(num1):
        b = {

                'image_data': ' '
                
            }
        a.append(b)
    with open('saveImage9.json', 'w', encoding="utf-8") as make_file:
        a=json.dump(a,make_file, ensure_ascii=False)
    
    db.commit()
    db.close()
    return a

# user='79ncTrk3AqWhsoUX6YAP87KiZp53'
# a_json=open('saveImageData.json',encoding='utf-8')
# a_dict=json.load(a_json)
# # print(a_dict[7]["image_data"])
# image_data1=a_dict[0]['image_data']
# saveImage(user, image_data1)
# loadImage(user)