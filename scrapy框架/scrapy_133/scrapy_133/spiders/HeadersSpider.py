import scrapy
class HSpider(scrapy.Spider):
    name = 'headers'
    def start_requests(self):
        yield  scrapy.Request("http://httpbin.org/headers",headers={'User-Agent':'AI123'})
    def parse(self, response):
        print(response.text)