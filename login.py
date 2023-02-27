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

def login(id, passWord):
    db = pymysql.connect(host="localhost",user="root",password="cogus123",charset="utf8")
    cursor = db.cursor()
    cursor.execute('USE project01;')

    sql = f'select * from userdata where id IN ("{id}")'
    cursor.execute(sql)
    idFind=cursor.fetchone()
    print(idFind[0])

    a=False

    if idFind[0]==id:
        if idFind[1==passWord]:
            print(idFind[1]==passWord)
            a=True
        else :
            a=False
    else :
        a=False 

    db.commit()
    db.close()

    return a

id="skkd"
passWord="1232a"
name="ss123"
height=170 
weight=100 
kcal=123 
carbo=1
protein=1 
fat=1
login(id, passWord)