import pymysql

conn = pymysql.connect(host='localhost', user='root',
                        password='cogus123', db='project01', charset='utf8')

cursor = conn.cursor()

sql = ''' CREATE TABLE idimage901 (

    user varchar(50),
    date varchar(50),
    image_data longblob

)
'''

cursor.execute(sql)

conn.close()