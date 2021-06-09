import urllib3
import json
import threading
import _thread as thread
from .zwf_menpiao_dahe import *
from .zwf_menpiao_feizhu import *
from .zwf_menpiao_klook import *
from .zwf_menpiao_lvmama import *
from .zwf_menpiao_qunar import *
from .zwf_menpiao_tongcheng import *
from .zwf_menpiao_tuniu import *
from .zwf_menpiao_xiecheng import *
from django.http import JsonResponse
import time
from fuzzywuzzy import process
from django.views.decorators.http import require_http_methods
from .zwf_menpiaosort import sortmenpiao



'''各对象'''
feizhu, xiecheng, tuniu, quna, lvmama, dahe, klook, tongcheng=None,None,None,None,None,None,None,None
'''是否已经初始化'''
inited = False
'''数据汇总结果'''
spotsInfo = []
'''储存关键词'''
city_keywords = []
N = 10


def run_search(xc,keyword,city):
    '''
    线程开始运行
    :param xc:
    :param keyword:
    :param city:
    :return:
    '''
    print(1111)
    xc.search_spots(keyword,city)
    # print(xc.name,xc.spotsInfo)


def merge2(spi, xc, name):
    '''
    把两个字典数据合并在一起
    :param spi:
    :param xc:
    :param name:
    :return:
    '''
    if len(name) == 0:
        spotsInfo = spi
    else:
        spotsInfo = {}
    for info in spi.keys():
        try:
            spotsInfo.setdefault(info, {})
            k = xc.spotsInfo[info]
            if len(name) == 0:
                spotsInfo[info][xc.name] = xc.spotsInfo[info]
            else:
                spotsInfo[info][name] = spi[info]
                spotsInfo[info][xc.name] = xc.spotsInfo[info]
            xc.spotsInfo.pop(info)
        except Exception as e:
            # print(e)
            if len(name) != 0:
                spotsInfo[info][name] = spi[info]
    for info in xc.spotsInfo.keys():
        spotsInfo.setdefault(info, {})
        spotsInfo[info][xc.name] = xc.spotsInfo[info]
    # print(spotsInfo)
    print('done')
    return spotsInfo


def merge(feizhu,xiecheng,tuniu,quna,lvmama,dahe,klook,tongcheng):
    '''
    把所有的平台的数据都合并在一起
    :param feizhu:
    :param xiecheng:
    :param tuniu:
    :param quna:
    :param lvmama:
    :param dahe:
    :param klook:
    :param tongcheng:
    :return:
    '''
    list = [feizhu,xiecheng,tuniu,quna,lvmama,dahe,klook,tongcheng]
    merged = False
    spotsInfo0 = {}
    while len(list)>0:
        l = list[0]
        if merged:
            spotsInfo0 = merge2(spotsInfo0,list.pop(0),'')
        else:
            spotsInfo0 = merge2(list.pop(0).spotsInfo,list.pop(0),l.name)
            merged = True
    # print(spotsInfo0)
    return spotsInfo0
    # merged = False
    # spotsInfo = {}
    # while True:
    #     donelist = []
    #     for xc in list:
    #         if xc.done:
    #             list.remove(xc)
    #             donelist.append(xc)
    #     if merged==False and len(donelist)>=2:
    #         xc1 = donelist.pop(0)
    #         spotsInfo = merge2(xc1.spotsInfo, donelist.pop(0), xc1.name)
    #         merged = True
    #     if len(donelist)>0:
    #         while(len(donelist)>0):
    #             spotsInfo = merge2(spotsInfo,donelist.pop(0),'')
    #     if len(list) == 0:
    #         break
    # print(spotsInfo)
    # print('done')


def init():
    '''
    建立对象
    :return:
    '''
    global inited
    global feizhu,xiecheng,tuniu,quna,lvmama,dahe,klook,tongcheng
    feizhu = FeizhuSpider()
    xiecheng = XiechengSpider()
    tuniu = TuNiuSpider()
    quna = QunaSpider()
    lvmama = LvmamaSpider()
    dahe = DaheSpider()
    klook = KlookSpider()
    tongcheng = TongchengSpider()
    inited = True


def searchSpots(keyword, city):
    '''
    根据关键词和城市返回对应景点的门票，目前已爬取的网站：飞猪、去哪、携程、途牛、klook、驴妈妈、同程、大河
    :param keyword:
    :param city:
    :return:
    '''
    global feizhu, xiecheng, tuniu, quna, lvmama, dahe, klook, tongcheng
    global spotsInfo,city_keywords#景点名称，门票（名称name，类别type，价格price，url，已售buy，旅行社from，可退isReturnable，预定时间bookTime,出票时间outTime，可用时间useTime,说明discription)
    if inited==False:
        init()

    # feizhu = menpiao.zwf_menpiao_feizhu.FeizhuSpider()
    # xiecheng = menpiao.zwf_menpiao_xiecheng.XiechengSpider()
    # tuniu = menpiao.zwf_menpiao_tuniu.TuNiuSpider()
    # quna = menpiao.zwf_menpiao_qunar.QunaSpider()
    # lvmama = menpiao.zwf_menpiao_lvmama.LvmamaSpider()
    # dahe = menpiao.zwf_menpiao_dahe.DaheSpider()
    # klook = menpiao.zwf_menpiao_klook.KlookSpider()
    # tongcheng = menpiao.zwf_menpiao_tongcheng.TongchengSpider()

    # list = [feizhu,xiecheng,tuniu,quna,lvmama,dahe,klook,tongcheng]
    # for l in list:
    #     l.search_spots(keyword,city)
    #     print(l.spotsInfo)
    # merge(feizhu, xiecheng, tuniu, quna, lvmama, dahe, klook, tongcheng)


    # feizhu.search_spots(keyword,city)
    # xiecheng.searchSpots(keyword,city)
    # tuniu.search_spots(keyword,city)
    # quna.search_spots(keyword,city)
    list = [feizhu,xiecheng,tuniu,quna,lvmama,dahe,klook,tongcheng]
    try:
        '''建立线程，提高速度'''
        t1 = threading.Thread(target=run_search, args=(xiecheng,keyword,city,))
        t2 = threading.Thread(target=run_search, args=(feizhu, keyword, city,))
        t3 = threading.Thread(target=run_search, args=(tuniu, keyword, city,))
        t4 = threading.Thread(target=run_search, args=(quna, keyword, city,))
        t5 = threading.Thread(target=run_search, args=(lvmama, keyword, city,))
        t6 = threading.Thread(target=run_search, args=(dahe, keyword, city,))
        t7 = threading.Thread(target=run_search, args=(klook, keyword, city,))
        t8 = threading.Thread(target=run_search, args=(tongcheng, keyword, city,))
        '''线程开始'''
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()

        '''父线程等待'''
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()
        t8.join()
        print(333)
        '''合并'''
        ti = merge(feizhu, xiecheng, tuniu, quna, lvmama, dahe, klook, tongcheng)
        ti = sortmenpiao(ti)
        spotsInfo.append(ti)
        city_keywords.append(city+''+keyword)


    except Exception as e:
        print(e)


@require_http_methods(["GET"])
def getTicketInfo(request):
    '''
    外部调用
    :param keyword:
    :param city:
    :return:
    '''
    keyword = request.GET.get('keyword')
    city = request.GET.get('city')
    print(request.GET)
    print(keyword)
    print(city)
    global spotsInfo, city_keywords
    result = process.extractBests(city+keyword, city_keywords, score_cutoff=99, limit=1)
    # print(keyword,city)
    # print(result)
    if len(result) == 0:
        searchSpots(keyword, city)
        print(spotsInfo[0].keys())
        print(spotsInfo[len(spotsInfo)-1].keys())

        spot = spotsInfo[len(spotsInfo)-1]
        response = {'data':spot}
        print(response)
        return JsonResponse(response)
    else:
        index = city_keywords.index(result[0][0])
        spot = spotsInfo[index]
        response = {'data': spot}
        print(response)
        return JsonResponse(response)



@require_http_methods(["GET"])
def getSpotTAI(request):
    '''
    外部调用
    :param keyword:
    :param city:
    :return:
    '''
    keyword = request.GET.get('keyword')
    print(request.GET)
    print(keyword)
    global tuniu
    result = process.extractBests(keyword, tuniu.spots.keys(), score_cutoff=50, limit=1)
    try:
        response = {'data':tuniu.spots[result[0][0]]}
    except Exception as e:
        print(e)
        response = {'data':{}}
    print(response)
    print(tuniu.spots)
    return JsonResponse(response)



if __name__ == '__main__':
    ticket = getTicketInfo('方特','青岛')
    print(ticket)
