# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapy133Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    salary=scrapy.Field()

# class LagouItem(scrapy.Item):
#     salary=scrapy.Field()
#     city=scrapy.Field()
#     workYear=scrapy.Field()
#     education=scrapy.Field()
#     # industryField=scrapy.Field() #产业领域
#     companySize=scrapy.Field()
#     positionName=scrapy.Field()
