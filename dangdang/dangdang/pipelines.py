# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import re


class DangdangPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host='localhost', port=3306,
                               user='dsuser', password='123456', db='dsdb')
        cursor = conn.cursor()
        for i in range(0, len(item['title'])):
            title = item['title'][i]
            link = item['link'][i]
            comment = item['comment'][i]
            pat = '^(\d+)'
            comment = re.compile(pat).findall(comment)[0]
            sql = "insert into books(title,link,comment) values (%s,%s,%s)"
            cursor.execute(sql, (title, link, comment))
            conn.commit()
        conn.close()
        return item
