import scrapy
class WbSpider(scrapy.Spider):
    name = 'wb'
    start_urls=['https://weibo.com/a/aj/transform/loadingmoreunlogin?ajwvr=6&category=0&page=2&lefnav=0&cursor=&__rnd=1542678470955']

    def parse(self, response):
        print(response.text)
