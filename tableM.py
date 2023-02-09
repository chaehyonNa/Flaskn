import pymysql

conn = pymysql.connect(host='localhost', user='root',
                        password='cogus123', db='project01', charset='utf8')

cursor = conn.cursor()

sql = ''' CREATE TABLE images (
    id  int auto_increment PRIMARY KEY,
    image_data MEDIUMBLOB ,
    date VARCHAR(50),
    time VARCHAR(50)
)
'''

cursor.execute(sql)

conn.close()