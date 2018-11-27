# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class YingjieshengPipeline(object):
#     def process_item(self, item, spider):
#         return item
import MySQLdb

class YingjieshengPipeline(object):
    def __init__(self):
        self.conn=MySQLdb.connect(
            host='172.16.14.90',port=3306,
            user='root',password='123456',charset='utf8',db='crawler'
        )
    def process_item(self, item, spider):
        self.save(item)
        return item

    def save(self,item):
        print(item)
            #job_require,,%s,,item['job_require'],item['company_net'],,company_net
        sql='insert into recruit_info(website,city,job_name,salary,experience_time,education,job_info,request_num,company,address,company_property,company_scale,company_business,issue_time,remark) VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        self.conn.cursor().execute(sql,[item['website'],item['city'],item['job_name'],item['salary'],item['experience_time'],item['education'],item['job_info'], item['request_num'],item['company'],item['address'], item['company_property'],item['company_scale'],item['company_business'],item['issue_time'],item['remark']])
        # print("wwwwwwwwwwww")
        self.conn.commit()