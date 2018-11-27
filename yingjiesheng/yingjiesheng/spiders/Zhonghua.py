#中华英才网
import scrapy
import json
from lxml import etree
from  ..items import YingjieshengItem
class YJSpider(scrapy.Spider):
    name='zh'
    #另一种起始连接的方式
    #死循环不要写到起始请求里面，比逊等到起始请求全部构造完毕才会开始采集
    # def __init__(self):
    #     self.item=YingjieshengItem()
    def start_requests(self):
       # city_ids = ['bj']#, 'sh', 'gz', 'sz']
       #  kws = ['AI']#, '爬虫', '大数据', 'python web']
       #  for city_id in city_ids:
       #      for kw in kws:
       #          #构造请求不给参数 默认是parse解析
       #          print(scrapy.Request(url='http://search.chinahr.com/'+city_id +'/job/pn2/?key='+kw+''))
       #          yield scrapy.Request('http://search.chinahr.com/'+city_id +'/job/pn2/?key='+kw+'')

                yield scrapy.Request('http://search.chinahr.com/bj/job/pn2/?key=AI')

    def parse(self, response):
        html = etree.HTML(response.text)
        page = html.xpath('//*[@id="container"]/div[2]/div/p/span/text()')[0].encode("utf-8")
        page=page.decode()
        # print(page,type(page))
        # str=response.url.split('2')
        page=int(str(page))//30
        # print(page,"sssssssssssssss")
        city_ids = ['bj' , 'sh', 'gz', 'sz']
        kws = ['AI', '爬虫', '大数据', 'python web']
        for city_id in city_ids:
             for kw in kws:
                # item = YingjieshengItem()
                # item['job_category']=kw
                # print(item['kw'])
                for i in range(page):
                        # print(scrapy.Request(url='http://search.chinahr.com/' + city_id + '/job/pn' + str(i) + '/?key=' + kw + ''))
                        yield scrapy.Request(url='http://search.chinahr.com/' + city_id + '/job/pn'+str(i)+'/?key=' + kw + '')

        urls = html.xpath('//div[@class="jobList pc_search_listclick"]/@data-detail')  # //*[@id="container"]/div[1]/ul/li[10]/div/h3/a
        # print(urls,"凄凄切切群群群群")
        for i in urls:
            # print('wwwww')
            yield scrapy.Request(i,callback=self.detail)

    # 三级回调函数
    def detail(self,resp):
        #构造item
        #/html/body/div[3]/div[2]/div[2]/div/div[1]/h1
        item=YingjieshengItem()
        # try:
        item['website']='中华英才网'

        item['city']=resp.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()')[0].extract()

        item['job_name']=resp.xpath('//h1/@title')[0].extract()

        item['salary']=resp.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/strong/text()')[0].extract()

        item['experience_time'] = resp.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()')[1].extract()

        item['education'] = resp.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()')[2].extract()

        job = resp.xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div//text()').extract()
        j = ''
        for i in job:
            j += i.strip()  # 责任与福利
        item['job_info']=j

        item['request_num'] = resp.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()')[3].extract()  # 招聘人数

        item['company']=resp.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[1]/a[1]/@title')[0].extract()

        address = resp.xpath('/html/body/div[3]/div[2]/div[3]/div[2]/div/p/text()')[1].extract()
        a = ''
        for i in address:
            a += i.strip()  # 工作地址
        item['address']=a

        item['company_property'] = resp.xpath('/html/body/div[3]/div[2]/div[4]/div[1]/div[2]/p[1]/text()').extract()

        item['company_scale'] = resp.xpath('/html/body/div[3]/div[2]/div[4]/div[1]/div[2]/p[2]/@title')[0].extract()

        # item['job_info']=resp.xpath('//div[@class="bmsg job_msg inbox"]/p/text()').extract()

        item['company_business'] = resp.xpath('/html/body/div[3]/div[2]/div[4]/div[1]/div[2]/p[3]/@title')[0].extract()

        issue_time = resp.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()')[4].extract()
        iss = ''
        for i in issue_time:
            iss += i.strip()  # 发布时间
        item['issue_time']=iss

        item['remark'] = item['city']  + item['company'] + item['job_name']  # 联合唯一

        print(item['city'],item['job_name'],item['salary'],item['experience_time'],item['education'],
              item['job_info'],item['request_num'],item['company'],item['address'],item['company_property'],item['company_scale'],
              item['company_business'],item['issue_time'],item['remark'])

        yield  item
        # except:
        #     pass