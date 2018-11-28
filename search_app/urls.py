from django.urls import path

from search_app import views

urlpatterns = [
    # path('search/',views.search,name='search'),
    path('page/',views.page,name='page'),
    path('main/',views.main,name='main'),
    path('vague/',views.search_vague,name='vague')

]