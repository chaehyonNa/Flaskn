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

def upUserData(id, name, height, weight, kcal, carbo, protein, fat):
    db = pymysql.connect(host="localhost",user="root",password="cogus123",charset="utf8")
    cursor = db.cursor()
    cursor.execute('USE project01;')

    sql = f'select * from userdata where id IN ("{id}")'
    cursor.execute(sql)
    idFind=cursor.fetchone()
    print(idFind)
    a=False

    if idFind[0]==id:
        sql = "UPDATE userdata SET name=%s, height=%s, weight=%s, kcal=%s, carbo=%s, protein=%s, fat=%s WHERE id=%s "
        cursor.execute(sql, (name, height, weight, kcal, carbo, protein, fat, id))
        a=True
    else :
        a=False 

    db.commit()
    db.close()
    return a

# id="mg7Ij8aACvP18Utxdkqp7HAIlfo2"
# name="전영우"
# height=170 
# weight=100 
# kcal=123 
# carbo=1
# protein=1 
# fat=1
# upUserData(id, name, height, weight, kcal, carbo, protein, fat)