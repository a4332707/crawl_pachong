# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YingjieshengItem(scrapy.Item):
    # define the fields for your item here like:
    # kw=scrapy.Field()
    website=scrapy.Field()#网站
    city=scrapy.Field()#城市
    # job_category = scrapy.Field()#工作种类
    job_name=scrapy.Field()#职位
    salary = scrapy.Field()#工资
    experience_time=scrapy.Field()#工作年限
    education=scrapy.Field()#学历
    job_info=scrapy.Field()#工作信息
    job_require=scrapy.Field()#职位需求
    request_num=scrapy.Field()#招聘人数
    company=scrapy.Field()#公司
    address=scrapy.Field()#地址
    company_scale=scrapy.Field()#公司规模
    company_net=scrapy.Field()#公司网站
    company_property=scrapy.Field()#公司性质
    company_business=scrapy.Field()#公司主营业务
    issue_time=scrapy.Field()#发布时间
    remark=scrapy.Field()#唯一
    pass
