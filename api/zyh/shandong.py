import requests
import json


def getURL(dep, arr, date):
    '''
    :param dep: SHA
    :param arr: TNA
    :param date: 2021-05-06
    :return:
    '''


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
        'Referer': 'https://flights.sda.cn/flight/search/' + dep.lower() + '-' + arr.lower() + '-210506-1',
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
    print(r.text)

    id = json.loads(r.text)["id"]
    # print(id)

    return id


def shandong(dep, arr, day, id):

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
        'Referer': 'https://flights.sda.cn/flight/search/sha-tna-210506-1',
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

    print(dict)


def getCityID(cityname):
    '''
    :param cityname:
    :return: 大写
    '''
    dict = {'安庆': 'AQG', '阿克苏': 'AKU', '北海': 'BHY', '毕节': 'BFJ', '包头': 'BAV', '北京大兴': 'PKX', '北京首都': 'PEK', '常州': 'CZX', '常德': 'CGD', '成都': 'CTU', '池州': 'JUH', '长春': 'CGQ', '重庆': 'CKG', '长沙': 'CSX', '承德': 'CDE', '大同': 'DAT', '大连': 'DLC', '敦煌': 'DNH', '大庆': 'DQA', '大理': 'DLU', '恩施': 'ENH', '福州': 'FOC', '贵阳': 'KWE', '广州': 'CAN', '固原': 'GYU', '赣州': 'KOW', '桂林': 'KWL', '杭州': 'HGH', '海拉尔': 'HLD', '呼和浩特': 'HET', '衡阳': 'HNY', '海口': 'HAK', '汉中': 'HZG', '哈尔滨': 'HRB', '黄山': 'TXN', '邯郸': 'HDG', '合肥': 'HFE', '淮安': 'HIA', '九寨': 'JZH', '嘉峪关': 'JGN', '景德镇': 'JDZ', '济宁': 'JNG', '揭阳': 'SWA', '井冈山': 'JGS', '金昌': 'JIC', '济南': 'TNA', '昆明': 'KMG', '库尔勒': 'KRL', '喀什': 'KHG', '拉萨': 'LXA', '柳州': 'LZH', '泸州': 'LZO', '陇南': 'LNL', '临沂': 'LYI', '连云港': 'LYG', '兰州': 'LHW', '连城': 'LCX', '洛阳': 'LYA', '丽江': 'LJG', '牡丹江': 'MDG', '满洲里': 'NZH', '梅州': 'MXZ', '绵阳': 'MIG', '南昌': 'KHN', '南充': 'NAO', '宁波': 'NGB', '南阳': 'NNY', '南京': 'NKG', '南通': 'NTG', '南宁': 'NNG', '鄂尔多斯': 'DSN', '攀枝花': 'PZI', '秦皇岛': 'BPE', '衢州': 'JUZ', '琼海': 'BAR', '青岛': 'TAO', '泉州': 'JJN', '日照': 'RIZ', '石家庄': 'SJW', '三亚': 'SYX', '三清山': 'SQD', '深圳': 'SZX', '沈阳': 'SHE', '上海浦东': 'PVG', '三明': 'SQJ', '松原': 'YSQ', '上海虹桥': 'SHA', '十堰': 'WDS', '唐山': 'TVS', '铜仁': 'TEN', '太原': 'TYN', '腾冲': 'TCZ', '台州': 'HYN', '吐鲁番': 'TLQ', '天津': 'TSN', '温州': 'WNZ', '武夷山': 'WUS', '无锡': 'WUX', '乌鲁木齐': 'URC', '乌海': 'WUA', '万州': 'WXN', '武汉': 'WUH', '威海': 'WEH', '忻州': 'WUT', '西双版纳': 'JHG', '襄阳': 'XFN', '西安': 'XIY', '西昌': 'XIC', '厦门': 'XMN', '兴义': 'ACX', '徐州': 'XUZ', '西宁': 'XNN', '伊宁': 'YIN', '义乌': 'YIW', '宜昌': 'YIH', '宜春': 'YIC', '盐城': 'YNZ', '宜宾': 'YBP', '银川': 'INC', '扬州': 'YTY', '烟台': 'YNT', '岳阳': 'YYA', '榆林': 'UYN', '运城': 'YCU', '延吉': 'YNJ', '中卫': 'ZHY', '湛江': 'ZHA', '张家口': 'ZQZ', '张家界': 'DYG', '遵义新舟': 'ZYI', '遵义茅台': 'WMT', '临汾': 'LFQ', '珠海': 'ZUH', '郑州': 'CGO', '扎兰屯': 'NZL', '舟山': 'HSN'}
    cityID = dict[cityname]
    return cityID


departure = getCityID("上海虹桥")
arrival = getCityID("济南")
dateforurl = '2021-06-06'
id = getURL(departure, arrival, dateforurl)

departurel = departure.lower()
arrivall = arrival.lower()
dayl = '210506'
shandong(departurel, arrivall, dayl, id)
