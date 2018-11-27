import  scrapy
import json
# from scrapy框架.scrapy_133.scrapy_133.items import LagouItem

class LagouwangSpider(scrapy.Spider):
    name='lagouwang'

    start_urls=['https://www.lagou.com/upload/ltm/oss.html?u=/jobs/5350693.html&q=417&n=421&d=443&l=1249&dns=0&p=2144&pi=112&qn=1342&t=1542889226787']
    def parse(self, response):
        print(response.xpath('//a/text()').extract())

    # def start_request(self):
    #     citys = ['北京','上海','广州','深圳']
    #     kds=['AI','爬虫','大数据','python web']
    #     for city in citys:
    #         for kd in kds:
    #             yield scrapy.Request(url=)

    # def __init__(self):
    #     self.handles={'Referer':'https://www.lagou.com/jobs/list_?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    #     self.cookie={"user_trace_token":"20180526201245-0ea516fd-da30-4994-9995-5fa02a3eab36",
    #                 "LGUID":"20180526201246-19bb1f81-60de-11e8-a18e-525400f775ce",
    #                 "index_location_city":"%E5%85%A8%E5%9B%BD",
    #                 "JSESSIONID":"ABAAABAABEEAAJAF96A0BE8427F1DD99F8C9B9EB6D7970D",
    #                 "TG-TRACK-CODE":"search_code",
    #                 "SEARCH_ID":"acc14cb01bbe44db9e430661bccdc92e",
    #                 "_gid":"GA1.2.187875505.1527336770",
    #                 "_ga":"GA1.2.467998237.1527336770",
    #                 "Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6":"1527408192,1527408683,1527469793,1527486623",
    #                 "Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6":"1527503666",
    #                 "LGSID":"20180528183425-b12d579f-6262-11e8-ada5-525400f775ce",
    #                 "PRE_UTM":"",
    #                 "PRE_HOST":"",
    #                 "PRE_SITE":"https%3A%2F%2Fwww.lagou.com%2F",
    #                 "PRE_LAND":"https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D",
    #                 "LGRID":"20180528183425-b12d59ef-6262-11e8-ada5-525400f775ce"}
    #     self.url = 'https://www.lagou.com/jobs/positionAjax.json?px=new&needAddtionalResult=false'
    #     self.total_page = 0
    #     self.first = 'true'
    #     self.kd = ''
    #     self.pn = 1
    #
    #     def parse(self, response):
    #         item = LagouItem()
    #         data = json.loads(response.body)
    #         data_position = data['content']['positionResult']
    #         data_result = data_position['result']
    #         self.total_page = data_position['totalCount']
    #         for i in range(len(data_result)):
    #             item['salary'] = data_result[i]['salary']
    #             item['city'] = data_result[i]['city']
    #             item['workYear'] = data_result[i]['workYear']
    #             item['education'] = data_result[i]['education']
    #             # item['industryField'] = data_result[i]['industryField']
    #             item['companySize'] = data_result[i]['companySize']
    #             item['positionName'] = data_result[i]['positionName']
    #             # sal = data_result[i]['salary']
    #             # sal = sal.split('-')
    #             # if (len(sal) == 1):
    #             #     item['salary_min'] = sal[0][:sal[0].find('k')]
    #             #     item['salary_max'] = sal[0][:sal[0].find('k')]
    #             # else:
    #             #     item['salary_min'] = sal[0][:sal[0].find('k')]
    #             #     item['salary_max'] = sal[1][:sal[1].find('k')]
    #             yield item
    #         if (self.pn <= self.total_page):
    #             '''当前页数小于总页数，那么我们就继续请求下一页，再爬取'''
    #         print("pn：{}    运行中请勿打断...".format(self.pn + 1))
    #         time.sleep(0.5)
    #         self.pn += 1
    #         yield scrapy.http.FormRequest(self.url, cookies=self.cookie, headers=self.headers,
    #                                       formdata={'first': self.first, 'kd': self.kd, 'pn': str(self.pn)},
    #                                       callback=self.parse)
    #
    # def start_requests(self):
    #     return [scrapy.http.FormRequest(self.url, cookies=self.cookie, headers=self.headers,
    #                                     formdata={'first': self.first, 'kd': self.kd, 'pn': str(self.pn)},
    #                                     callback=self.parse)]






