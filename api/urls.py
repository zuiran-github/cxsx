from .views import *
from django.conf.urls import url
# from .allcompany import *
from .zyh_flight import *


urlpatterns = [


    url(r"allsearch$", allsearch, )  # 查询所有票的价格



]