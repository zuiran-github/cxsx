import requests
import json

cookies = {
    '_ga': 'GA1.2.1158422880.1618923448',
    'Hm_lvt_9157968cfa248050a24cffbb58d677d6': '1618923428,1620649237',
    'Hm_lpvt_9157968cfa248050a24cffbb58d677d6': '1620649237',
    '_045db': 'http://172.31.46.235:8080',
    'nodeWeb': 's%3AzFUoKabq6Q-MPlFAuHNVCCVeY9OZ_AKs.BBMNuzupzOJVv12SbH7Ssf8WhZQQ8miOpP8rAMCt0I4',
    'route': 'cd427a68642f427bbfe0741e21a8bbe0',
    'OZ_1U_2074': 'vid=v07ecfa42fd333.0&ctime=1620649275&ltime=1620649275',
    'OZ_1Y_2074': 'erefer=-&eurl=http%3A//www.westair.cn/portal/&etime=1620649236&ctime=1620649275&ltime=1620649275&compid=2074',
    'OZ_SI_2074': 'sTime=1620649236&sIndex=6',
}

headers = {
    'Proxy-Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://www.westair.cn',
    'Referer': 'http://www.westair.cn/mainprocess/select',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

data = {
  'q': '%u02AD%9D%96%E6%DB%D9%C4%CD%E9%D5%87%5C%5Cq%A6yNN%91%E4%E9%D6%D1%E4%E3%D2%B3%BF%E4%DD%D8%DD%90%5C%B5%9D%86%C9%D5%D1%D3%E6%E9%E7%D7%A9%A5%D5%D9%87%5C%5CTbbc%5E%5Deb_cSNN%86%C9%D8%BC%BC%B7%B3%DC%D2%D8%E7%DD%CC%85%5C%5C%7B%7BNN%86%C9%D8%E7%DD%D7%CF%D5%DD%D8%DD%BA%BB%D2%C4%D5%DD%D8%DD%B1%B2%D3%C9%87%5C%5Cy%AC%9DjNN%86%C9%D8%E7%DD%D7%CF%D5%DD%D8%DD%BA%BB%D2%C4%D5%DD%D8%DD%BC%AF%CE%D2%87%5C%5C%u6B88%uD7AF%u6C6BNN%91%E1%DB%B2%BC%B7%B3%DC%D2%D8%E7%DD%CC%85%5C%5C%7B%7BNN%91%E1%DB%D0%D0%D7%BA%BB%D2%C4%D5%DD%D8%DD%B1%B2%D3%C9%87%5C%5Ch%95%92eNN%91%E1%DB%D0%D0%D7%BA%BB%D2%C4%D5%DD%D8%DD%BC%AF%CE%D2%87%5C%5C%u79B1%uD76D%u5E00%9F%A9N%8F%E2%E1%E0%DD%AC%AC%DD%ED%C8%BF%E4%DD%D8%DD%E1%95%5C%95%B8%89N%8B%D7%D0%D1%E4%E3%D2%B3%BF%E4%DD%D8%DD%90%5C%B5%9D%86%C9%D5%D1%D3%E6%E9%E7%D7%A9%A5%D5%D9%87%5C%5CD%9F%A9N%89%DC%DA%D8%E7%C8%CD%E9%D5%D8%95%5C%95%D6%9D%83%CE%DC%E4%E3%E2%96%5Ck%5DN%85%D2%D3%C9%87%5C%5Cc%85%98v%9F%A9%A7%9D%83%CE%DC%E4%E3%E2%96%5Cj%5CN%85%D2%D3%C9%87%5C%5Ce%91%9Cp%9F%A9%A7%9D%83%CE%DC%E4%E3%E2%96%5Cj%5CN%85%D2%D3%C9%87%5C%5Ck%97%94h%9F%A9%A7%9D%83%CE%DC%E4%E3%E2%96%5Cj%5CN%85%D2%D3%C9%87%5C%5Cu%A2%9Bn%9F%A9%A7%9D%83%CE%DC%E4%E3%E2%96%5Cj%5CN%85%D2%D3%C9%87%5C%5Cr%9F%9Bn%9F%DA%89N%85%C4%C3%CB%D7%B1%AF%CD%D4%E6%95%5C%5Cg%A8%D2%DD%DD%DC%E6%9BNN%85%D8%E7%E4%D7%D3%D1%DC%CD%CD%E9%D5%87%5C%5Ce%91%A7%7BNN%8B%DC%B7%B3%DC%D2%D8%E7%DD%CC%85%5C%5C%7B%7BNN%88%D2%D1%DD%E1%CB%CE%D1%87%5C%5CppNN%8E%CD%CF%D5%BB%CD%E9%D5%87%5C%5C%9C%E2%C7%A2%91pNN%95%E3%D5%C8%CC%CA%CD%B3%BC%DA%D8%E7%C8%CD%E9%D5%87%5C%5CDNN%92%DC%CD%D5%DA%D5%E1%DF%C1%CD%E9%D5%87%5C%5C%92%D3%85%9F'
}

response = requests.post('http://www.westair.cn/mainprocess/flight/searchFlightInfo', headers=headers, cookies=cookies, data=data, verify=False)
print(response.status_code)
# print(response.text)

data = json.loads(response.text)['data']['originDestinations']

cabin = json.loads(response.text)['data']['criteria']['cabin']

company = '西部航空'
tzurl = 'http://www.westair.cn/portal/'

listfordict = []

for item in data:
    arrdate = item['airItineraries'][0]['flightSegments'][0]['arrivalDate']
    depdate = item['departureDate']
    acity = item['dstInfo']['name']
    atime = arrdate + ' ' + item['airItineraries'][0]['flightSegments'][0]['arrivalTime']
    dcity = item['orgInfo']['name']
    dtime = depdate + ' ' + item['airItineraries'][0]['flightSegments'][0]['departureTime']

    flightID = item['airItineraries'][0]['flightSegments'][0]['marketingAirlineCode'] + item['airItineraries'][0]['flightSegments'][0]['flightNumber']
    price = item['airItineraries'][0]['airItineraryPrices'][0]['travelerPrices'][0]['baseFare']

    listfordict.append({
        'company': company,
        'flightID': flightID,
        'dCityName': dcity,
        'aCityName': acity,
        'date': depdate,
        'dTime:': dtime,
        'aTime': atime,
        'cabin': cabin,
        'price': price,
        'tzurl': tzurl,
    })

print(listfordict)


def xibu(depcode, arrcode, day):
    cookies = {
        '_ga': 'GA1.2.1158422880.1618923448',
        'Hm_lvt_9157968cfa248050a24cffbb58d677d6': '1618923428,1620649237',
        'Hm_lpvt_9157968cfa248050a24cffbb58d677d6': '1620649237',
        '_045db': 'http://172.31.46.235:8080',
        'nodeWeb': 's%3AzFUoKabq6Q-MPlFAuHNVCCVeY9OZ_AKs.BBMNuzupzOJVv12SbH7Ssf8WhZQQ8miOpP8rAMCt0I4',
        'route': 'cd427a68642f427bbfe0741e21a8bbe0',
        'OZ_1U_2074': 'vid=v07ecfa42fd333.0&ctime=1620649275&ltime=1620649275',
        'OZ_1Y_2074': 'erefer=-&eurl=http%3A//www.westair.cn/portal/&etime=1620649236&ctime=1620649275&ltime=1620649275&compid=2074',
        'OZ_SI_2074': 'sTime=1620649236&sIndex=6',
    }

    headers = {
        'Proxy-Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://www.westair.cn',
        'Referer': 'http://www.westair.cn/mainprocess/select',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    data = {
        'q': '%u02AD%9D%96%E6%DB%D9%C4%CD%E9%D5%87%5C%5Cq%A6yNN%91%E4%E9%D6%D1%E4%E3%D2%B3%BF%E4%DD%D8%DD%90%5C%B5%9D%86%C9%D5%D1%D3%E6%E9%E7%D7%A9%A5%D5%D9%87%5C%5CTbbc%5E%5Deb_cSNN%86%C9%D8%BC%BC%B7%B3%DC%D2%D8%E7%DD%CC%85%5C%5C%7B%7BNN%86%C9%D8%E7%DD%D7%CF%D5%DD%D8%DD%BA%BB%D2%C4%D5%DD%D8%DD%B1%B2%D3%C9%87%5C%5Cy%AC%9DjNN%86%C9%D8%E7%DD%D7%CF%D5%DD%D8%DD%BA%BB%D2%C4%D5%DD%D8%DD%BC%AF%CE%D2%87%5C%5C%u6B88%uD7AF%u6C6BNN%91%E1%DB%B2%BC%B7%B3%DC%D2%D8%E7%DD%CC%85%5C%5C%7B%7BNN%91%E1%DB%D0%D0%D7%BA%BB%D2%C4%D5%DD%D8%DD%B1%B2%D3%C9%87%5C%5Ch%95%92eNN%91%E1%DB%D0%D0%D7%BA%BB%D2%C4%D5%DD%D8%DD%BC%AF%CE%D2%87%5C%5C%u79B1%uD76D%u5E00%9F%A9N%8F%E2%E1%E0%DD%AC%AC%DD%ED%C8%BF%E4%DD%D8%DD%E1%95%5C%95%B8%89N%8B%D7%D0%D1%E4%E3%D2%B3%BF%E4%DD%D8%DD%90%5C%B5%9D%86%C9%D5%D1%D3%E6%E9%E7%D7%A9%A5%D5%D9%87%5C%5CD%9F%A9N%89%DC%DA%D8%E7%C8%CD%E9%D5%D8%95%5C%95%D6%9D%83%CE%DC%E4%E3%E2%96%5Ck%5DN%85%D2%D3%C9%87%5C%5Cc%85%98v%9F%A9%A7%9D%83%CE%DC%E4%E3%E2%96%5Cj%5CN%85%D2%D3%C9%87%5C%5Ce%91%9Cp%9F%A9%A7%9D%83%CE%DC%E4%E3%E2%96%5Cj%5CN%85%D2%D3%C9%87%5C%5Ck%97%94h%9F%A9%A7%9D%83%CE%DC%E4%E3%E2%96%5Cj%5CN%85%D2%D3%C9%87%5C%5Cu%A2%9Bn%9F%A9%A7%9D%83%CE%DC%E4%E3%E2%96%5Cj%5CN%85%D2%D3%C9%87%5C%5Cr%9F%9Bn%9F%DA%89N%85%C4%C3%CB%D7%B1%AF%CD%D4%E6%95%5C%5Cg%A8%D2%DD%DD%DC%E6%9BNN%85%D8%E7%E4%D7%D3%D1%DC%CD%CD%E9%D5%87%5C%5Ce%91%A7%7BNN%8B%DC%B7%B3%DC%D2%D8%E7%DD%CC%85%5C%5C%7B%7BNN%88%D2%D1%DD%E1%CB%CE%D1%87%5C%5CppNN%8E%CD%CF%D5%BB%CD%E9%D5%87%5C%5C%9C%E2%C7%A2%91pNN%95%E3%D5%C8%CC%CA%CD%B3%BC%DA%D8%E7%C8%CD%E9%D5%87%5C%5CDNN%92%DC%CD%D5%DA%D5%E1%DF%C1%CD%E9%D5%87%5C%5C%92%D3%85%9F'
    }

    response = requests.post('http://www.westair.cn/mainprocess/flight/searchFlightInfo', headers=headers,
                             cookies=cookies, data=data, verify=False)
    print(response.status_code)
    # print(response.text)

    data = json.loads(response.text)['data']['originDestinations']

    cabin = json.loads(response.text)['data']['criteria']['cabin']

    company = '西部航空'
    tzurl = 'http://www.westair.cn/portal/'

    listfordict = []

    for item in data:
        arrdate = item['airItineraries'][0]['flightSegments'][0]['arrivalDate']
        depdate = item['departureDate']
        acity = item['dstInfo']['name']
        atime = arrdate + ' ' + item['airItineraries'][0]['flightSegments'][0]['arrivalTime']
        dcity = item['orgInfo']['name']
        dtime = depdate + ' ' + item['airItineraries'][0]['flightSegments'][0]['departureTime']

        flightID = item['airItineraries'][0]['flightSegments'][0]['marketingAirlineCode'] + \
                   item['airItineraries'][0]['flightSegments'][0]['flightNumber']
        price = item['airItineraries'][0]['airItineraryPrices'][0]['travelerPrices'][0]['baseFare']

        listfordict.append({
            'company': company,
            'flightID': flightID,
            'dCityName': dcity,
            'aCityName': acity,
            'date': depdate,
            'dTime:': dtime,
            'aTime': atime,
            'cabin': cabin,
            'price': price,
            'tzurl': tzurl,
        })

    print(listfordict)

