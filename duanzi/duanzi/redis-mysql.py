#-*- coding:utf-8 -*-
# datetime:2019/5/24 0024 19:05
# software: PyCharm
import redis
import pymysql
import json


r = redis.Redis(host='10.12.31.42', port=6379,db=0)
conn = pymysql.connect(host='localhost', port=3306,
                               user='root', password='password', db='demo')
cursor = conn.cursor()
while True:
    source, data = r.blpop(['qiushi:items'])
    items = json.loads(data)
    try:
        sql = "insert into duanzi(name, content) values (%s,%s)"
        a = items['name'][0]
        b = items['content'][0]
        b = b.replace('\n','')
        b = b.replace('\r','')
        cursor.execute(sql, (a, b))
        conn.commit()
    except Exception as e:
        print(e)
# conn.close()