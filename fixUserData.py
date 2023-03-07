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

def fixUserData(id, name, height, weight, kcal, carbo, protein, fat):
    db = pymysql.connect(host="localhost",user="root",password="cogus123",charset="utf8")
    cursor = db.cursor()
    cursor.execute('USE project01;')

    # sql = f'select * from userdata where id IN ("{id}")'
    # cursor.execute(sql)
    # idFind=cursor.fetchone()
    # print(idFind)
    sql = "UPDATE userdata SET height=%s, weight=%s, kacl=%s, carbo=%s, protein=%s, fat=%s  WHERE id =%s "
    cursor.execute(sql,(name, height, weight, kcal, carbo, protein, fat, id))
    a=True

    db.commit()
    db.close()

    return a

# id="skkd"
# name="ss123"
# height=170 
# weight=100 
# kcal=123 
# carbo=2
# protein=2
# fat=2
# fixUserData(id, name, height, weight, kcal, carbo, protein, fat)