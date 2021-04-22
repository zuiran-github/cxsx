from django.shortcuts import render
from django.http import JsonResponse
import json
import requests
# Create your views here.

def xiamen(request):
    # date = request.GET.get('goDdate')
    # dep = request.GET.get('departure')
    # arr = request.GET.get('destination')
    date = "2021-05-13"
    dep = '成都'
    arr = '厦门'
    dict = cityCode()
    depcode = dict[dep]
    arrcode = dict[arr]
    piao = xiamen1(date, depcode, arrcode)

    return JsonResponse(piao)




def cityCode():
    url = 'https://wwwapi.xiamenair.com/api/offers/city'

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'https://www.xiamenair.com/',
        'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': 'gr_user_id=834f2db0-e127-4d85-a24f-c45dcf96b835; b014f44b281415f1_gr_session_id=25345647-14f4-42dd-8223-32a7a07e8249; b014f44b281415f1_gr_session_id_25345647-14f4-42dd-8223-32a7a07e8249=true; _ga=GA1.2.418467561.1618753452; _gid=GA1.2.1827916485.1618753452; _gat_UA-96517318-2=1',
        'Host': 'wwwapi.xiamenair.com',
        'Origin': 'https://www.xiamenair.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }

    r = requests.get(url=url, headers=headers)

    dict = {}

    jsdata = json.loads(r.text)['result']['mainlandCityList']
    # print(jsdata)
    # print(type(jsdata))
    # print(len(jsdata))
    for item in jsdata:
        # print(jsdata[item])
        # print(type(jsdata[item]))
        # print(len(jsdata[item]))
        for i in range(len(jsdata[item])):
            code = jsdata[item][i]['iataApCode']
            jichangname = jsdata[item][i]['cityChName']
            cityname = jsdata[item][i]['cityMLName']
            dict[jichangname] = code

    # print(list)
    return dict


def xiamen1(date, departure, arrival):
    url = "https://wwwapi.xiamenair.com/api/offers"

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'https://www.xiamenair.com/',
        'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': 'gr_user_id=834f2db0-e127-4d85-a24f-c45dcf96b835; b014f44b281415f1_gr_session_id=25345647-14f4-42dd-8223-32a7a07e8249; b014f44b281415f1_gr_session_id_25345647-14f4-42dd-8223-32a7a07e8249=true; _ga=GA1.2.418467561.1618753452; _gid=GA1.2.1827916485.1618753452; _gat_UA-96517318-2=1',
        'Host': 'wwwapi.xiamenair.com',
        'Origin': 'https://www.xiamenair.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }


    data1 = {
        "ecip": {"shoppingPreference":
                     {"connectionPreference": {"maxConnectionQuantity": 2},
                      "flightPreference":
                          {"cabinCombineMode": "Cabin",
                           "lowestFare": 'false'
                           },
                      "accountCodeSlogan": "", "pricingMode": "Money"
                      },
                 "cabinClasses": ["Economy", "Business", "First"],
                 "passengerCount": 'null',
                 "itineraries": [{
                     "departureDate": date,
                     "origin": {"airport": {"code": departure}},
                     "destination": {"airport": {"code": arrival}}
                 }]
                 },
        "jfCabinFirst": 'false',
        "dOrI": "D",
        "isJCGM": 'false',
        "partner": 'false'
    }

    jdata = json.dumps(data1)
    r = requests.post(url, data=jdata, headers=headers)
    print(r.status_code)

    ptemp = departure + '-' + arrival

    jsdata1 = json.loads(r.text)['result']['egr']['sepa'][ptemp]
    jsdata2 = json.loads(r.text)['result']['egr']['segmentDetail']
    print(len(jsdata1))

    tzurl = 'https://www.xiamenair.com/zh-cn/nticket.html?tripType=OW&orgCodeArr%5B0%5D='+departure+ \
            '&dstCodeArr%5B0%5D='+ arrival + \
            '&orgDateArr%5B0%5D='+date+ \
            '&dstDate=&isInter=false&adtNum=1&chdNum=0&JFCabinFirst=false&acntCd=&mode=Money&partner=false&jcgm=false'

    dict = {}
    count = 0

    print("厦门航空-航班号-出发地-目的地-日期-起飞时间-降落时间-仓型-最低价格")
    for item in jsdata1:
        # print(item)  # 航班号-出发地-目的地-日期
        # print(len(jsdata1[item]))  # 机票数量
        # print(len(jsdata[item]['itemsAll'][item]))
        # print(type(jsdata1[item]['itemsAll'][item]['[CHD1]'][0]))
        # print(type(jsdata1[item]['itemsAll'][item]['[CHD1]'][0][0]))
        # print(jsdata1[item]['itemsAll'][item]['[CHD1]'][0][0]['cabin'])  # 仓型
        cabin = jsdata1[item]['itemsAll'][item]['[CHD1]'][0][0]['cabin']
        # print(jsdata1[item]['itemsAll'][item]['[CHD1]'][0][0]['price']['totalAmount'])  # 最低价格
        price = jsdata1[item]['itemsAll'][item]['[ADT1]'][0][0]['price']['totalAmount']

        # print(jsdata2[item]['arrival'])
        aCityName = jsdata2[item]['arrival']['cityName'] + jsdata2[item]['arrival']['stationName']
        # print(aCityName)
        aTime = jsdata2[item]['arrival']['aircraftScheduledDateTime']
        # print(aTime)

        # print(jsdata2[item]['departure'])
        dCityName = jsdata2[item]['departure']['cityName'] + jsdata2[item]['departure']['stationName']
        # print(dCityName)
        dTime = jsdata2[item]['departure']['aircraftScheduledDateTime']

        # during = datetime.strptime(aTime) - datetime.strptime(dTime)
        # print(during)

        print("厦门航空"+" "+item[:6] + " " + dCityName + " " + aCityName + " " + item[-10:] + " " + dTime + " " + aTime + " " + cabin + " " + str(price) +" "+tzurl)


        dict[str(count)] = {'company':'厦门航空',
                            'flightID': item[:6],
                            'dCityName': dCityName,
                            'aCityName': aCityName,
                            'date': item[-10:],
                            'dTime:': dTime,
                            'aTime': aTime,
                            'cabin': cabin,
                            'price': price,
                            'tzurl': tzurl
                            }
        count += 1

    jsdict = json.dumps(dict)
    return dict