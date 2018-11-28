import random
import time
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import happybase,hashlib
# Create your views here.
from django.db.models import Count, Max,Avg,Min,Sum
from search_app.models import RecruitInfo
# conn_hbase=happybase.Connection(host='172.16.14.56',port=9090)
# conn_hbase.open()
# table=conn_hbase.table('crawler:recruit')
def main(request):
    return render(request,'main.html')
def page(request):
    v_cookie=request.COOKIES.get('v_pass')
    if not v_cookie:
        vister=Vister()
        v_pass=random.sample('qwertyuiopasdfghjkzxcvbnm',8)
        request.session[str(v_pass)]=vister
        page = Paginator(object_list=RecruitInfo.objects.filter(city="北京", job_category='大数据'), per_page=20).page(1)
        resp = render(request, 'menu.html', {'page': page, 'num':1})
        resp.set_cookie('v_pass', str(v_pass))
        return resp
    else:
        vister=request.session.get(v_cookie)
        vister.all_time+=1
        v_pass=v_cookie
        request.session[str(v_pass)] = vister
    num = request.GET.get("num")
    city = request.GET.get('city')
    if not city:
        city='北京'
    category = request.GET.get('category')
    if not category:
        category='大数据'
    company = request.GET.get('company')
    if not num:
        num=1
    page=Paginator(object_list=RecruitInfo.objects.filter(city=city, job_category=category), per_page=20).page(
        int(num))
    if vister.check() or not v_cookie:
        return render(request,'menu.html',{'page':page,'num':num})
    else:
        time.sleep(2)
        return render(request,'menu.html',{'page':page,'num':num})



# def search(request):
#     num=request.GET.get('num')
#     if not num:
#         num=11
#     website=request.GET.get('website')
#     if not website:
#         website='内推网'
#     city = request.GET.get('city')
#     if not city:
#         city = '北京'
#     category = request.GET.get('category')
#     if not category:
#         category = '大数据'
#     job_name = request.GET.get('job_name')
#     if not job_name:
#         job_name='20503-AI应用Linux后台研发工程师（上海）'
#     row_start=website+':'+city+':'+category+':'+job_name
#     # row_stop=website+':'+city+':'+category+':Java开发工程师（大数据方向）-平台事业部'
#     datas=table.scan(row_start=row_start,columns=['show'],limit=20)
#     l=table.scan()
#     pages=[]
#     for key,value in datas:
#         info=dict()
#         for i,j in value.items():
#
#             info.update({i.decode()[5:]:j.decode()})
#         pages.append(info)
#     # return render(request,'suggest.html')
#     return render(request,'menu_base.html',{'page':pages,'num':num})
    # return HttpResponse('page')
# {'salary': '30k-45k', 'job_info': '岗位职责：1.负责时空位置大数据对外接口后台和服务框架的开发和运营；2.负责时空位置大数据数据中、后台的建设以及数据和服务安全方面的建设；岗位要求：1.重点大学本科以上学历，计算机及相关专业；2.两年以上相关工作经验，精通算法与数据结构，精通C/C++编程语言；3.精通linux、unix编程环境，熟悉数据库；4.精通网络编程，有分布式系统开发经验，有大平台开发经验优先；5.熟悉GIS和时空大数据处理和管理，有相关工作经验者优先，6.具备优秀的独立解决问题能力, 善于团队合作，沟通良好，有一定的抗压能力；', 'education': '本科', 'job_name': 'CSIG16-大数据后台研发工程师', 'experience_time': '5-10年', 'city': '北京', 'job_category': '大数据', 'company': '腾讯', 'address': '\r\n\t\t\t北京\r\n\t\t'}
def search_vague(request):
    value=request.GET.get('value')
    value='大数据'
    datas=RecruitInfo.objects.filter(job_name__contains=value).values('job_name')[:10]
    data=[]
    for i in datas:
        data.append(i['job_name'])
    return JsonResponse({'data':data})
def get_data(item):
    return RecruitInfo.objects.filter(city=item).aggregate(Count('id'))['id__count']
def get_data_category(item):
    return RecruitInfo.objects.filter(job_category=item).aggregate(Count('id'))['id__count']
def column(request):
    num_bj=get_data('北京')
    num_sh=get_data('上海')
    num_sz=get_data('广州')
    num_gz=get_data('深圳')
    data=[num_bj,num_sh,num_sz,num_gz]
    return render(request,'column.html',{'data':data})
def pie(request):
    python_web= get_data_category('Python Web')
    crawler = get_data_category('爬虫')
    big_data = get_data_category('大数据')
    ai= get_data_category('AI')
    data = [python_web,crawler,big_data,ai]
    print(data)
    return render(request, 'pie.html', {'data': data})
def map(request):
    num_bj=get_data('北京')
    num_sh=get_data('上海')
    num_sz=get_data('广州')
    num_gz=get_data('深圳')
    data=[num_bj,num_sh,num_sz,num_gz]
    return render(request,'map.html',{'data':data})
def line(request):
    num_bj=get_data('北京')
    num_sh=get_data('上海')
    num_sz=get_data('广州')
    num_gz=get_data('深圳')
    data=[num_bj,num_sh,num_sz,num_gz]
    return render(request,'line.html',{'data':data})
class Vister:
    def __init__(self,all_time=1,first_time=time.time()):
        self.all_time=all_time
        self.first_time=first_time
        self.vip=None
    def get_cookie(self,request):
        self.cookie=request.COOKIES['v_pass']
    def check(self):
        if self.all_time>50:
            result=time.time() - self.first_time
            if result<1:
                self.all_time = 0
                return None
        return True