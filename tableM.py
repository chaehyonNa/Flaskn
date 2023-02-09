import pymysql

conn = pymysql.connect(host='localhost', user='root',
                        password='cogus123', db='project01', charset='utf8')

cursor = conn.cursor()

sql = ''' CREATE TABLE impo (
    id  int auto_increment PRIMARY KEY,
    date VARCHAR(50),
    kacl FLOAT,
    carbo FLOAT,
    province FLOAT,
    protein FLOAT
)
'''

cursor.execute(sql)

conn.close()