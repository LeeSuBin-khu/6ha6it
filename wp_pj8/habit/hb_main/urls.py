from django.conf.urls import url
from django.urls import path
from . import views #view와 연결하기 위해서

app_name="hb_main" #namespace

urlpatterns =[
    path('', views.home, name='home'),
    url(r'^result/', views.result, name='result'),
    url(r'^adding/$', views.adding, name='adding'),
    url(r'^doit/$', views.doit, name='doit'),
    url(r'^statistics/(?P<habit_id>\d+)/$', views.statistics, name='statistics'),
    url(r'^deleting/$', views.deleting, name='deleting'),
    url(r'^statistics2/(?P<habit_id>\d+)/$', views.statistics2, name='statistics2'),
    url(r'^updating/$', views.updating, name='updating'),
    url(r'^updating/(?P<habit_id>\d+)/$', views.updating, name='updating'),
]