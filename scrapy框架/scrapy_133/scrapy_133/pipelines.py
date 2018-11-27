# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

class Scrapy133Pipeline(object):
    def __init__(self):
        self.conn=MySQLdb.connect(
            host='127.0.0.1',port=3306,
            user='root',password='000000',charset='utf8',db='dbzhilian'
        )
    def process_item(self, item, spider):
        self.save(item)
        return item

    def save(self,item):
        sql='insert into t_zhilian_scrapy(title,salary)VALUE (%s,%s)'
        self.conn.cursor().execute(sql,[item['title'],item['salary']])
        self.conn.commit()