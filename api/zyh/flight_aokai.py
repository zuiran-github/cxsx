import requests
import json


def aokai(dep, arr, day):
    '''

    :param dep: 大写城市代码
    :param arr: 大写城市代码
    :param day: 2021-05-26
    :return:
    '''

    day1 = day[:4] + day[5:7] + day[8:]

    cookies = {
        'acw_tc': '65c86a0a16203841712926043ebd00c4942fd75783bb27e0bc439ec65dc986',
        'A_JNID': '8a367336165a643ac48557293464edbf64beb880800eaa0b5bd8e',
        'A_SSID': '16220c7b3ce7137c4186d0b29c57c8be',
        'UM_distinctid': '179466c491682a-08683f65d69897-336a7c08-13c680-179466c4917b1a',
        'CNZZDATA1277681476': '931279298-1620380120-%7C1620380120',
        'currentCity': '%E6%B5%8E%E5%8D%97',
        'currentCode': 'TNA',
        'currentType': 'D',
        'notice-read-ETweb': 'true',
        'A_CKPC': 'IHiLpDtUtFm6vrfwpw5ynx5abJ25VEYxXbnp0RBjRAqB92ngrQpgQoEQ%2B3sWpHOr%2B0w89nX3RYd2Bc7TBgnG8g%3D%3D',
    }

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'Content-Type': 'application/json',
        'Origin': 'https://www.okair.net',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.okair.net/services.html',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    data = '{' \
           '"org":"' + dep + '",' \
           '"dst":"' + arr + '",' \
           '"fltDate":"' + day1 + '"' \
           '}'

    response = requests.post('https://www.okair.net/api/pub/queryFare', headers=headers, cookies=cookies, data=data)
    print(response.status_code)

    jdata = json.loads(response.text)['data']['avFltInfo']
    # print(jdata)

    company = "奥凯航空"
    listfordict = []
    for item in jdata:
        flightID = item['flightNoGroup']

        i = item['segmentList'][0]

        arrAirportInfo = i['arrAirportInfo']
        acity = arrAirportInfo['airportLongName']
        atime = i['arrTime']
        atime = day + ' ' + atime[:2] + ':' + atime[2:] + ':00'
        depAirportInfo = i['depAirportInfo']
        dcity = depAirportInfo['airportLongName']
        dtime = i['depTime']
        dtime = day + ' ' + dtime[:2] + ':' + dtime[2:] + ':00'

        avCabinInfo = i['avCabinInfo']
        cabin = avCabinInfo[-2]['baseCabinName']
        price = int(avCabinInfo[-2]['fdPrice']) + 50

        tzurl = 'https://www.okair.net/welcome.html'

        listfordict.append({'company': company,
                            'flightID': flightID,
                            'dCityName': dcity,
                            'aCityName': acity,
                            'date': day,
                            'dTime:': dtime,
                            'aTime': atime,
                            'cabin': cabin,
                            'price': price,
                            'tzurl': tzurl
                            })

    print(listfordict)

    return listfordict

dep = 'CTU'
arr = 'TSN'
date = '2021-05-20'
aokai(dep, arr, date)