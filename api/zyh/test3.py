import requests
import json


url = 'https://flights.sda.cn/tRtApi/flight/resultSets/99bd2d6d-094e-42f5-8953-15cb6a12042b'


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

    tzurl = 'https://flights.sda.cn/flight/search/' #+ dep + '-' + arr + '-' + day

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








