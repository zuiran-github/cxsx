import requests
import json



dep = 'TNA'
arr = 'SHA'
day = '2021-06-24'


headers = {
    'authority': 'sjipiao.fliggy.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-dest': 'script',
    'referer': 'https://sjipiao.fliggy.com/homeow/trip_flight_search.htm?searchBy=1280&ttid=seo.000000574&tripType=0&depCityName=%C9%CF%BA%A3&depCity=&arrCityName=%B1%B1%BE%A9&arrCity=&depDate=2021-06-24&arrDate=',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cookie': 'lid=zuqing3988; enc=Db9%2F5wUab0ON8wJKb9gEVIi7wIvSmfJjArOgLXBbxg1OeVi2ln%2BDZUciMBvLOP1eyRT3cPvm3DTYEou%2BtwP31Q%3D%3D; cna=2pwEFhXYfBkCATrCqSdDLazR; t=deba0f00f7313525600dd7fff4b8a120; _tb_token_=e9771b35e115e; cookie2=1bfe8fa7a40bcf84ae42a36933612924; UM_distinctid=17968e9515d3a-09056b768495b-336a7c08-13c680-17968e9515edc9; CNZZDATA30066717=cnzz_eid%3D978279844-1620959474-%26ntime%3D1620959474; xlly_s=1; isg=BF9fZH4PQ4tQp0eXDDVRmSxX7rXpxLNmsW-HBfGsnY5VgH8C-ZSDt1WRQhD-LIve; tfstk=cyNlBmcOnmtsL_D0C_G7yuzvV-QAZnTq2kr7gWzHimOZjbFVi692QJ7Cnmqu9p1..; l=eBPb1IO4j4h1rUS1BOfZlurza77thIRvmuPzaNbMiOCPObf95iD1W66Qko8pCnGVhsn6R3lbzS4YBeYBcbh-nxvOZTG47vHmn',
}



params = (
    ('_ksTS', '1620962800220_176'),
    ('callback', 'jsonp177'),
    ('tripType', '0'),
    ('depCity', 'SHA'),
    ('depCityName', '上海'),
    ('arrCity', 'TNA'),
    ('arrCityName', '济南'),
    ('depDate', '2021-06-29'),
    ('searchSource', '99'),
    ('searchBy', '1280'),
    ('sKey', ''),
    ('qid', ''),
    ('needMemberPrice', 'true'),
    ('_input_charset', 'utf-8'),
    ('ua', '090#qCQXtXX2XuTXPTi0XXXXXQkIIr0yT9jhBlLlIe5rAGB2foX4cn0JGwEPOz7ej0jJzwl5XvXQjsAKIqXiXXkkfi4bQ0TO1ixiXakNRJdYr4ENDSd91ED3ry0ESb+cCXV3Sp1NRhMQr4EDd/d91ED3ryBlHTQXaPjPipg1hwIVPXQXiJcvQBqVFnviXXxXTPFNvaXVXvXQceniiv=='),
    ('openCb', 'false'),
)

response = requests.get('https://sjipiao.fliggy.com/searchow/search.htm', headers=headers, params=params)
print(response.status_code)
s = response.text
s = s.replace(' ', '')
s = s.replace('\n', '')
s = s[10:-2]
# print(s)
data = json.loads(s)['data']
airportMap = data['airportMap']
aircodeNameMap = data['aircodeNameMap']


tzurlMap = {
    # 厦门
    'MF' : 'https://www.xiamenair.com/zh-cn/nticket.html?tripType=OW&orgCodeArr%5B0%5D=' + dep + \
                '&dstCodeArr%5B0%5D=' + arr + \
                '&orgDateArr%5B0%5D=' + day + \
                '&dstDate=&isInter=false&adtNum=1&chdNum=0&JFCabinFirst=false&acntCd=&mode=Money&partner=false&jcgm=false',

    # 山东
    'SC' : 'https://flights.sda.cn/flight/search/' + dep + '-' + arr + '-' + day,

    # 深圳
    'ZH' : 'http://www.shenzhenair.com/szair_B2C/flightsearch.action?' \
                'orgCityCode=' + dep + \
                '&dstCityCode=' + arr + \
                '&hcType=DC&orgCity=%E4%B8%8A%E6%B5%B7%E8%99%B9%E6%A1%A5&dstCity=%E6%B7%B1%E5%9C%B3' \
                '&orgDate=' + day + \
                '&dstDate=' + day + \
                '&easyFlyFlag=0&constId=',

    # 吉祥
    'HO' : 'http://www.juneyaoair.com/pages/Flight/flight.aspx?' \
                'flightType=OW' \
                '&sendCity=%E4%B8%8A%E6%B5%B7' \
                '&sendCode=' + dep + \
                '&arrCity=%E8%A5%BF%E5%AE%89' \
                '&arrCode=' + arr + \
                '&directType=N' \
                '&tripType=D' \
                '&departureDate=' + day + \
                '&returnDate=',

    # 东航
    'MU' : 'http://www.juneyaoair.com/pages/Flight/flight.aspx?' \
                'flightType=OW' \
                '&sendCity=%E4%B8%8A%E6%B5%B7' \
                '&sendCode=' + dep + \
                '&arrCity=%E8%A5%BF%E5%AE%89' \
                '&arrCode=' + arr + \
                '&directType=N' \
                '&tripType=D' \
                '&departureDate=' + day + \
                '&returnDate=',

    # 春秋
    '9C' : 'https://flights.ch.com/' + dep + '-' + arr + '.html?' \
                                                                      'Departure=%E6%98%86%E6%98%8E' \
                                                                      '&Arrival=%E4%B8%8A%E6%B5%B7' \
                                                                      '&FDate=' + day + \
                '&RetDate=2021-07-22' \
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
                '&IsNew=1',

    # 国航 待修改
    'CA': 'http://et.airchina.com.cn/InternetBooking/AirFareFamiliesFlexibleForward.do',

    # 海航 待修改
    'HU': 'https://new.hnair.com/hainanair/ibe/air/searchResults.do?'
          'telassa-id=IbeNotLogin%7E5C5F2CF573E7BF9359FFBA26F7B2592A%7Ehu-dev-PRD-0a08e4c4-450301-173456'
          '&_catRootMessageId=hu-dev-PRD-0a08e4c4-450301-173456'
          '&_catParentMessageId=hu-dev-PRD-0a08e4c4-450301-173456'
          '&_catChildMessageId=hu-dev-PRD-0a08e4c4-450301-173731',

    # 联航
    'KN': 'http://www.flycua.com/booking/search.html?'
          'flightType=oneway'
          '&Origin=CITY_'+dep+'_CN'
          '&Destination=CITY_'+arr+'_CN'
          '&departDate=' + day +
          '&adults=1&children=0&militaryDisability=0&policeRemnants=0',

    # 奥凯 待修改
    'BK': 'https://www.okair.net/services.html#/searchResult'
}
# print(airportMap)
# print(type(airportMap))

flightinfo = data['flight']

listfordict = []

for item in flightinfo:

    arrAirport = item['arrAirport']
    acity = airportMap[arrAirport]
    atime = item['arrTime'][:10] + ' ' + item['arrTime'][10:]

    depAirport = item['depAirport']
    dcity = airportMap[depAirport]
    dtime = item['depTime'][:10] + ' ' + item['depTime'][10:]

    flightID = item['flightNo']
    cabin = item['cabin']['specialType']

    price = item['cabin']['bestPrice']

    airlineCode = item['airlineCode']
    company = aircodeNameMap[airlineCode]

    date = dtime[:10]

    # 南航
    if airlineCode == 'CZ':
        tzurl1 = 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?' \
                 't=S' \
                 '&c1=BJS' \
                 '&c2=SHA' \
                 '&d1=' + day + \
                 '&at=1' \
                 '&ct=0' \
                 '&it=0' \
                 '&b1=PEK-PKX' \
                 '&b2=SHA-PVG'

        tzurl2 = 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?' \
                 't=S' \
                 '&c1=' + dep + \
                 '&c2=' + arr + \
                 '&d1=' + day + \
                 '&at=1' \
                 '&ct=0' \
                 '&it=0' \
                 '&b1=' + dep + \
                 '&b2=' + arr

        tzurl3 = 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?' \
                 't=S' \
                 '&c1=SHA' \
                 '&c2=BJS' \
                 '&d1=' + day + \
                 '&at=1' \
                 '&ct=0' \
                 '&it=0' \
                 '&b1=SHA-PVG' \
                 '&b2=PEK-PKX'

        tzurl4 = 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?' \
                 't=S' \
                 '&c1=BJS' \
                 '&c2=' + arr + \
                 '&d1=' + day + \
                 '&at=1' \
                 '&ct=0' \
                 '&it=0' \
                 '&b1=PEK-PKX' \
                 '&b2=' + arr

        tzurl5 = 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?' \
                 't=S' \
                 '&c1=SHA' \
                 '&c2=' + arr + \
                 '&d1=' + day + \
                 '&at=1' \
                 '&ct=0' \
                 '&it=0' \
                 '&b1=SHA-PVG' \
                 '&b2=' + arr

        tzurl6 = 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?' \
                 't=S' \
                 '&c1=' + dep + \
                 '&c2=SHA' \
                 '&d1=' + day + \
                 '&at=1' \
                 '&ct=0' \
                 '&it=0' \
                 '&b1=' + dep + \
                 '&b2=SHA-PVG'

        tzurl7 = 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?' \
                 't=S' \
                 '&c1=' + dep + \
                 '&c2=BJS' \
                 '&d1=' + day + \
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
    else:
        tzurl = tzurlMap[airlineCode]

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

print(listfordict)







#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://sjipiao.fliggy.com/searchow/search.htm?_ksTS=1620962800220_176&callback=jsonp177&tripType=0&depCity=SHA&depCityName=%E4%B8%8A%E6%B5%B7&arrCity=BJS&arrCityName=%E5%8C%97%E4%BA%AC&depDate=2021-06-24&searchSource=99&searchBy=1280&sKey=&qid=&needMemberPrice=true&_input_charset=utf-8&ua=090%23qCQXtXX2XuTXPTi0XXXXXQkIIr0yT9jhBlLlIe5rAGB2foX4cn0JGwEPOz7ej0jJzwl5XvXQjsAKIqXiXXkkfi4bQ0TO1ixiXakNRJdYr4ENDSd91ED3ry0ESb%2BcCXV3Sp1NRhMQr4EDd%2Fd91ED3ryBlHTQXaPjPipg1hwIVPXQXiJcvQBqVFnviXXxXTPFNvaXVXvXQceniiv%3D%3D&openCb=false', headers=headers)
