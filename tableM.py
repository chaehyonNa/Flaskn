import pymysql

conn = pymysql.connect(host='localhost', user='root',
                        password='cogus123', db='project01', charset='utf8')

cursor = conn.cursor()

sql = ''' CREATE TABLE idimage9 (
    id varchar(50) primary key,
    user varchar(50),
    date varchar(50),
    image_data MEDIUMBLOB
)
'''

cursor.execute(sql)

conn.close()