import pymysql

conn = pymysql.connect(host='localhost', user='root',
                        password='cogus123', db='project01', charset='utf8')

cursor = conn.cursor()

sql = ''' CREATE TABLE imp (

    date VARCHAR(50) PRIMARY KEY,
    kacl INT
)
'''

cursor.execute(sql)

conn.close()