import scrapy
class PSpider(scrapy.Spider):
    name = 'proxy'
    def start_requests(self):
        # {
        #     "origin": "219.143.103.186"
        # }
        req=scrapy.Request("http://httpbin.org/ip")
        #meta类字典结构，必须绑定到meta属性的proxy中
        req.meta['proxy']='http://118.190.95.35:9001'
        yield req
    def parse(self, response):
        print(response.text)