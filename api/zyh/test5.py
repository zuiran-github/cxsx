import requests
import json

listfordict = []
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
        print(id)

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


    day = day1[2:4] + day1[5:7] + day1[8:]  # 210506 山东航空传参格式

    id = getURL(dep, arr, day1)  # 2021-05-06 获取id的日期格式
    url = 'https://flights.sda.cn/tRtApi/flight/resultSets/' + id

    cookies = {
        'lang_type': 'zh_CN',
        '_dx_uzZo5y': '863d1c78292767606282e3f7837ae3fb21ae5c897e5ea665255e60b732c8991a442290d1',
        'zh_CN_air_his': 'sha-tna-210506-1%3Bsha-tna-210506%3Bsha-tna-210506-3%3Bsha-tna-210506-2',
        '_dx_app_73360ce3e32b708eb1a2a95602a614fe': '607fde150H8s6qlHY44u96kkN8UDeYq8AKXAsfD1',
        '_dx_captcha_vid': '87413C8D1C3B02ECA2149A499FB09F3D128D34A6655FDE7B8017F3959AB9D2CA6ECEF684BF4ACAB7CABEB29AD452B139DBDEA4DBE50B4FCECC33E2AE63F1F25E81112FE6A177B4030AE202363A20172C',
        'ROUTELOCATID': '.LocationAPIServer2',
        'ROUTEAPIID': '.tRetailAPISolutionServer20',
        'JSESSIONID': 'iWxb81iFiQKmPGXIeMdws9XK-etuc0fww948mlxj.SCIbeServer58589',
        'OZ_SI_3072': 'sTime=1619054352&sIndex=5',
        'OZ_1U_3072': 'vid=v07e8b809665a8.0&ctime=1619054386&ltime=1619054385',
        'OZ_1Y_3072': 'erefer=https%3A//link.csdn.net/%3Ftarget%3Dhttps%253A%252F%252Fflights.sda.cn%252Fflight%252Fsearch%252Fcsha-tna-210420-1&eurl=https%3A//flights.sda.cn/flight/search/csha-tna-210420-1&etime=1619054352&ctime=1619054386&ltime=1619054385&compid=3072',
    }

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'Accept-Language': 'zh-CN',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'Accept': 'application/json',
        'Market-Country-Code': 'CN',
        'Device-Id': 'e66002a234eab777f887055413633ec7',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://flights.sda.cn/flight/search/sha-tna-210506-1',
    }

    # r = requests.post(url=url, data=jsdata, headers=headers)
    r = requests.get(url=url, headers=headers, cookies=cookies)
    print(r.status_code)
    print(r.text)

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

shandong('PKX', 'SHA', '2021-05-20')

#
# import requests
#
# cookies = {
#     'lang_type': 'zh_CN',
#     '_dx_uzZo5y': '863d1c78292767606282e3f7837ae3fb21ae5c897e5ea665255e60b732c8991a442290d1',
#     'zh_CN_air_his': 'sha-tna-210506-1%3Bsha-tna-210506%3Bsha-tna-210506-3%3Bsha-tna-210506-2',
#     '_dx_app_73360ce3e32b708eb1a2a95602a614fe': '607fde150H8s6qlHY44u96kkN8UDeYq8AKXAsfD1',
#     '_dx_captcha_vid': '87413C8D1C3B02ECA2149A499FB09F3D128D34A6655FDE7B8017F3959AB9D2CA6ECEF684BF4ACAB7CABEB29AD452B139DBDEA4DBE50B4FCECC33E2AE63F1F25E81112FE6A177B4030AE202363A20172C',
#     'ROUTELOCATID': '.LocationAPIServer2',
#     'ROUTEAPIID': '.tRetailAPISolutionServer20',
#     'JSESSIONID': 'iWxb81iFiQKmPGXIeMdws9XK-etuc0fww948mlxj.SCIbeServer58589',
#     'OZ_SI_3072': 'sTime=1619054352&sIndex=5',
#     'OZ_1U_3072': 'vid=v07e8b809665a8.0&ctime=1619054386&ltime=1619054385',
#     'OZ_1Y_3072': 'erefer=https%3A//link.csdn.net/%3Ftarget%3Dhttps%253A%252F%252Fflights.sda.cn%252Fflight%252Fsearch%252Fcsha-tna-210420-1&eurl=https%3A//flights.sda.cn/flight/search/csha-tna-210420-1&etime=1619054352&ctime=1619054386&ltime=1619054385&compid=3072',
# }
#
# headers = {
#     'Connection': 'keep-alive',
#     'Pragma': 'no-cache',
#     'Cache-Control': 'no-cache',
#     'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
#     'Accept-Language': 'zh-CN',
#     'sec-ch-ua-mobile': '?0',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
#     'Accept': 'application/json',
#     'Market-Country-Code': 'CN',
#     'Device-Id': 'e66002a234eab777f887055413633ec7',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Dest': 'empty',
#     'Referer': 'https://flights.sda.cn/flight/search/sha-tna-210506-1',
# }
#
# response = requests.get('https://flights.sda.cn/tRtApi/flight/resultSets/1ca4b32b-edb2-48c1-bfc8-47341afd3ee1', headers=headers, cookies=cookies)
# print(response.text)
