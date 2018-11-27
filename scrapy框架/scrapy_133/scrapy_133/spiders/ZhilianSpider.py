import scrapy
import json
from  ..items import Scrapy133Item
class ZLSpider(scrapy.Spider):
    name='zl'
    #另一种起始连接的方式
    #死循环不要写到起始请求里面，比逊等到起始请求全部构造完毕才会开始采集
    def start_requests(self):
        city_ids = ['530', '538', '765', '763']
        kws = ['AI', '爬虫', '大数据', 'python web']
        for city_id in city_ids:
            for kw in kws:
                #构造请求不给参数 默认是parse解析
                yield scrapy.Request(url='https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=' + city_id + '&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=' + kw+ '&kt=3&_v=0.32069266&x-zp-page-request-id=3f968250f3c34bb684f49471e62bcad0-1542178189207-705386&start=0')

    def parse(self, response):
        datas=json.loads(response.text)['data']
        for data in datas['results']:
            yield  scrapy.Request(data['positionURL'],callback=self.detail)
        #抽取三级的url,交给三级url对应的解析函数
        #构造二级请求
        num=datas['numFound']
        strs=response.url.split('start=')
        number=int(strs[1])+60
        if number<num:
            url=strs[0]+'start='+str(number)
            yield  scrapy.Request(url)

    # 三级回调函数
    def detail(self,resp):
        #构造item
        item=Scrapy133Item()
        item['title']=resp.xpath("//h1/text()")[0].extract()
        item['salary']=resp.xpath('//li[@class="info-money"]/strong/text()')[0].extract()
        yield  item