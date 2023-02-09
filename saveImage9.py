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

def saveImage9():
    db = pymysql.connect(host="localhost",user="root",password="cogus123",charset="utf8")
    cursor = db.cursor()
    a=[]
    cursor.execute('USE project01;')
    sql2 =  "SELECT id FROM project01.images ORDER BY id desc LIMIT 9; "
    cursor.execute(sql2)
    num = cursor.fetchall()
    for i in num:
        
        cursor.execute(f'SELECT * FROM images WHERE id={i[0]};')
        value1 = cursor.fetchone()
        b = {
                'id': value1[0],
                'image_data': value1[1].decode('utf8'),
                'date': value1[2],
                'time': value1[3],
            }
        a.append(b)
    
    with open('saveImage9.json', 'w', encoding="utf-8") as make_file:
        a=json.dump(a,make_file, ensure_ascii=False,indent="\t")

    # a=json.dumps(a, ensure_ascii=False, indent="\t")

    db.commit()
    db.close()
    return a
saveImage9()