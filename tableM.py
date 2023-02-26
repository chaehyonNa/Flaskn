import pymysql

conn = pymysql.connect(host='localhost', user='root',
                        password='cogus123', db='project01', charset='utf8')

cursor = conn.cursor()

sql = ''' CREATE TABLE idimpo01 (
    id varchar(50) PRIMARY KEY,
    one varchar(50),
    two varchar(50),
    three varchar(50),
    four varchar(50),
    five varchar(50),
    six varchar(50),
    seven varchar(50),
    sum int
)
'''

cursor.execute(sql)

conn.close()