from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import operator
import json


def sortByTime(info):
    """
    根据出发时间排序
    :param info: 列表
    :return: {"data": sorted_list}
    """

    sorted_list = sorted(info, key=operator.itemgetter('dTime'))
    response = {"data": sorted_list}

    return response



def sortByATime(info):
    """
    根据到达时间排序
    :param info: 列表
    :return: {"data": sorted_list}
    """

    sorted_list = sorted(info, key=operator.itemgetter('aTime'))
    response = {"data": sorted_list}

    return response



def sortByCompany(info):
    """
    根据航班号排序
    :param info: 列表
    :return: {"data": sorted_list}
    """

    sorted_list = sorted(info, key=operator.itemgetter('company'))
    response = {"data": sorted_list}

    return response


def sortByPrice(info):
    """
    根据价格排序
    :param info: 列表
    :return: {"data": sorted_list}
    """

    sorted_list = sorted(info, key=operator.itemgetter('price'))
    response = {"data": sorted_list}

    return response




@require_http_methods(["GET"])
def zyh_sortByTime(request):
    '''
    根据出发时间排序
    :param request:
    :return:
    '''

    flightlist1 = request.GET.getlist('flight[]')  # 获取字典进行排序

    flightlist = []
    for item in flightlist1:
        flightlist.append(json.loads(item))

    if flightlist == None:
        return
    print('**********************************************')
    print(flightlist)
    response = sortByTime(flightlist)

    return JsonResponse(response)



@require_http_methods(["GET"])
def zyh_sortByATime(request):
    '''
    根据出发时间排序
    :param request:
    :return:
    '''

    flightlist1 = request.GET.getlist('flight[]')  # 获取字典进行排序

    flightlist = []
    for item in flightlist1:
        flightlist.append(json.loads(item))

    if flightlist == None:
        return
    print('**********************************************')
    print(flightlist)
    response = sortByATime(flightlist)

    return JsonResponse(response)



@require_http_methods(["GET"])
def zyh_sortByCompany(request):

    flightlist1 = request.GET.getlist('flight[]')  # 获取字典进行排序

    flightlist = []
    for item in flightlist1:
        flightlist.append(json.loads(item))

    if flightlist == None:
        return

    response = sortByCompany(flightlist)

    return JsonResponse(response)




@require_http_methods(["GET"])
def zyh_sortByPrice(request):

    flightlist1 = request.GET.getlist('flight[]')  # 获取字典进行排序

    flightlist = []
    for item in flightlist1:
        flightlist.append(json.loads(item))

    if flightlist == None:
        return
    response = sortByPrice(flightlist)

    return JsonResponse(response)




