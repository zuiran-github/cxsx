from .views import *
from django.conf.urls import url
# from .allcompany import *
from .zyh_flight import *
from .zyh_train import *


urlpatterns = [


    url(r"allsearch$", allsearch, ),  # 查询所有机票的价格
    url(r"getTraininfo", zyh_getTrainTicket, ),  # 查询所有火车票的价格



]