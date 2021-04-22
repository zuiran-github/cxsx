import requests
import json
import time
from django.views.decorators.http import require_http_methods

from django.http import JsonResponse

listfordict = []

def getCityID(cityname):
    '''
    :param cityname: 北京大兴
    :return: 大写城市代码
    '''

    try:
        dict = {'安庆': 'AQG', '阿克苏': 'AKU', '北海': 'BHY', '毕节': 'BFJ', '包头': 'BAV', '北京大兴': 'PKX', '北京首都': 'PEK',
                '常州': 'CZX', '常德': 'CGD', '成都': 'CTU', '池州': 'JUH', '长春': 'CGQ', '重庆': 'CKG', '长沙': 'CSX', '承德': 'CDE',
                '大同': 'DAT', '大连': 'DLC', '敦煌': 'DNH', '大庆': 'DQA', '大理': 'DLU', '恩施': 'ENH', '福州': 'FOC', '贵阳': 'KWE',
                '广州': 'CAN', '固原': 'GYU', '赣州': 'KOW', '桂林': 'KWL', '杭州': 'HGH', '海拉尔': 'HLD', '呼和浩特': 'HET',
                '衡阳': 'HNY', '海口': 'HAK', '汉中': 'HZG', '哈尔滨': 'HRB', '黄山': 'TXN', '邯郸': 'HDG', '合肥': 'HFE', '淮安': 'HIA',
                '九寨': 'JZH', '嘉峪关': 'JGN', '景德镇': 'JDZ', '济宁': 'JNG', '揭阳': 'SWA', '井冈山': 'JGS', '金昌': 'JIC',
                '济南': 'TNA', '昆明': 'KMG', '库尔勒': 'KRL', '喀什': 'KHG', '拉萨': 'LXA', '柳州': 'LZH', '泸州': 'LZO', '陇南': 'LNL',
                '临沂': 'LYI', '连云港': 'LYG', '兰州': 'LHW', '连城': 'LCX', '洛阳': 'LYA', '丽江': 'LJG', '牡丹江': 'MDG',
                '满洲里': 'NZH', '梅州': 'MXZ', '绵阳': 'MIG', '南昌': 'KHN', '南充': 'NAO', '宁波': 'NGB', '南阳': 'NNY', '南京': 'NKG',
                '南通': 'NTG', '南宁': 'NNG', '鄂尔多斯': 'DSN', '攀枝花': 'PZI', '秦皇岛': 'BPE', '衢州': 'JUZ', '琼海': 'BAR',
                '青岛': 'TAO', '泉州': 'JJN', '日照': 'RIZ', '石家庄': 'SJW', '三亚': 'SYX', '三清山': 'SQD', '深圳': 'SZX',
                '沈阳': 'SHE', '上海浦东': 'PVG', '三明': 'SQJ', '松原': 'YSQ', '上海虹桥': 'SHA', '十堰': 'WDS', '唐山': 'TVS',
                '铜仁': 'TEN', '太原': 'TYN', '腾冲': 'TCZ', '台州': 'HYN', '吐鲁番': 'TLQ', '天津': 'TSN', '温州': 'WNZ',
                '武夷山': 'WUS', '无锡': 'WUX', '乌鲁木齐': 'URC', '乌海': 'WUA', '万州': 'WXN', '武汉': 'WUH', '威海': 'WEH',
                '忻州': 'WUT', '西双版纳': 'JHG', '襄阳': 'XFN', '西安': 'XIY', '西昌': 'XIC', '厦门': 'XMN', '兴义': 'ACX',
                '徐州': 'XUZ', '西宁': 'XNN', '伊宁': 'YIN', '义乌': 'YIW', '宜昌': 'YIH', '宜春': 'YIC', '盐城': 'YNZ', '宜宾': 'YBP',
                '银川': 'INC', '扬州': 'YTY', '烟台': 'YNT', '岳阳': 'YYA', '榆林': 'UYN', '运城': 'YCU', '延吉': 'YNJ', '中卫': 'ZHY',
                '湛江': 'ZHA', '张家口': 'ZQZ', '张家界': 'DYG', '遵义新舟': 'ZYI', '遵义茅台': 'WMT', '临汾': 'LFQ', '珠海': 'ZUH',
                '郑州': 'CGO', '扎兰屯': 'NZL', '舟山': 'HSN'}
        cityID = dict[cityname]

    except:
        print('输入城市名称有误')


    return cityID




def xiamen(date, departure, arrival):

    '''
    厦门航空
    :param date: 2021-05-21
    :param departure: 大写代码
    :param arrival: 大写代码
    :return: 列表
    '''

    try:
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
        # print(len(jsdata1))

        tzurl = 'https://www.xiamenair.com/zh-cn/nticket.html?tripType=OW&orgCodeArr%5B0%5D=' + departure + \
                '&dstCodeArr%5B0%5D=' + arrival + \
                '&orgDateArr%5B0%5D=' + date + \
                '&dstDate=&isInter=false&adtNum=1&chdNum=0&JFCabinFirst=false&acntCd=&mode=Money&partner=false&jcgm=false'

        dict = {}
        count = 0
        # listforjson = []

        # print("厦门航空-航班号-出发地-目的地-日期-起飞时间-降落时间-仓型-最低价格")
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

            # print("厦门航空" + " " + item[:6] + " " + dCityName + " " + aCityName + " " + item[
            #                                                                           -10:] + " " + dTime + " " + aTime + " " + cabin + " " + str(
            #     price) + " " + tzurl)

            dict[str(count)] = {'company': '厦门航空',
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

            listfordict.append({'company': '厦门航空',
                                'flightID': item[:6],
                                'dCityName': dCityName,
                                'aCityName': aCityName,
                                'date': item[-10:],
                                'dTime': dTime,
                                'aTime': aTime,
                                'cabin': cabin,
                                'price': price,
                                'tzurl': tzurl
                                })
            count += 1

        # dictlist = {
        #     "data": listfordict
        # }

        # jsdict = json.dumps(dictlist)

        # f2 = open('flight.json', 'w')
        # f2.write(jsdict)
        # f2.close()

        print("厦门航空搜索完成")
    except:
        print("厦门航空报错或未查询到数据")

    return listfordict



def getURL(dep, arr, date):

    '''
    得到山东航空访问数据的ID
    :param dep: SHA
    :param arr: TNA
    :param date: 2021-05-06
    :return:
    '''

    try:
        day = date[2:4] + date[5:7] + date[8:]  # 210506 山东航空传参格式

        url = 'https://flights.sda.cn/tRtApi/flight/resultSets'

        headers = {
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Length': '252',
            'Content-Type': 'application/json',
            'Cookie': 'lang_type=zh_CN; ROUTELOCATID=.LocationAPIServer3; _dx_uzZo5y=863d1c78292767606282e3f7837ae3fb21ae5c897e5ea665255e60b732c8991a442290d1; _dx_app_73360ce3e32b708eb1a2a95602a614fe=607e8b45YfsjYtDOhwbtpyBxlpC4afYRBuoHX3M1; ROUTEAPIID=.tRetailAPISolutionServer2; JSESSIONID=uOuWFPOmlMqUHaJ2Nxw9Lkd1frBAgI5DepOZba47.SCIbeServer58595; _dx_captcha_vid=37DA49AB8B71BCA538E8EA567680DFE7DCA7AFD543EE68C4DD4ACBCE524379D9A2695557D5701685E0D724A1648C2C5EA895290F6C14B7114AA20ABB79CF8FABCB3382DA8E1B9D5816B7C64839E20EFA; OZ_1Y_3072=erefer=-&eurl=https%3A//flights.sda.cn/flight/search/sha-tna-210506-1&etime=1618905983&ctime=1618906979&ltime=1618906967&compid=3072; zh_CN_air_his=sha-tna-210506-1%3Bcsha-tna-210420-1%3Bsha-tna-210506%3Bsha-tna-210506-3%3Bsha-tna-210506-2; OZ_SI_3072=sTime=1618905983&sIndex=39; OZ_1U_3072=vid=v07e8b809665a8.0&ctime=1618906980&ltime=1618906979',
            'Device-Id': 'c91bc55e8f1666137e8240d97374eda4',
            'Host': 'flights.sda.cn',
            'Market-Country-Code': 'CN',
            'Origin': 'https://flights.sda.cn',
            'Pragma': 'no-cache',
            'Referer': 'https://flights.sda.cn/flight/search/' + dep.lower() + '-' + arr.lower() + '-' + day + '-1',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        }

        data = {
            "cabinClass": "ANY",
            "currencyCode": "CNY",
            "bounds": [{
                "departureDate": date,
                "destination": {
                    "code": "AIR_" + arr + "_CN",
                    "context": "LOCATION_ID"
                },
                "origin": {
                    "code": "AIR_" + dep + "_CN",
                    "context": "LOCATION_ID"
                }}],
            "passengerCounts": [{"count": 1, "passengerType": "ADT"}]
        }

        # jsdata = json.dumps(data)

        r = requests.post(url=url, json=data, headers=headers)
        print(r.status_code)
        # print(r.text)

        id = json.loads(r.text)["id"]
        # print(id)

    except:
        print("获取山东航空ID出错")


    return id



def shandong(dep, arr, day1):
    '''
    山东航空
    :param dep: 大写城市代码
    :param arr: 大写城市代码
    :param day1: 2021-05-06
    :return: 列表
    '''


    try:
        day = day1[2:4] + day1[5:7] + day1[8:]  # 210506 山东航空传参格式

        id = getURL(dep, arr, day1)  # 2021-05-06 获取id的日期格式

        url = 'https://flights.sda.cn/tRtApi/flight/resultSets/' + id

        headers = {
            'Host': 'flights.sda.cn',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'Accept-Language': 'zh-CN',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': 'application/json',
            'Market-Country-Code': 'CN',
            'Device-Id': 'd45761eea5aa6d00b1dc8c992a57d365',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            # 'Referer': 'https://flights.sda.cn/flight/search/sha-tna-210506-1',
            'Referer': 'https://flights.sda.cn/flight/search/' + dep.lower() + '-' + arr.lower() + '-' + day + '-1',
            'Accept-Encoding': 'gzip, deflate, br',
            'Cookie': 'lang_type=zh_CN; ROUTELOCATID=.LocationAPIServer3; _dx_uzZo5y=863d1c78292767606282e3f7837ae3fb21ae5c897e5ea665255e60b732c8991a442290d1;'
        }

        # r = requests.post(url=url, data=jsdata, headers=headers)
        r = requests.get(url=url, headers=headers)
        print(r.status_code)
        # print(r.text)

        getprice = json.loads(r.text)['flightOptions']
        getinfo = json.loads(r.text)['flightSegments']
        getcabin = json.loads(r.text)['fareFamilies']

        company = '山东航空'

        # 仓位字典
        dictcabin = {}
        for i in getcabin:
            dictcabin[i['code']] = i['name']
        # print(dictcabin)

        dict = {}
        # listfordict = []
        count = 0
        for i in range(len(getprice)):
            # print(type(getprice[i]))
            # print(getprice[i]['prices'][0]['total']['amount'])
            price = getprice[i]['prices'][0]['total']['amount']  # 价格
            cabin = dictcabin[getprice[i]['prices'][0]['fareFamilyCode']]  # 仓位

            # print(type(getinfo[i]))
            acity = getinfo[i]['arrival']['city']
            atime = getinfo[i]['arrival']['dateTime']
            dcity = getinfo[i]['departure']['city']
            dtime = getinfo[i]['departure']['dateTime']
            flightID = getinfo[i]['marketingAirlineInfo']['airlineCode'] + getinfo[i]['marketingAirlineInfo'][
                'flightNumber']

            date = dtime[:10]

            tzurl = 'https://flights.sda.cn/flight/search/' + dep + '-' + arr + '-' + day

            dict[str(count)] = {'company': company,
                                'flightID': flightID,
                                'dCityName': dcity,
                                'aCityName': acity,
                                'date': date,
                                'dTime:': dtime,
                                'aTime': atime,
                                'cabin': cabin,
                                'price': price,
                                'tzurl': tzurl
                                }
            count += 1

            listfordict.append({'company': company,
                                'flightID': flightID,
                                'dCityName': dcity,
                                'aCityName': acity,
                                'date': date,
                                'dTime:': dtime,
                                'aTime': atime,
                                'cabin': cabin,
                                'price': price,
                                'tzurl': tzurl
                                })

        # print(dict)
        print("山东航空搜索完成")
    except:
        print('山东航空报错或未查询到数据')

    return listfordict

def shenzhen(depcode, arrcode, day):

    '''
    深圳航空
    :param depcode: 大写城市代码
    :param arrcode: 大写城市代码
    :param day: 2021-05-12
    :return: 列表
    '''

    # depcode = getCityID(dep)
    # arrcode = getCityID(arr)

    try:
        cookies = {
            'JSESSIONID': '767A56CBDCCA05C09BC313DBF9016CC0',
            'x-s3-sid': 'S123Xxuxdpu8514515jur6nzj',
            'A_JNID': '50a67a76e465568dc3f661316e74b937082c880a18de0878aa6e8%3B%3BRMKMXU%2FRqsjuyJ1NrTMVpz6QRkqW74WHtVwy7zyRYKr%2BxBTgUWJGIXC7%2FZ6B0QJAFrRBePesFEbhAiD3zNxIWhe%2FrfJTaF%2FPDjFOUXyJZffitQyTEkptEiVESyKpaENzyMy6mHgzaFxlVlAglWKheNsHv5eTJ8EUdU6xWXRdHE3qTlg5YltOHpKQ2uGb%2B8u%2BmYkHzQ6sU%2FeAk8Uh4Oqrn6QWqX7q3FwOmg2pVwC8CXRXZfcVB43RcMG9t%2F8CqsSY2Ug%2BxuxnHSuguNjmOb%2Bjv4PqFZ8axdnZ3IaLvYrA0eHCFjtpFlVkwwOuPJANk3Xqm%2BwawjmityWiGOYlvEE3%2FH2%2F46zGpKkK57uRPC2Rq5FjnDakbcygfVswgqfRM8k2vHG6IzBhWpGaCLzQf%2FObkA%3D%3D',
            'A_SSID': '440a3f432c39eb7b923e5aabecd298d3',
            '_gscu_1739384231': '188399133q88wx13',
            # 'AlteonP': f"BKKzUm9ADgqd9cNJgocdLg{$}",
            'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22178ea60c78d5b2-039e2cc5d09aa6-336a7c08-1296000-178ea60c78eea3%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22178ea60c78d5b2-039e2cc5d09aa6-336a7c08-1296000-178ea60c78eea3%22%7D',
            'x-s3-tid': 'b2a3006eaf0d6c1f4aa97280d210d6b57880c5be:95:b215fccd-a24b-11eb-9343-3cd2e55daed6:ae97f500c0',
            '_gscbrs_1739384231': '1',
            'x-s3-s4e': 'W6kCgewc0bF0RUDv0GCM21wuZCaBZT2092GQwdKAL%2Fcaqq1njR6ya2Fzsh9HLwkZP4LW7ZoAs5D3B9to%2Fhuhtdhl%2Fr4erzygIJ4xwX2RedD0EZbt2hVpdH1ZNNH%2Fug92F8Pz9R1JB2ieJfEvIjZnCzn3BGSiK%2Bf0UjOE%2Fgin36bf4%2FvNq0G3XBIZ%2BiBYO4dGtLLXbtK9NkI%2BbvLCGu1UjCOaVsEz6689GsETy9pjR31bEfxQghWdayQzoAuGsbhZzoB3KL%2FIzgHVTuZMbbxyNr7WOb6k4HqJF6lbnUvael8mL4eM1jsk%2FrSBJX3AQsgObe9%2Fb%2FOGgeEezBiyMK90CI%2F6cHVAPwLab1%2Ff47Wz4w2mxquMyd3Tq4be0j7f4%2FD%2FAXGmzlXhABO9JVu%2BftLmRF230%2FrhrjB23%2Fa6J22u3v3Qi6dNRQCGE8uVKSxfMFKHD6zuwwEJWVtgXTpQoYQvXwPkKBj15WasNPdj5G5rE9rpgQQlo1gsvBM6opA56LNSsvWXJdp4ZSePPJTHfLI9YLIEbltipQXylJhGERq1LyR6v9%2BdO4lPehI9iHJNXcUhNHki1sgOENqXFJuBJ4dcaIDZ%2BHvBpZl%2B%2B2cu75efCHy4dXAh9DTQr7Fanz%2FAObsT86nCcqHRdyPRvqwaGgIMShLOUN7twU52m6VAZMv75PMAVQT268uvkurIBEc4hGk9twD8eb56XbXCNz9q0Aku1kL6PpaqtL%2Bz8Uaw9Uau4osP63DrNWlnm%2BlJRYzR%2FChOL%2FEa2GqmXuUC%2FOKGSqwZsznSJGBztwZuzsozWlUYDd1cuJFUhoYFZklCsaW4c0eN1IMIpeHTimcKcdFkbzfTxwiuP139s6HkVf6WOWZ5aw9iveOy3W6x7apBAlQvbSuHrxxJHhx77Da7ECskC53F2iMEJUUA5k1ddyfM2XLgsZRrjZYbUYc%2BKW6Rd7WVV07W4VKwEIjHznJYH5EJRGgn94fkeSQwfMeIdGtgrQrQUinz3aJH%2FJsz%2BTMGUP0l4zbn3sSsb2a3006eaf0d6c1f4aa97280d210d6b57880c5be:95:b215fccd-a24b-11eb-9343-3cd2e55daed6:ae97f500c0',
            'fromPage': '%7BfromPage%3A%22flightSearch%22%7D',
            'sccode': '%7BsccodeInfo%3A%22%u822A%u73ED%u5217%u8868%u9875%26%u91CD%u65B0%u67E5%u8BE2%22%7D',
            'A_CKPC': 'nS64pPhAXifyseDBfryk89haRaaXXGTbZ29hS7SA5HkoUcl3nvfEyQ%2FhN8jhHDXtXDyuF8weO280MzYqZFw8AMkKzTiWlC3rqxs9mrCp78AuMAoLQTicY8E3Bm4DcOcvLTfxbMPLJ9Iuaf5UpCkD6w%3D%3D',
            '_gscs_1739384231': '18973156o1fdwt18|pv:2',
        }

        headers = {
            'Proxy-Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'http://www.shenzhenair.com',
            'Referer': 'http://www.shenzhenair.com/szair_B2C/flightsearch.action?orgCityCode=SHA&dstCityCode=SZX&hcType=DC&orgCity=%E4%B8%8A%E6%B5%B7%E8%99%B9%E6%A1%A5&dstCity=%E6%B7%B1%E5%9C%B3&orgDate=2021-05-13&dstDate=2021-05-13&easyFlyFlag=0&constId=',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        }

        data = {
            'condition.orgCityCode': depcode,
            'condition.dstCityCode': arrcode,
            'condition.hcType': 'DC',
            'condition.orgDate': day,
            'condition.dstDate': day,
        }

        response = requests.post('http://www.shenzhenair.com/szair_B2C/flightSearch.action', headers=headers,
                                 cookies=cookies, data=data, verify=False)

        print(response.status_code)
        # print(response.text)
        jsdata = json.loads(response.text)['flightSearchResult']
        # print(type(jsdata))

        company = '深圳航空'
        tzurl = 'http://www.shenzhenair.com/szair_B2C/flightsearch.action?' \
                'orgCityCode=' + depcode + \
                '&dstCityCode=' + arrcode + \
                '&hcType=DC&orgCity=%E4%B8%8A%E6%B5%B7%E8%99%B9%E6%A1%A5&dstCity=%E6%B7%B1%E5%9C%B3' \
                '&orgDate=' + day + \
                '&dstDate=' + day + \
                '&easyFlyFlag=0&constId='

        # 仓位
        cabindict = jsdata['classTypes']
        # print(type(cabindict))
        # print(cabindict)

        flightinfo = jsdata['flightInfoList']

        date = jsdata['departureTime']

        dict = {}
        count = 0

        # listfordict = []

        for item in flightinfo:
            # print(type(item))
            flightID = item['flightNo']
            # print(flightID)

            dcity = item['orgCityCH']
            dtime = date +' '+ item['orgTime']+':00'
            acity = item['dstCityCH']
            atime = date +' '+ item['dstTime']+':00'

            pricelist = item['classInfoList']
            i = len(pricelist)
            price = pricelist[i - 1]['classPrice']
            cabin = cabindict[pricelist[i - 1]['classType']]

            dict[count] = {
                'company': company,
                'flightID': flightID,
                'dCityName': dcity,
                'aCityName': acity,
                'date': date,
                'dTime': dtime,
                'aTime': atime,
                'cabin': cabin,
                'price': price,
                'tzurl': tzurl,
            }
            count += 1

            listfordict.append({
                'company': company,
                'flightID': flightID,
                'dCityName': dcity,
                'aCityName': acity,
                'date': date,
                'dTime': dtime,
                'aTime': atime,
                'cabin': cabin,
                'price': price,
                'tzurl': tzurl,
            })

        # print(dict)
        print("深圳航空搜索完成")

    except:
        print('深圳航空报错或未查询到数据')


    return listfordict




def donghang(dep, arr, day):
    '''
    吉祥航空&东方航空
    :param dep: 大写城市代码
    :param arr: 大写城市代码
    :param day: 2021-05-16
    :return: 列表
    '''

    try:
        url = 'http://www.juneyaoair.com/UnitOrderWebAPI/Book/QueryFlightFareNew?'

        headers = {
            'Host': 'www.juneyaoair.com',
            'Proxy-Connection': 'keep-alive',
            'Content-Length': '324',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'http://www.juneyaoair.com',
            'Referer': 'http://www.juneyaoair.com/pages/Flight/flight.aspx?flightType=OW'
                       '&sendCity=%E5%8C%97%E4%BA%AC'
                       '&sendCode=PEK'
                       '&arrCity=%E4%B8%8A%E6%B5%B7'
                       '&arrCode=SHA'
                       '&directType=N'
                       '&tripType=D'
                       '&departureDate=2021-05-12'
                       '&returnDate=2021-05-12',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cookie': 'ASP.NET_SessionId=0zymuwtk3sm3jegrhdjdmhq0;'
        }

        data = "flightType=OW" \
               "&tripType=D" \
               "&directType=D" \
               "&departureDate=" + day + \
               "&sendCode=" + dep + \
               "&arrCode=" + arr + \
               "&returnDate="

        r = requests.post(url=url, data=data, headers=headers)
        print(r.status_code)
        # print(type(r.text))
        jsdata = json.loads(r.text)['FlightInfoList']
        # print(type(jsdata))

        companydict = {
            "HO": "吉祥航空",
            "MU": "东方航空"
        }

        tzurl = 'http://www.juneyaoair.com/pages/Flight/flight.aspx?' \
                'flightType=OW' \
                '&sendCity=%E4%B8%8A%E6%B5%B7' \
                '&sendCode=' + dep + \
                '&arrCity=%E8%A5%BF%E5%AE%89' \
                '&arrCode=' + arr + \
                '&directType=N' \
                '&tripType=D' \
                '&departureDate=' + day + \
                '&returnDate='

        dict = {}
        count = 0
        # listfordict = []
        for item in jsdata:
            # print(type(item))
            # print(item)

            acity = item['ArrCityName']
            atime = item['ArrDateTime']+':00'
            dcity = item['DepCityName']
            dtime = item['DepDateTime']+':00'

            date = item['FlightDate']

            flightID = item['CarrierNo']

            company = companydict[flightID[:2]]

            if len(item['CabinFareList']) > 1:
                price = int(item['CabinFareList'][1]['PriceValue']) + int(item['CabinFareList'][1]['TaxAmount'])

                cabin = item['CabinFareList'][1]['PriceShowType']

            else:
                price = int(item['CabinFareList'][0]['PriceValue']) + int(item['CabinFareList'][0]['TaxAmount'])

                cabin = item['CabinFareList'][0]['PriceShowType']

            dict[str(count)] = {'company': company,
                                'flightID': flightID,
                                'dCityName': dcity,
                                'aCityName': acity,
                                'date': date,
                                'dTime': dtime,
                                'aTime': atime,
                                'cabin': cabin,
                                'price': price,
                                'tzurl': tzurl
                                }
            count += 1

            listfordict.append({'company': company,
                                'flightID': flightID,
                                'dCityName': dcity,
                                'aCityName': acity,
                                'date': date,
                                'dTime': dtime,
                                'aTime': atime,
                                'cabin': cabin,
                                'price': price,
                                'tzurl': tzurl
                                })

        # print(dict)
        # print(listfordict)
        print("吉祥航空搜索完成")
        print("东方航空搜索完成")
    except:
        print("吉祥航空东方航空报错或未查询到数据")

    return listfordict




def chunqiu(dep, arr, day):
    '''
    春秋航空
    :param dep: 城市中文名
    :param arr: 城市中文名
    :param day: 2021-05-21
    :return: 列表
    '''

    try:
        cookies = {
            '_os': 'ff08ef99dd88107fb19f42ac0fe919bd',
            'RiskifiedToken': '3c62959fd52445fbad3ba59dd4ff3a6e',
            'IsShowTaxprice': 'false',
            'smidV2': '20210419213103b225054a49c795c51a67c980e02b9efc00554d7df5b0b1390',
            '_ga': 'GA1.2.1860291403.1618839067',
            'gr_user_id': '7f4c661e-8c82-4898-b1ea-b3844d08b42b',
            's6': '5a1d7bfb4c8a49168cd412b0a220ca6b',
            'rskxRunCookie': '0',
            'rCookie': '7jro1r0eij9xswur5jsecnknomzf9g',
            'acw_tc': '2f624a5f16189889250918187e7047723abe3fa830ff59c718a4e17f6c4198',
            'c3': 'link.csdn.net',
            'c4': '',
            's7': 'https://link.csdn.net/?target=https%3A%2F%2Fflights.ch.com%2FDOY-SHA.html%3FDeparture%3D%25E4%25B8%259C%25E8%2590%25A5%26Arrival%3D%25E4%25B8%258A%25E6%25B5%25B7%26FDate%3D2021-04-20%26DepartCityCode%3DDOY%26ArriveCityCode%3D%26IsSearchDepAirport%3Dfalse%26IsSearchArrAirport%3Dfalse%26isOnlyZf%3Dfalse%26ANum%3D1%26CNum%3D0%26INum%3D0%26IfRet%3Dfalse%26SType%3D0%26MType%3D0%26IsNew%3D1',
            'hasProcessIP': '1',
            'g_refresh': '0',
            'Hm_lvt_f6066c7da67b0ae5719a9fa8c6e004a8': '1618839066,1618901878,1618988929',
            'Hm_lpvt_f6066c7da67b0ae5719a9fa8c6e004a8': '1618988929',
            'Qs_lvt_100645': '1618839065%2C1618901877%2C1618988929',
            'Qs_pv_100645': '2673840618400725000%2C2648938634253314000%2C337083941064597500%2C2995469463255247000%2C2680091118663421400',
            'mediav': '%7B%22eid%22%3A%22194066%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22hdN%C2%B27%23X.8n%24JC%5E%5Et)J%22%2C%22ctn%22%3A%22%22%2C%22vvid%22%3A%22hdN%25b27%23X.8n%24JC%5E%5Et)J%22%2C%22_mvnf%22%3A1%2C%22_mvctn%22%3A0%2C%22_mvck%22%3A0%2C%22_refnf%22%3A0%7D',
            'lastRskxRun': '1618988929568',
            's4': 'dd2468236b264bff93ff08979e4364f6',
            's5': '1',
            's1': 'Mac',
            's2': 'WEB',
            's3': 'zh-cn',
            '9683d26dac59f3e8_gr_session_id': '9ef9e5fa-7e3f-488c-b319-ddffd34c5d55',
            '9683d26dac59f3e8_gr_session_id_9ef9e5fa-7e3f-488c-b319-ddffd34c5d55': 'true',
            '_gid': 'GA1.2.877059680.1618988931',
            '_gat': '1',
            'SearchHis': 'zh-cn%26KMG%26%u6606%u660E%26SHA%26%u4E0A%u6D77%262021-05-12%26%26%26%26false%26false',
            'shumei_device_id': 'WHJMrwNw1k%2FE3AgU0jRKQ7x76m60CtwJkTCp%2FhDhfaeVsBk5T0WV4K2q13qM%2BWSz%2B%2Bhxt8158Y5X%2Ba18pqoFXZDMtiHLrSepOCFqixxb%2FTFet6u1MerOs5IaHMOKM8qKVBJ7HANruhDjgssVEtOEyiJGebD4P9188MdzVDzvFXj9%2FyCKqUzHii%2B%2Fuin5U7osgzbQCr3JAl58WVhtziRydZ6DEi0ba5KFfsuCOzGbvX7zcLjlxvuKHBaTkjp7Yczxq1487582755342',
        }

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'Accept': '*/*',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://flights.ch.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://flights.ch.com/KMG-SHA.html?Departure=%E6%98%86%E6%98%8E&Arrival=%E4%B8%8A%E6%B5%B7&FDate=2021-05-12&RetDate=2021-04-22&DepartCityCode=&ArriveCityCode=&IsSearchDepAirport=false&IsSearchArrAirport=false&isOnlyZf=false&ANum=1&CNum=0&INum=0&MType=0&IfRet=false&SType=012&isBg=false&IsJC=false&IsNew=1',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        }

        data = {
            'Active9s': '',
            'IsJC': 'false',
            'IsShowTaxprice': 'false',
            'Currency': '0',
            'SType': '0',
            'Departure': dep,  # '\u6606\u660E',
            'Arrival': arr,  # '\u4E0A\u6D77',
            'DepartureDate': day,
            'ReturnDate': 'null',
            'IsIJFlight': 'false',
            'IsBg': 'false',
            'IsEmployee': 'false',
            'IsLittleGroupFlight': 'false',
            'SeatsNum': '1',
            'ActId': '0',
            'IfRet': 'false',
            'IsUM': 'false',
            'CabinActId': 'null',
            'SpecTravTypeId': '',
            'IsContains9CAndIJ': 'false',
            'DepCityCode': '',
            'ArrCityCode': '',
            'DepAirportCode': '',
            'ArrAirportCode': '',
            'IsSearchDepAirport': 'false',
            'IsSearchArrAirport': 'false',
            'isdisplayold': 'false'
        }

        response = requests.post('https://flights.ch.com/Flights/SearchByTime', headers=headers, cookies=cookies,
                                 data=data)
        print(response.status_code)

        cabindict = {
            "5": "会员专享座",
            "3": "经济座",
            "0": "商务经济座"
        }

        jsdata = json.loads(response.text)['Route']

        if dep == '北京':
            depcode = 'PEK'
        elif dep == '上海':
            depcode = 'SHA'
        else:
            depcode = getCityID(dep)

        if arr == '北京':
            arrcode = "PEK"
        elif arr == '上海':
            arrcode = 'SHA'
        else:
            arrcode = getCityID(arr)

        tzurl = 'https://flights.ch.com/' + depcode + '-' + arrcode + '.html?' \
                                                                      'Departure=%E6%98%86%E6%98%8E' \
                                                                      '&Arrival=%E4%B8%8A%E6%B5%B7' \
                                                                      '&FDate=' + day + \
                '&RetDate=2021-04-22' \
                '&DepartCityCode=' \
                '&ArriveCityCode=' \
                '&IsSearchDepAirport=false' \
                '&IsSearchArrAirport=false' \
                '&isOnlyZf=false' \
                '&ANum=1' \
                '&CNum=0' \
                '&INum=0' \
                '&MType=0' \
                '&IfRet=false' \
                '&SType=012' \
                '&isBg=false' \
                '&IsJC=false' \
                '&IsNew=1'

        dict = {}
        count = 0
        # listfordict = []

        for item in jsdata:
            acity = item[0]['Arrival']
            atime = item[0]['ArrivalTimeBJ']
            dcity = item[0]['Departure']
            dtime = item[0]['DepartureTimeBJ']

            company = item[0]['CompanyName']
            date = item[0]['FlightDateBJ']

            flightID = item[0]['No']

            price = int(item[0]['MinCabinPrice']) + int(item[0]['RouteTotalTax'])

            cabin = cabindict[str(item[0]['MinCabinLevel'])]

            dict[str(count)] = {'company': company,
                                'flightID': flightID,
                                'dCityName': dcity,
                                'aCityName': acity,
                                'date': date,
                                'dTime:': dtime,
                                'aTime': atime,
                                'cabin': cabin,
                                'price': price,
                                'tzurl': tzurl
                                }
            count += 1

            listfordict.append({'company': company,
                                'flightID': flightID,
                                'dCityName': dcity,
                                'aCityName': acity,
                                'date': date,
                                'dTime:': dtime,
                                'aTime': atime,
                                'cabin': cabin,
                                'price': price,
                                'tzurl': tzurl
                                })
        # print(dict)
        print("春秋航空搜索完成")
    except:
        print("春秋航空报错或未查询到数据")


    return listfordict


def nanhang(dep, arr, dayBZ):

    '''
    南方航空查询机票
    :param dep: 大写城市代码
    :param arr: 大写城市代码
    :param day: 2021-05-06
    :return: 列表
    '''

    try:
        day = dayBZ[:4] + dayBZ[5:7] + dayBZ[8:]  # 南方航空传参要求20210505

        cookies = {
            'JSESSIONID': 'F86101DAA3B76D734D8E0660284E73D3',
            'likev_user_id': '286b9ea3-071b-4b9a-82c2-49b196d21373',
            '_gscu_422057653': '14841486g9gpq115',
            '_gcl_au': '1.1.1434185319.1614841509',
            'sid': 'b59095d034474eaea6e83cf60390dc87',
            'language': 'zh_CN',
            'last_session_stm_8mrmut7r76ntg21b': '1618996887244',
            'likev_session_id_8mrmut7r76ntg21b': '87ebea95-d4cd-4878-de64-ede1c2364c42',
            'last_session_id_8mrmut7r76ntg21b': '87ebea95-d4cd-4878-de64-ede1c2364c42',
            '_gscbrs_422057653': '1',
            'acw_tc': 'ac11000116189968870303046e00ee9035de15d1faa194db5c39af5d30f751',
            'temp_zh': 'cou%3D2%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-05-05%3B%E5%8D%97%E4%BA%AC-%E6%AD%A6%E6%B1%89%3B1%2C0%2C0%3B00%3B%26cou%3D3%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-06-15%3B%E5%8C%97%E4%BA%AC-%E4%B8%8A%E6%B5%B7%3B1%2C0%2C0%3B00%3B%26cou%3D4%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-05-20%3B%E5%8C%97%E4%BA%AC-%E4%B8%8A%E6%B5%B7%3B1%2C0%2C0%3B00%3B%26cou%3D5%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-05-20%3B%E5%8C%97%E4%BA%AC-%E4%B8%8A%E6%B5%B7%3B1%2C0%2C0%3B00%3B%26cou%3D5%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-05-21%3B%E5%8C%97%E4%BA%AC-%E4%B8%8A%E6%B5%B7%3B1%2C0%2C0%3B00%3B%26',
            'WT.al_flight': 'WT.al_hctype(S)%3AWT.al_adultnum(1)%3AWT.al_childnum(0)%3AWT.al_infantnum(0)%3AWT.al_orgcity1(BJS)%3AWT.al_dstcity1(SHA)%3AWT.al_orgdate1(2021-05-21)',
            'ticketBoolingSearch': '%7B%22segType%22%3A%22S%22%2C%22adultNum%22%3A%221%22%2C%22childNum%22%3A%220%22%2C%22infantNum%22%3A%220%22%2C%22citys%22%3A%5B%7B%22id%22%3A%22single-formCity%22%2C%22value%22%3A%22%E5%8C%97%E4%BA%AC%22%7D%2C%7B%22id%22%3A%22single-formCityCode%22%2C%22value%22%3A%22BJS%22%7D%2C%7B%22id%22%3A%22isdepair%22%2C%22value%22%3Afalse%7D%2C%7B%22id%22%3A%22single-toCity%22%2C%22value%22%3A%22%E4%B8%8A%E6%B5%B7%22%7D%2C%7B%22id%22%3A%22single-toCityCode%22%2C%22value%22%3A%22SHA%22%7D%2C%7B%22id%22%3A%22isarrair%22%2C%22value%22%3Afalse%7D%5D%2C%22dates%22%3A%5B%7B%22id%22%3A%22single-formCalender%22%2C%22value%22%3A%222021-05-21%22%2C%22minDate%22%3A%22%2B0d%22%7D%5D%7D',
            'WT-FPC': 'id=222.175.103.33-2839966592.30871748:lv=1618996898914:ss=1618996887237:fs=1614841486574:pn=2:vn=6',
            'likev_session_etm_8mrmut7r76ntg21b': '1618996898919',
            '_gscs_422057653': '18996887ehy4sb99|pv:2',
        }

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'application/json',
            'Origin': 'https://b2c.csair.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?t=S&c1=BJS&c2=SHA&d1=2021-05-21&at=1&ct=0&it=0&b1=PEK-PKX&b2=SHA-PVG',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        }

        data = '{' \
               '"depCity":"' + dep + '",' \
                                     '"arrCity":"' + arr + '",' \
                '"flightDate":"' + day + '",' \
                                         '"adultNum":"1",' \
                                                                                    '"childNum":"0",' \
                                                                                    '"infantNum":"0",' \
                                                                                    '"cabinOrder":"0",' \
                                                                                    '"airLine":1,' \
                                                                                    '"flyType":0,' \
                                                                                    '"international":"0",' \
                                                                                    '"action":"0",' \
                                                                                    '"segType":"1",' \
                                                                                    '"cache":0,' \
                                                                                    '"preUrl":"",' \
                                                                                    '"isMember":""}'

        response = requests.post('https://b2c.csair.com/portal/flight/direct/query', headers=headers, cookies=cookies,
                                 data=data)

        print(response.status_code)

        jsdata = json.loads(response.text)['data']['segment'][0]

        # if getCityID(json.loads(response.text)['data']['citys'][1]['zhName']) == arr:
        #     acity = json.loads(response.text)['data']['citys'][1]['zhName']
        #     dcity = json.loads(response.text)['data']['citys'][0]['zhName']
        # else:
        #     acity = json.loads(response.text)['data']['citys'][0]['zhName']
        #     dcity = json.loads(response.text)['data']['citys'][1]['zhName']
        for i in json.loads(response.text)['data']['citys']:
            if getCityID(i['zhName']) == dep:
                dcity = i['zhName']
            if getCityID(i['zhName']) == arr:
                acity = i['zhName']

        # list = []
        company = '南方航空'

        tzurl1 = 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?' \
                 't=S' \
                 '&c1=BJS' \
                 '&c2=SHA' \
                 '&d1=' + dayBZ + \
                 '&at=1' \
                 '&ct=0' \
                 '&it=0' \
                 '&b1=PEK-PKX' \
                 '&b2=SHA-PVG'

        tzurl2 = 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?' \
                 't=S' \
                 '&c1=' + dep + \
                 '&c2=' + arr + \
                 '&d1=' + dayBZ + \
                 '&at=1' \
                 '&ct=0' \
                 '&it=0' \
                 '&b1=' + dep + \
                 '&b2=' + arr

        tzurl3 = 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?' \
                 't=S' \
                 '&c1=SHA' \
                 '&c2=BJS' \
                 '&d1=' + dayBZ + \
                 '&at=1' \
                 '&ct=0' \
                 '&it=0' \
                 '&b1=SHA-PVG' \
                 '&b2=PEK-PKX'

        tzurl4 = 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?' \
                 't=S' \
                 '&c1=BJS' \
                 '&c2=' + arr + \
                 '&d1=' + dayBZ + \
                 '&at=1' \
                 '&ct=0' \
                 '&it=0' \
                 '&b1=PEK-PKX' \
                 '&b2=' + arr

        tzurl5 = 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?' \
                 't=S' \
                 '&c1=SHA' \
                 '&c2=' + arr + \
                 '&d1=' + dayBZ + \
                 '&at=1' \
                 '&ct=0' \
                 '&it=0' \
                 '&b1=SHA-PVG' \
                 '&b2=' + arr

        tzurl6 = 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?' \
                 't=S' \
                 '&c1=' + dep + \
                 '&c2=SHA' \
                 '&d1=' + dayBZ + \
                 '&at=1' \
                 '&ct=0' \
                 '&it=0' \
                 '&b1=' + dep + \
                 '&b2=SHA-PVG'

        tzurl7 = 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?' \
                 't=S' \
                 '&c1=' + dep + \
                 '&c2=BJS' \
                 '&d1=' + dayBZ + \
                 '&at=1' \
                 '&ct=0' \
                 '&it=0' \
                 '&b1=' + dep + \
                 '&b2=PEK-PKX'

        if (dep == 'PEK' or dep == 'PKX') and (arr == 'SHA' or arr == 'PVG'):
            tzurl = tzurl1
        elif (dep == 'SHA' or dep == 'PVG') and (arr == 'PEK' or arr == 'PKX'):
            tzurl = tzurl3
        elif dep == 'PEK' or dep == 'PKX':
            tzurl = tzurl4
        elif dep == 'SHA' or dep == 'PVG':
            tzurl = tzurl5
        elif arr == 'SHA' or arr == 'PVG':
            tzurl = tzurl6
        elif arr == 'PEK' or arr == 'PKX':
            tzurl = tzurl7
        else:
            tzurl = tzurl2

        info = jsdata['dateFlight']['flight']
        for i in info:
            date = i['arrDate']
            flightID = i['flightNo']

            atime = dayBZ + ' ' + i['arrTime'][:2] + ':' + i['arrTime'][2:] +':00'
            dtime = dayBZ + ' ' + i['depTime'][:2] + ':' + i['depTime'][2:] +':00'
            # print(atime)

            cabin = i['cabin'][len(i['cabin']) - 1]['adultFareBasis']
            price = i['cabin'][len(i['cabin']) - 1]['adultPrice']

            listfordict.append({
                'company': company,
                'flightID': flightID,
                'dCityName': dcity,
                'aCityName': acity,
                'date': date,
                'dTime': dtime,
                'aTime': atime,
                'cabin': cabin,
                'price': price,
                'tzurl': tzurl
                         })

        print("南方航空搜索完成")
    except:
        print("南方航空报错或未查询到数据")

    return listfordict

def trans_format(time_string, from_format, to_format='%Y.%m.%d %H:%M:%S'):
    """
    @note 时间格式转化
    :param time_string:
    :param from_format:
    :param to_format:
    :return:
    """
    time_struct = time.strptime(time_string,from_format)
    times = time.strftime(to_format, time_struct)
    return times
# depcityname = '广州'
# arrcityname = '南京'
# day = '2021-05-21'
#
# depcode = getCityID(depcityname)
# arrcode = getCityID(arrcityname)
#
# xiamenr = []
# shandongr = []
# shenzhenr = []
# donghangr = []
# chunqiur = []
# nanhangr = []
#
# xiamenr = xiamen(day, depcode, arrcode)
# shandongr = shandong(depcode, arrcode, day)
# shenzhenr = shenzhen(depcode, arrcode, day)
# donghangr = donghang(depcode, arrcode, day)
# chunqiur = chunqiu(depcityname, arrcityname, day)
# nanhangr = nanhang(depcode, arrcode, day)
#
# print(listfordict)

@require_http_methods(["GET"])
def allsearch(request):
    response = {}
    global listfordict
    listfordict = []
    depcityname = request.GET.get('departure')  # '北京大兴'
    arrcityname = request.GET.get('destination')  # '广州'
    day = trans_format(request.GET.get('goDate')[:15], '%a %b %d %Y', '%Y-%m-%d')[:10]  # '2021-05-21'

    depcode = getCityID(depcityname)
    arrcode = getCityID(arrcityname)

    xiamen(day, depcode, arrcode)
    shandong(depcode, arrcode, day)
    shenzhen(depcode, arrcode, day)
    donghang(depcode, arrcode, day)
    chunqiu(depcityname, arrcityname, day)
    nanhang(depcode, arrcode, day)

    print(listfordict)
    response = {"data" : listfordict}

    return JsonResponse(response)

# allsearch()