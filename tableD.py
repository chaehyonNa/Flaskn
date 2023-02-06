import pymysql

conn = pymysql.connect(host='localhost', user='root',
                        password='cogus123', db='project01', charset='utf8')

sql = "DROP TABLE IF EXISTS impo01"

with conn:
    with conn.cursor() as cur:
        cur.execute(sql)
    conn.commit()