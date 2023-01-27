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

def savesum():
    db = pymysql.connect(host="localhost",user="root",password="cogus123",charset="utf8")
    cursor = db.cursor()
    
    a=[]

    cursor.execute('USE project01;')
    cursor.execute('SELECT * FROM project01.imp ORDER BY date desc LIMIT 1;')
    value1 = cursor.fetchone()
    # print(value1[0])
    # cursor.execute(f'SELECT * FROM imp WHERE date="{value1[0]}";')
    # value1 = cursor.fetchone()
    date = datetime.today().strftime("%Y/%m/%d")
    kacl=500
    # print((value1[1]))
    # print(date)

    if value1[0]==date:
        sql = "UPDATE imp SET kacl = %s WHERE date = %s "
        cursor.execute(sql,(kacl,value1[0]))

    elif value1[0]!=date:
        


    # print(value1[2])
    # for i in range(100):
    #     if value1[2].equals(date):
    #         cursor.execute(f'SELECT * FROM food1 WHERE name="{}";')
    #         value2 = cursor.fetchone()

    # sql2 =  "SELECT id FROM project01.images02 ORDER BY id desc LIMIT 9; "
    # cursor.execute(sql2)
    # num = cursor.fetchall()
    # print(num)
    # for i in num:
        
    #     cursor.execute(f'SELECT * FROM images02 WHERE id={i[0]};')
    #     value1 = cursor.fetchone()
    #     b = {
    #             'id': value1[0],
    #             'image_data': value1[1].decode('utf8'),
    #             'date': value1[2],
    #             'time': value1[3],
    #         }
    #     a.append(b)sadasdasdasd
    
    # a=json.dumps(a, ensure_ascii=False, indent="\t")

    db.commit()
    db.close()
    return a
savesum()