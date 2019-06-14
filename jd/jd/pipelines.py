# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class JdPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host='localhost', port=3306,
                               user='root', password='password', db='jd')
        cursor = conn.cursor()
        goodsid = item['goodsid']
        title = item['title']
        goodslink = item['goodslink']
        shop = item['shop']
        shoplink = item['shoplink']
        price = item['price']
        goodrate = item['goodrate']
        sql = "insert into goods(goodsid,title,goodslink,shop,shoplink,price,goodrate) values (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, (goodsid,title,goodslink,shop,shoplink,price,goodrate))
        conn.commit()
        #conn.close()
        return item
