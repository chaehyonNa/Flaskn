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


def savesum(names,amounts):
    db = pymysql.connect(host="localhost",user="root",password="cogus123",charset="utf8")
    cursor = db.cursor()
    cursor.execute('USE project01;')
    a=[]
    kacl=0
    carbo=0
    province=0
    protein=0
    for i in range(len(names)):
        foodSL = names[i]
        cursor.execute(f'SELECT * FROM food WHERE name="{foodSL}";')
        value2 = cursor.fetchone()
        kacl=value2[2]*int(amounts[i])+kacl
        carbo=value2[3]*int(amounts[i])+carbo
        province=value2[4]*int(amounts[i])+province
        protein=+value2[5]*int(amounts[i])+protein
        # print(kacl)
        # print(carbo)
        # print(province)
        # print(protein)

    cursor.execute('SELECT * FROM project01.impo1 ORDER BY date desc LIMIT 1;')
    value1 = cursor.fetchone()
    date = datetime.today().strftime("%Y/%m/%d")

    if value1[0]==date:
        sql = "UPDATE impo1 SET kacl=%s, carbo=%s, province=%s, protein=%s  WHERE date =%s "
        cursor.execute(sql, ((value1[1]+kacl), (value1[2]+carbo), (value1[3]+province), (value1[4]+protein), value1[0]))
    elif value1[0]!=date:
        sql = "INSERT INTO impo1 (date, kacl, carbo, province, protein) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql,(date, kacl, carbo, province, protein))

    sql1 =  "SELECT date FROM project01.impo1 ORDER BY date desc LIMIT 7; "
    cursor.execute(sql1)
    num = cursor.fetchall()
    print(num)
    a=[]
    for i in num:
        cursor.execute(f'SELECT * FROM impo1 WHERE date={i[0]};')
        value2 = cursor.fetchone()
        b = {
                'date': value2[0],
                'kacl': value2[1],
                'carbo': value2[2],
                'province': value2[3],
                'protein': value2[4]
            }
        a.append(b)

    with open('words03.json', 'w', encoding="utf-8") as make_file:
        a=json.dump(a,make_file, ensure_ascii=False,indent="\t")

    db.commit()
    db.close()
    return a
    
names=["곤드레밥","김치볶음밥"]
amounts=["2","1"]
savesum(names,amounts)