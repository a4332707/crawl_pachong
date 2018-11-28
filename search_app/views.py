from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import happybase,hashlib
# Create your views here.
from search_app.models import RecruitInfo
# conn_hbase=happybase.Connection(host='172.16.14.56',port=9090)
# conn_hbase.open()
# table=conn_hbase.table('crawler:recruit')
def main(request):
    return render(request,'main.html')
def page(request):
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
    page = Paginator(object_list=RecruitInfo.objects.filter(city=city, job_category=category), per_page=20).page(int(num))
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
    print(data)
    return JsonResponse({'data':data})
