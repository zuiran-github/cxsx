import requests
import json


def getURL(dep, arr, date):
    '''
    :param dep: SHA
    :param arr: TNA
    :param date: 2021-05-06
    :return:
    '''

    # url = 'https://flights.sda.cn/tRtApi/flight/resultSets'
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
        'Referer': 'https://flights.sda.cn/flight/search/sha-tna-210506-1',
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
                "code": "AIR_"+arr+"_CN",
                "context": "LOCATION_ID"
            },
            "origin": {
                "code": "AIR_"+dep+"_CN",
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

    return id





departure = "SHA"
arrival = "TNA"
date = "2021-05-06"
getURL(departure,arrival,date)


