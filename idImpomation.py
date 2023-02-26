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


def idImpo(names,amounts):
    db = pymysql.connect(host="localhost",user="root",password="cogus123",charset="utf8")
    cursor = db.cursor()
    cursor.execute('USE project01;')

    kacl=0
    carbo=0
    province=0
    protein=0
    for i in range(len(names)):
        foodSL = names[i]
        cursor.execute(f'SELECT * FROM food1 WHERE name="{foodSL}";')
        value2 = cursor.fetchone()
        kacl=value2[2]*int(amounts[i])+kacl
        carbo=value2[3]*int(amounts[i])+carbo
        province=value2[4]*int(amounts[i])+province
        protein=value2[5]*int(amounts[i])+protein

    date = datetime.today().strftime("%Y/%m/%d")
    user="dnalsdl"

    a='{\n'
    a = a+ f'\t"date:" {date},\n'
    a = a+ f'\t"kacl:" {kacl},\n'
    a = a+ f'\t"carbo:" {carbo},\n'
    a = a+ f'\t"province:" {province},\n'
    a = a+ f'\t"protein:" {protein}\n'
    a = a+ '}'
    print(a)
    strdate=a[11:21]
    sum=1
    cursor.execute(f'SELECT * FROM project01.idimpo01 WHERE id="{user}";')
    value1 = cursor.fetchone()

    if value1==None:
        sql = "INSERT INTO idImpo01 (id,one,sum) VALUES (%s, %s, %s)"
        cursor.execute(sql,(user, a, sum))
    if value1!=None:
        if date==strdate:
            if value1[8]%7==1:
                sql = "UPDATE idImpo01 SET one=%s, sum=%s WHERE id =%s "
                cursor.execute(sql, (a,(value1[8]), value1[0]))
            if value1[8]%7==2:
                sql = "UPDATE idImpo01 SET two=%s, sum=%s WHERE id =%s "
                cursor.execute(sql, (a,(value1[8]), value1[0]))
            if value1[8]%7==3:
                sql = "UPDATE idImpo01 SET three=%s, sum=%s WHERE id =%s "
                cursor.execute(sql, (a,(value1[8]), value1[0]))
            if value1[8]%7==4:
                sql = "UPDATE idImpo01 SET four=%s, sum=%s WHERE id =%s "
                cursor.execute(sql, (a,(value1[8]), value1[0]))
            if value1[8]%7==5:
                sql = "UPDATE idImpo01 SET five=%s, sum=%s WHERE id =%s "
                cursor.execute(sql, (a,(value1[8]), value1[0]))
            if value1[8]%7==6:
                sql = "UPDATE idImpo01 SET six=%s, sum=%s WHERE id =%s "
                cursor.execute(sql, (a,(value1[8]), value1[0]))
            if value1[8]%7==0:
                sql = "UPDATE idImpo01 SET seven=%s, sum=%s WHERE id =%s "
                cursor.execute(sql, (a,(value1[8]), value1[0]))
        else :
            if value1[8]%7==1:
                sql = "UPDATE idImpo01 SET two=%s, sum=%s WHERE id =%s "
                cursor.execute(sql, (a,(value1[8]+1), value1[0]))
            if value1[8]%7==2:
                sql = "UPDATE idImpo01 SET three=%s, sum=%s WHERE id =%s "
                cursor.execute(sql, (a,(value1[8]+1), value1[0]))
            if value1[8]%7==3:
                sql = "UPDATE idImpo01 SET four=%s, sum=%s WHERE id =%s "
                cursor.execute(sql, (a,(value1[8]+1), value1[0]))
            if value1[8]%7==4:
                sql = "UPDATE idImpo01 SET five=%s, sum=%s WHERE id =%s "
                cursor.execute(sql, (a,(value1[8]+1), value1[0]))
            if value1[8]%7==5:
                sql = "UPDATE idImpo01 SET six=%s, sum=%s WHERE id =%s "
                cursor.execute(sql, (a,(value1[8]+1), value1[0]))
            if value1[8]%7==6:
                sql = "UPDATE idImpo01 SET seven=%s, sum=%s WHERE id =%s "
                cursor.execute(sql, (a,(value1[8]+1), value1[0]))
            if value1[8]%7==0:
                sql = "UPDATE idImpo01 SET one=%s, sum=%s WHERE id =%s "
                cursor.execute(sql, (a,(value1[8]+1), value1[0]))

    db.commit()
    db.close()
    return a
    
names=["곤드레밥","김치볶음밥"]
amounts=["2","1"]
idImpo(names,amounts)