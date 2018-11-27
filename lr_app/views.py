from django.shortcuts import render

# from lr_app.models import User
from crawl_pachong.lr_app.models import RecruitInfo




# Create your views here.
#  转发登录页面


def login(request):
    return render(request,'login.html')








def introduce(request):
    return render(request,'introduce.html')