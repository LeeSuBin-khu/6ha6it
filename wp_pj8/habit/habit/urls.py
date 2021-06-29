from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include ######################

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('hb_main.urls', namespace='hb_main')), ########################
]
