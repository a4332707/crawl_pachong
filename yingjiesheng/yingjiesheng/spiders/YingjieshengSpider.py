import scrapy
from lxml import etree
from  ..items import YingjieshengItem
class YJSpider(scrapy.Spider):
    name='yjs'
    #另一种起始连接的方式
    def start_requests(self):
        areas = ['1056', '1349', '1085', '1102']
        words = ['AI', '爬虫', '大数据','python web']    #死循环不要写到起始请求里面，比逊等到起始请求全部构造完毕才会开始采集

        for area in areas:
            for word in words:
                # 构造请求不给参数 默认是parse解析
                yield scrapy.Request(url='http://s.yingjiesheng.com/search.php?word='+ word +'&area='+ area +'&sort=score&start=0')

    def parse(self, response):
        html = etree.HTML(response.text)
        page = html.xpath('//div[@class="resultStats"]/text()')
        page=page[0][5:8]
        # print(response.url.split('start='))
        print(page,"总数")
        strs = response.url.split('start=')
        print(strs,"asasdaasdasd")
        # page = int(strs[1]+10)
        number= int(strs[1]) + 10
        print(number,'每页加')
        # print(page)

        if number < int(page):
            url = strs[0] + 'start=' + str(number)
            number += 10
            print(url,"asdadasda")
            yield scrapy.Request(url)

        # page=int(page)
        # for i in page:
        #     #http: // s.yingjiesheng.com / search.php?word = '+ word +' & area = '+ area +' & sort = score & start = 0
        urls=html.xpath('//h3[@class="title"]/a/@href')#//*[@id="container"]/div[1]/ul/li[10]/div/h3/a
        print(urls)
        for i in urls:
            # print('wwwww')
            yield scrapy.Request(i,callback=self.detail)

    # 三级回调函数
    def detail(self,resp):
        #构造item
        print('ok')
        item=YingjieshengItem()

        item['website'] = '应届生招聘网'
        #城市
        item['city']=resp.xpath('//*[@id="container"]/div[1]/div[1]/ol/li[2]/u/text()')[0].extract()
        #工作名字
        item['job_name'] = resp.xpath('//*[@id="container"]/div[1]/div[1]/ol/li[5]/u/text()')[0].extract()

        item['salary'] = ''

        item['experience_time']=''

        item['education']=''
        #职位信息
        job_info = resp.xpath('//*[@id="wordDiv"]/div/div/text()').extract()
        j = ''
        for i in job_info:
            j += i.strip()  # 责任与福利
        item['job_info'] = j

        item['request_num']=''

        item['company'] = resp.xpath('//*[@id="container"]/div[1]/h1/text()')[0].extract()  # 公司

        item['address']=''

        item['company_property']=''

        item['company_scale']=''

        item['company_business']=''

        item['issue_time'] = resp.xpath('//*[@id="container"]/div[1]/div[1]/ol/li[1]/u/text()').extract()

        item['remark'] = item['city']  + item['company'] + item['job_name']

        print(item['city'], item['job_name'], item['salary'], item['experience_time'], item['education'],
              item['job_info'], item['request_num'], item['company'], item['address'], item['company_property'],
              item['company_scale'],
              item['company_business'], item['issue_time'], item['remark'])

        yield  item