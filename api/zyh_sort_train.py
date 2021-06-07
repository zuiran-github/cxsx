from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import operator
import json


def sortByTime(info):
    """
    根据时间排序
    :param info: 列表
    :return: {"data": sorted_list}
    """
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^info')
    print(info)
    sorted_list = sorted(info, key=operator.itemgetter('dtime'))
    response = {"data": sorted_list}
    print('********************************response')
    print(response)

    return response



def sortByATime(info):
    """
    根据时间排序
    :param info: 列表
    :return: {"data": sorted_list}
    """
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^info')
    print(info)
    sorted_list = sorted(info, key=operator.itemgetter('atime'))
    response = {"data": sorted_list}
    print('********************************response')
    print(response)

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
def zyh_trainsortTime(request):
    '''
    根据出发时间排序
    :param request:
    :return:
    '''

    trainlist1 = request.GET.getlist('train[]')  # 获取字典进行排序

    trainlist = []
    for item in trainlist1:
        trainlist.append(json.loads(item))

    print('##############################')
    print(trainlist)
    if trainlist == None:
        return

    response = sortByTime(trainlist)

    return JsonResponse(response)


@require_http_methods(["GET"])
def zyh_trainsortPrice(request):
    '''
    火车票根据价格排序
    :param request:
    :return:
    '''

    trainlist1 = request.GET.getlist('train[]')  # 获取字典进行排序

    trainlist = []
    for item in trainlist1:
        trainlist.append(json.loads(item))

    if trainlist == None:
        return
    response = sortByPrice(trainlist)

    return JsonResponse(response)


@require_http_methods(["GET"])
def zyh_trainsortATime(request):
    '''
    根据到达时间排序
    :param request:
    :return:
    '''

    trainlist1 = request.GET.getlist('train[]')  # 获取字典进行排序

    trainlist = []
    for item in trainlist1:
        trainlist.append(json.loads(item))

    print('##############################')
    print(trainlist)
    if trainlist == None:
        return

    response = sortByATime(trainlist)

    return JsonResponse(response)