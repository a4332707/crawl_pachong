import scrapy
class ZPHSpider(scrapy.Spider):
    name='zph'
    #发送post请求只能用start_request构造起始请求
    def start_requests(self):
        url = 'http://www.honestcareer.com/hr/dologin'
        formdata = {
            'type': '1',
            'username': '18501279410',
            'password': 'hbw123'
        }
        yield scrapy.FormRequest(url=url,formdata=formdata)

    def parse(self, response):
        yield scrapy.Request('http://www.honestcareer.com/hr/index',callback=self.parse1)


    def parse1(self,resp):
        print(resp.text)