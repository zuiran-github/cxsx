import requests
import json


def chunqiu(dep, arr, day):
    '''
    春秋航空
    :param dep: 城市中文名
    :param arr: 大写城市代码
    :param day: 2021-05-21
    :return: 列表
    '''

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

    response = requests.post('https://flights.ch.com/Flights/SearchByTime', headers=headers, cookies=cookies, data=data)
    print(response.status_code)

    cabindict = {
        "5": "会员专享座",
        "3": "经济座",
        "0": "商务经济座"
    }

    jsdata = json.loads(response.text)['Route']

    tzurl = 'https://flights.ch.com/'+dep+'-'+arr+'.html?' \
            'Departure=%E6%98%86%E6%98%8E' \
            '&Arrival=%E4%B8%8A%E6%B5%B7' \
            '&FDate='+day+ \
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
    listfordict = []

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
    return listfordict


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
  'Departure': '广州',#'\u6606\u660E',
  'Arrival': '上海',#'\u4E0A\u6D77',
  'DepartureDate': '2021-05-12',
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

response = requests.post('https://flights.ch.com/Flights/SearchByTime', headers=headers, cookies=cookies, data=data)
print(response.status_code)


cabindict = {
    "5": "会员专享座",
    "3": "经济座",
    "0": "商务经济座"
}

jsdata = json.loads(response.text)['Route']

tzurl = 'https://flights.ch.com/CAN-SHA.html?' \
        'Departure=%E6%98%86%E6%98%8E' \
        '&Arrival=%E4%B8%8A%E6%B5%B7' \
        '&FDate=2021-05-12' \
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

print(dict)



