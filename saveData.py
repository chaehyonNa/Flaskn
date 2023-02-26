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

    sql = "INSERT INTO image02 (image_data) VALUES(%s)"
    cursor.execute(sql,(data))
    a=[]
    sql1 =  "SELECT id FROM project01.image02 ORDER BY id desc LIMIT 10; "
    cursor.execute(sql1)
    num1 = cursor.fetchall()
    if len(num1)>9:
        sql="DELETE FROM image02 WHERE id = %s"
        cursor.execute(sql,(str(num1[9][0])))

    db.commit()
    db.close()
    return a

# a_json=open('words01.json',encoding='utf-8')
# a_dict=json.load(a_json)
# # print(a_dict[0]['image_data'])
# data_path=a_dict[0]['image_data']
# saveda(data_path=a_dict[0]['image_data'])