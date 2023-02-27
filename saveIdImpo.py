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


def saveIdImpo(user, names, amounts):
    db = pymysql.connect(host="localhost",user="root",password="cogus123",charset="utf8")
    cursor = db.cursor()
    cursor.execute('USE project01;')

    cursor.execute(f'SELECT * FROM project01.idimpo WHERE user="{user}";')
    value1 = cursor.fetchone()

    date = datetime.today().strftime("%Y/%m/%d")

    sql = f'select * from idimpo where user IN ("{user}")'
    cursor.execute(sql)
    idFind=cursor.fetchone()
    # print(idFind)

    sql = f'select * from idimpo where date IN ("{date}")'
    cursor.execute(sql)
    dateFind=cursor.fetchone()
    # print(dateFind)

    if  (user==idFind[1]) and (date==dateFind[2]):
        kcal=idFind[3]
        carbo=idFind[4]
        fat=idFind[5]
        protein=idFind[6]
        # print(True)
    else :
        kcal=0
        carbo=0
        protein=0
        fat=0

    for i in range(len(names)):
        foodSL = names[i]
        cursor.execute(f'SELECT * FROM food1 WHERE name="{foodSL}";')
        value2 = cursor.fetchone()
        kcal=value2[2]*int(amounts[i])+kcal
        carbo=value2[3]*int(amounts[i])+carbo
        fat=value2[4]*int(amounts[i])+fat
        protein=value2[5]*int(amounts[i])+protein

    if  (user==idFind[1]) and (date==dateFind[2]):
        sql = "UPDATE idImpo SET kcal=%s, carbo=%s, fat=%s, protein=%s  WHERE user = %s and date = %s "
        cursor.execute(sql, (kcal, carbo, fat, protein, value1[1], value1[2]))
    else :
        sql = "INSERT idImpo SET user=%s, date=%s, kcal=%s, carbo=%s, fat=%s, protein=%s  "
        cursor.execute(sql, (user, date, kcal, carbo, fat, protein))
    

    sql2 =  f'SELECT date FROM project01.idImpo WHERE user="{user}" ORDER BY date desc LIMIT 8; '
    num1 = cursor.fetchall()
    
    if len(num1)>7:
        sql="DELETE FROM idImpo WHERE date = %s"
        cursor.execute(sql,(str(num1[7][0])))

    db.commit()
    db.close()
    return 

# user="dnalsdl"
# names=["곤드레밥","김치볶음밥"]
# amounts=["2","1"]
# saveIdImpo(user, names,amounts)