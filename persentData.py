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

def persentData(user):
    db = pymysql.connect(host="localhost",user="root",password="cogus123",charset="utf8")
    cursor = db.cursor()
    cursor.execute('USE project01;')

    sql1= f'SELECT * FROM userdata WHERE id="{user}"; '
    cursor.execute(sql1)
    num1=cursor.fetchone()
    # print(num1)

    sql2= f'SELECT * FROM idimpo1 WHERE user="{user}" ORDER BY date desc LIMIT 1; '
    cursor.execute(sql2)
    num2=cursor.fetchone()
    # print(num2)
        
    date = datetime.today().strftime("%Y/%m/%d")
    if num2[1]==date:
        kcal=((num2[2]/num1[4]))
        carbo=((num2[3]/num1[5]))
        fat=((num2[4]/num1[6]))
        protein=((num2[5]/num1[7]))
        # print(kcal)
        # print(carbo)
        # print(fat)
        # print(protein)
    else :
        kcal=0
        carbo=0
        fat=0
        protein=0

    a = [
        {
        "1":kcal,
        "2":carbo,
        "3":fat,
        "4":protein
        }
    ]
    with open('persentData.json', 'w', encoding="utf-8") as make_file:
        json.dump(a,make_file, ensure_ascii=False,indent="\t")

    db.commit()
    db.close()
    return 

# user='LumSbg5GKRUGvMmtkyZCCBR40ZW2'
# persentData(user)