import  scrapy
class BDSpider(scrapy.Spider):
    #给爬虫起一个名字来区分开其他爬虫
    name='bd'
    # 必须有一个起始url
    start_urls=['http://www.baidu.com']
    # 必须有一个解析方法
    def parse(self, response):
        # print(response.text)
        print(response.xpath('//a/text()').extract()) #返回的是选择器select，如果需要选择器中的data，需要序列化



