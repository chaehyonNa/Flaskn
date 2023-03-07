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

def userGraghJson(user):
    db = pymysql.connect(host="localhost",user="root",password="cogus123",charset="utf8")
    cursor = db.cursor()
    cursor.execute('USE project01;')

    sql3= f'SELECT * FROM project01.idImpo1 WHERE user="{user}" ORDER BY date desc LIMIT 7; '
    cursor.execute(sql3)
    num2=cursor.fetchall()
    # print(range(num2))
    a=[]
    num1=7-len(num2)

    for i in range(len(num2)):

        b = {
            'date':num2[i][1],
            'kcal':num2[i][2],
            'carbo':num2[i][3],
            'fat':num2[i][4],
            'protein':num2[i][5]
        }
        a.append(b)
    for i in range(num1):
        b = {
            'date': ' ',
            'kcal':0,
            'carbo':0,
            'fat':0,
            'protein':0
        }
        a.append(b)
    with open('saveUserData.json', 'w', encoding="utf-8") as make_file:
        json.dump(a,make_file, ensure_ascii=False,indent="\t")

    db.commit()
    db.close()
    return 

# user='T4KulviOqyOHlOFmjQpwfrmCpW32'
# userGraghJson(user)