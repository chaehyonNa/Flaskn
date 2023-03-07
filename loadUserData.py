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

def loadUserData(id):
    db = pymysql.connect(host="localhost",user="root",password="cogus123",charset="utf8")
    cursor = db.cursor()
    cursor.execute('USE project01;')

    sql = f'select * from userdata where id IN ("{id}")'
    cursor.execute(sql)
    idFind=cursor.fetchone()
    print(idFind)
    b = {
            "name": idFind[1],
            "height": idFind[2],
            "weight": idFind[3],
            "kcal": idFind[4],
            "carbo": idFind[5],
            "province": idFind[6],
            "protein": idFind[7]
    }

    with open('test.json', 'w', encoding="utf-8") as make_file:
        json.dump(b,make_file, ensure_ascii=False,indent="\t")

    db.commit()
    db.close()

# loadUserData('dnals')