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

    cursor.execute('SELECT * FROM project01.impo01 ORDER BY date desc LIMIT 1;')
    value1 = cursor.fetchone()
    date = datetime.today().strftime("%Y/%m/%d")

    if value1[1]==date:
        sql = "UPDATE impo01 SET kacl=%s, carbo=%s, province=%s, protein=%s  WHERE date =%s "
        cursor.execute(sql, ((value1[2]+kacl), (value1[3]+carbo), (value1[4]+province), (value1[5]+protein), value1[1]))
    elif value1[1]!=date:
        sql = "INSERT INTO impo01 (date, kacl, carbo, province, protein) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql,(date, kacl, carbo, province, protein))

    sql1 =  "SELECT id FROM project01.impo01 ORDER BY id desc LIMIT 7; "
    cursor.execute(sql1)
    num = cursor.fetchall()
    a=[]

    for i in num:
        cursor.execute(f'SELECT * FROM impo01 WHERE id={i[0]};')
        value2 = cursor.fetchone()
        b = {
                'date': value2[1],
                'kacl': value2[2],
                'carbo': value2[3],
                'province': value2[4],
                'protein': value2[5]
            }
        a.append(b)

    with open('savefoodim.json', 'w', encoding="utf-8") as make_file:
        a=json.dump(a,make_file, ensure_ascii=False,indent="\t")
    
    sql2 =  "SELECT id FROM project01.impo01 ORDER BY id desc LIMIT 8; "
    cursor.execute(sql2)
    num1 = cursor.fetchall()
    
    if len(num1)>7:
        sql="DELETE FROM impo01 WHERE id = %s"
        cursor.execute(sql,(str(num1[7][0])))

    db.commit()
    db.close()
    return a
    
# names=["곤드레밥","김치볶음밥"]
# amounts=["2","1"]
# savesum(names,amounts)