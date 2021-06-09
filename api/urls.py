from .views import *
from django.conf.urls import url
# from .allcompany import *
from .zyh_flight import *
from .zyh_train import *
from .zyh_sort import *
from .zyh_sort_train import *
from .zyh_choose import *
from .qxw_jiudian import *



from .yule import zwf_tupian
from .yule import zwf_yule_dazhongdianping
from .xiaochi import zwf_meishi_xiecheng
from .menpiao import zwf_searchSpots



urlpatterns = [


    url(r"allsearch$", allsearch, ),  # 查询所有机票的价格
    url(r"getTraininfo$", zyh_getTrainTicket, ),  # 查询所有火车票的价格
    url(r"trainshijianpai$", zyh_trainsortTime, ),  # 火车票根据时间排序
    url(r"trainjiagepai$", zyh_trainsortPrice, ),  # 火车票根据价格排序
    url(r"sortbytime$", zyh_sortByTime, ),  # 机票根据时间排序
    url(r"sortbycompany$", zyh_sortByCompany, ),  # 机票根据航空公司名称排序
    url(r"sortbyprice$", zyh_sortByPrice, ),  # 机票根据价格排序
    url(r"trainchoose$", zyh_choose_train, ),  # 根据车型筛选
    url(r"flightATimesort$", zyh_sortByATime, ),  # 机票按照到达时间排序
    url(r"huochepiaoAtime$", zyh_trainsortATime, ),  # 火车票按照到达时间排序


    url(r"jiudiansort$", qxw_jiudian_sort, ),  # 酒店推荐
    url(r"jiudiandistance$", qxw_distance, ),  # 距离
    url(r"jiudiancommends$", qxw_commends, ),  # 评价
    url(r"jiudianscore$", qxw_score, ),  # 评分
    url(r"pricedescend$", qxw_price_descend, ),  # 价格降序
    url(r"priceascend$", qxw_price_ascend, ),  # 价格升序
    url(r"pathplan$", qxw_path, ),  # 路径规划
    url(r"dianjifanhui$", qxw_dianji, ),  # 点击返回信息




    url(r"getTicketInfo$", zwf_searchSpots.getTicketInfo, ),  # 获取景点门票信息
    url(r"getMeishiInfo$", zwf_meishi_xiecheng.getInfo, ),  # 获取美食信息
    url(r"getSpotsInfo$", zwf_tupian.getInfo, ),  # 获取某个景点的详细信息
    url(r"getSpotsInfoofCity$", zwf_tupian.getInfoofCity, ),  # 获取某个城市的所有景点信息
    url(r"getYouhuiInfo$", zwf_yule_dazhongdianping.getYouhuiInfo, ),  # 获取优惠券信息
    url(r"getSpotTAI$", zwf_searchSpots.getSpotTAI, ), #获取景点信息

]