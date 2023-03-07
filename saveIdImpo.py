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

    cursor.execute(f'SELECT * FROM project01.idimpo1 WHERE user="{user}";')
    value1 = cursor.fetchone()

    date = datetime.today().strftime("%Y/%m/%d")

    sql = f'select * from idimpo1 where user IN ("{user}") ORDER BY date desc LIMIT 1'
    cursor.execute(sql)
    idFind=cursor.fetchone()
    # print(idFind)

    sql = f'select * from idimpo1 where date IN ("{date}")'
    cursor.execute(sql)
    dateFind=cursor.fetchone()
    # print(dateFind)

    kcal=0
    carbo=0
    protein=0
    fat=0
    # print(idFind[2])
    # print(dateFind[1])
        
    # if (idFind==None or dateFind==None):
    #     kcal=0
    #     carbo=0
    #     protein=0
    #     fat=0
    #     print('2')
    # if  (user==idFind[0]) and (date==dateFind[1]):
    #     kcal=idFind[2]
    #     carbo=idFind[3]
    #     fat=idFind[4]
    #     protein=idFind[5]
    #     print('1')
    # else:
    #     kcal=0
    #     carbo=0
    #     protein=0
    #     fat=0
    #     print('3')

    for i in range(len(names)):
        foodSL = names[i]
        cursor.execute(f'SELECT * FROM food1 WHERE name="{foodSL}";')
        value2 = cursor.fetchone()
        kcal=value2[2]*int(amounts[i])+kcal
        carbo=value2[3]*int(amounts[i])+carbo
        fat=value2[4]*int(amounts[i])+fat
        protein=value2[5]*int(amounts[i])+protein

    if (idFind==None or dateFind==None):
        # print('4')
        sql = "INSERT idImpo1 SET user=%s, date=%s, kcal=%s, carbo=%s, fat=%s, protein=%s  "
        cursor.execute(sql, (user, date, round(kcal), round(carbo), round(fat), round(protein)))

    elif  (user==idFind[0]) and (date==idFind[1]):
        sql = "UPDATE idImpo1 SET kcal=%s, carbo=%s, fat=%s, protein=%s  WHERE user = %s and date = %s "
        cursor.execute(sql, (round(idFind[2]+kcal), round(idFind[3]+carbo), round(idFind[4]+fat), round(idFind[5]+protein), user, date))
        # print('5')
    
    else :
        sql = "INSERT idImpo1 SET user=%s, date=%s, kcal=%s, carbo=%s, fat=%s, protein=%s  "
        cursor.execute(sql, (user, date, round(kcal), round(carbo), round(fat), round(protein)))
        # print('6')

    sql2 =  f'SELECT * FROM project01.idImpo1 WHERE user="{user}" ORDER BY date desc LIMIT 8; '
    cursor.execute(sql2)
    num1 = cursor.fetchall()
    # print(num1)
    if len(num1)>7:
        sql="DELETE FROM idImpo1 WHERE date = %s"
        cursor.execute(sql,(str(num1[7][0])))

    db.commit()
    db.close()
    return 

# user='T4KulviOqyOHlOFmjQpwfrmCpW32'
# names=["곤드레밥","김치볶음밥"]
# amounts=["2","1"]
# saveIdImpo(user, names,amounts)