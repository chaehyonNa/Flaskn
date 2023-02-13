import pymysql

conn = pymysql.connect(host='localhost', user='root',
                        password='cogus123', db='project01', charset='utf8')

cursor = conn.cursor()

sql = ''' CREATE TABLE image02 (
    id  int auto_increment PRIMARY KEY,
    image_data MEDIUMBLOB
)
'''

cursor.execute(sql)

conn.close()