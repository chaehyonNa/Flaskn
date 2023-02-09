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

def saveData(data_path):
    db = pymysql.connect(host="localhost",user="root",password="cogus123",charset="utf8")
    cursor = db.cursor()
    data = data_path
    cursor.execute('USE project01;')
    date = datetime.today().strftime("%Y/%m/%d")
    time = datetime.today().strftime("%H:%M:%S")

    sql = "INSERT INTO images (image_data, date, time) VALUES(%s,%s,%s)"
    cursor.execute(sql,(data, date, time))

    a=[]

    sql1 =  "SELECT id FROM project01.images ORDER BY id desc LIMIT 10; "
    cursor.execute(sql1)
    num1 = cursor.fetchall()
    if len(num1)>9:
        sql="DELETE FROM images WHERE id = %s"
        cursor.execute(sql,(str(num1[9][0])))

    db.commit()
    db.close()
    return a

# a_json=open('words01.json',encoding='utf-8')
# a_dict=json.load(a_json)
# # print(a_dict[0]['image_data'])
# data_path=a_dict[0]['image_data']
# saveda(data_path=a_dict[0]['image_data'])