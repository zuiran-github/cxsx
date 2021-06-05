from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .qxw import qxw_main
from .qxw import qxw_pathPlanning
import json


@require_http_methods(["GET"])
def qxw_jiudian_sort(request):

    # 测试
    city = request.GET.get('city')[:-1]   # '上海'
    places = request.GET.getlist('scenics[]')  # ['上海城隍庙 上海市黄浦区方浜中路249号', '上海朱家角古镇旅游区 新风路与美周路交界处']
    checkin_time = request.GET.get('date1')  # '2021-06-21'
    checkout_time = request.GET.get('date2')  # '2021-06-22'
    type = request.GET.get('type')  # '全部'

    print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
    print(request.GET)
    print(checkin_time)
    print(checkout_time)
    print(places)

    response = qxw_main.qxw_jiudian(city, places, checkin_time, checkout_time, type)
    # print(type(response))
    # response = json.dumps(response)
    # print(type(response))

    # print(response)
    return JsonResponse(response)



@require_http_methods(["GET"])
def qxw_distance(request):

    # 测试
    city = request.GET.get('city')[:-1]   # '上海'
    places = request.GET.getlist('scenics[]')  # ['上海城隍庙 上海市黄浦区方浜中路249号', '上海朱家角古镇旅游区 新风路与美周路交界处']
    checkin_time = request.GET.get('date1')  # '2021-06-21'
    checkout_time = request.GET.get('date2')  # '2021-06-22'
    type = request.GET.get('type')  # '全部'


    print('oooooooooooooooooooooooooooooooooo')
    response = qxw_main.qxw_distance_output(city, places, checkin_time, checkout_time, type)

    print('distanceresponse#########################################')
    print(response)
    print('qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq')

    return JsonResponse(response)


@require_http_methods(["GET"])
def qxw_score(request):

    # 测试
    city = request.GET.get('city')[:-1]   # '上海'
    places = request.GET.getlist('scenics[]')  # ['上海城隍庙 上海市黄浦区方浜中路249号', '上海朱家角古镇旅游区 新风路与美周路交界处']
    checkin_time = request.GET.get('date1')  # '2021-06-21'
    checkout_time = request.GET.get('date2')  # '2021-06-22'
    type = request.GET.get('type')  # '全部'

    print('score gfsdklgnksnf;owafnjknfjklsangu')
    response = qxw_main.qxw_score_output(city, places, checkin_time, checkout_time, type)
    print(response)
    print()

    return JsonResponse(response)


@require_http_methods(["GET"])
def qxw_commends(request):

    # 测试
    city = request.GET.get('city')[:-1]   # '上海'
    places = request.GET.getlist('scenics[]')  # ['上海城隍庙 上海市黄浦区方浜中路249号', '上海朱家角古镇旅游区 新风路与美周路交界处']
    checkin_time = request.GET.get('date1')  # '2021-06-21'
    checkout_time = request.GET.get('date2')  # '2021-06-22'
    type = request.GET.get('type')  # '全部'

    print(places)
    print('commends jhflaj;ljaglsadjfioewf')
    response = qxw_main.qxw_commends_output(city, places, checkin_time, checkout_time, type)
    print(response)
    print()

    return JsonResponse(response)



@require_http_methods(["GET"])
def qxw_price_descend(request):

    # 测试
    city = request.GET.get('city')[:-1]   # '上海'
    places = request.GET.getlist('scenics[]')  # ['上海城隍庙 上海市黄浦区方浜中路249号', '上海朱家角古镇旅游区 新风路与美周路交界处']
    checkin_time = request.GET.get('date1')  # '2021-06-21'
    checkout_time = request.GET.get('date2')  # '2021-06-22'
    type = request.GET.get('type')  # '全部'


    print('prcedescend hsalgjnsklafjslkfjlas;')
    response = qxw_main.qxw_price_descend_output(city, places, checkin_time, checkout_time, type)
    print(response)
    print()

    return JsonResponse(response)



@require_http_methods(["GET"])
def qxw_price_ascend(request):

    # 测试
    city = request.GET.get('city')[:-1]   # '上海'
    places = request.GET.getlist('scenics[]')  # ['上海城隍庙 上海市黄浦区方浜中路249号', '上海朱家角古镇旅游区 新风路与美周路交界处']
    checkin_time = request.GET.get('date1')  # '2021-06-21'
    checkout_time = request.GET.get('date2')  # '2021-06-22'
    type = request.GET.get('type')  # '全部'

    print(places)

    print('price ascend jfalsjflas;jf;sajf;ldasjfkljaslfjas')
    response = qxw_main.qxw_price_ascend_output(city, places, checkin_time, checkout_time, type)
    print(response)
    print()

    return JsonResponse(response)


@require_http_methods(["GET"])
def qxw_path(request):

    hotel = request.GET.get('hotelname')   # '上海'
    places = request.GET.getlist('scenic[]')  # ['上海城隍庙 上海市黄浦区方浜中路249号', '上海朱家角古镇旅游区 新风路与美周路交界处']

    print('***************************')
    print(request.GET)
    print(places)
    print('******************************')
    response = qxw_pathPlanning.qxw_path(hotel, places)

    return JsonResponse(response)

