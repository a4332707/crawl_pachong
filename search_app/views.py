import random
import time
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import happybase,hashlib
# Create your views here.
from django.db.models import Count, Max,Avg,Min,Sum
from redis import Redis

from search_app.models import RecruitInfo
conn_hbase=happybase.Connection(host='172.16.14.56',port=9090)
conn_hbase.open()
table=conn_hbase.table('crawler:recruit')
red=Redis(host='172.16.14.93',port=7000)
#显示主页
def main(request):
        return render(request,'main.html')
#查询页面
def page(request):
    v_cookie = request.COOKIES.get('v_pass')
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
    website = request.GET.get('website')
    if not website:
        website = '内推网'
    job_name = request.GET.get('job_name')
    if not job_name:
        job_name = '20503-AI应用Linux后台研发工程师（上海）'
    company = request.GET.get('company')
    if not num:
        num=1
    if int(num)>5 and not vister.vip:
        num=5
    if int(num) > 10:
        if vister.check() or not v_cookie and vister.crawler:
            return search(request,website,city,category,job_name,num)
        else:
            time.sleep(30)
            return search(request, website, city, category, job_name,num)
    else:
        page=Paginator(object_list=RecruitInfo.objects.filter(city=city, job_category=category), per_page=20).page(int(num))
        if vister.check() or not v_cookie and vister.crawler:
            return render(request,'menu.html',{'page':page,'num':num})
        else:
            time.sleep(30)
            return render(request,'menu.html',{'page':page,'num':num})
#hbase上查询数据
def search(request,website,city,category,job_name,num):
    row_start=website+':'+city+':'+category+':'+job_name
    datas=table.scan(row_start=row_start,columns=['show'],limit=20)
    l=table.scan()
    pages=[]
    for key,value in datas:
        info=dict()
        for i,j in value.items():
            info.update({i.decode()[5:]:j.decode()})
        pages.append(info)
    return render(request,'menu_base.html',{'page':pages,'num':num})
def search_vague(request):
    value=request.GET.get('value')
    value='大数据'
    datas=RecruitInfo.objects.filter(job_name__contains=value).values('job_name')[:10]
    data=[]
    for i in datas:
        data.append(i['job_name'])
    return JsonResponse({'data':data})
#根据城市查询数量的方法
def get_data(item):
    return RecruitInfo.objects.filter(city__icontains=item).aggregate(Count('id'))['id__count']
#获取相应城市的统计数量
def get_data_city():
    num_bj = get_data('北京')
    num_sh = get_data('上海')
    num_sz = get_data('广州')
    num_gz = get_data('深圳')
    return [num_bj, num_sh, num_sz, num_gz]
def get_data_category(item):
    return RecruitInfo.objects.filter(job_category=item).aggregate(Count('id'))['id__count']
#柱状图
def column(request):
    data=get_data_city()
    return render(request,'column.html',{'data':data})
#饼图
def pie(request):
    python_web= get_data_category('Python Web')
    crawler = get_data_category('爬虫')
    big_data = get_data_category('大数据')
    ai= get_data_category('AI')
    data = [python_web,crawler,big_data,ai]
    return render(request, 'pie.html', {'data': data})
#地图
def map(request):
    data = get_data_city()
    return render(request,'map.html',{'data':data})
#折线图
def line(request):
    data = get_data_city()
    return render(request,'line.html',{'data':data})
#vister类,
class Vister:
    def __init__(self,all_time=1,first_time=time.time()):
        self.all_time=all_time
        self.first_time=first_time
        self.vip=None
        self.crawler=True
        self.ip=None
        self.username=None
        self.login_time=None
    def check(self):
        if self.all_time>10:
            result=time.time() - self.first_time
            if result<1:
                self.all_time = 0
                self.crawler = None
                return None
            self.all_time=1
        return True
#用户登录了访问了哪个城市,哪个类数据
def log_redis_user(user=None,ip=None,city=None,category=None,login_time=None,request_time=None):
    data={'username':user,'value':{'ip':ip,'city':city,'job_category':category,'login_time':login_time,'request_time':request_time}}
    red.lpush('user_log',data)



