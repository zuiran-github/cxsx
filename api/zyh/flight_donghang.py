import requests
import json
import re

def getPrice(pricelist, flightID):
    try:
        for item in pricelist:
            try:
                if flightID in item.keys():
                    price = item[flightID]
                    return price
            except:
                return int(999999999999)
        return 9999999
    except:
        return int(999999999)



def setPrice(flightID, pricelist, minprice):
    pl = pricelist
    for item in pricelist:
        if flightID in item.keys():
            pl.remove(item)
    pl.append({flightID: minprice})
    # print(pl)

    return pl

def getDonghang(dep, arr, day):
    cookies = {
        'Webtrends': 'dbb8ae9c.5c0534c5c5608',
        'language': 'zh_CN',
        'ecrmWebtrends': '58.194.169.213.1618838879846',
        '_ga': 'GA1.2.1485316336.1618838880',
        'gr_user_id': '7f1bef40-4e48-4703-9d4d-6ae27b9462dc',
        '_gid': 'GA1.2.749067588.1622560138',
        'JSESSIONID': 'ZOH1kdj1jGPvVtuud5cQh9N2.laputaServer1',
        '84bb15efa4e13721_gr_session_id': '01f2d16d-1240-4ff1-b4bc-69e86deacbe5',
        '84bb15efa4e13721_gr_session_id_01f2d16d-1240-4ff1-b4bc-69e86deacbe5': 'true',
        '_gat_UA-80008755-11': '1',
        '_gat': '1',
    }

    headers = {
        'Proxy-Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://www.ceair.com',
        'Referer': 'http://www.ceair.com/booking/BJS-SHA-210705_CNY.html?seriesid=ec53ec609db011ebbf7dbff53ea62a3b',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    data = {
        '_': 'ec53ec609db011ebbf7dbff53ea62a3b',
        'searchCond': '{"adtCount":1,"chdCount":0,"infCount":0,"currency":"CNY","tripType":"OW","recommend":false,"reselect":"","page":"0","sortType":"a","sortExec":"a","seriesid":"ec53ec609db011ebbf7dbff53ea62a3b",'
                      '"segmentList":[{'
                      '"deptCd":"' + dep +
                      '",'
                      '"arrCd":"' + arr +
                      '",'
                      '"deptDt":"' + day +
                      '",'
                      '"deptAirport":"","arrAirport":"",'
                      '"deptCdTxt":"' + '昆明' +
                      '",'
                      '"arrCdTxt":"' + '杭州' +
                      '",'
                      '"deptCityCode":"' + dep +
                      '",'
                      '"arrCityCode":"' + arr +
                      '"}],"version":"A.1.0"}'
    }

    response = requests.post('http://www.ceair.com/otabooking/flight-search!doFlightSearch.shtml', headers=headers,
                             cookies=cookies, data=data, verify=False)

    print(response.status_code)
    print(response.text)
    data = json.loads(response.text)['searchProduct']
    # print(data)
    # print(len(data))
    pricelist = []

    for item in data:
        priceID = item['snk']
        flightID = priceID[32:38]
        price = item['salePrice']
        # price = int(re.findall(r'\d+', price)[-2]) - 10
        # print(price)
        minprice = getPrice(pricelist, flightID)
        # print(minprice)
        if int(minprice) > price:
            minprice = price
            npl = setPrice(flightID, pricelist, minprice)
            pricelist = []
            pricelist = npl
            # pricelist.append({flightID: minprice})

    print(pricelist)
    return pricelist


dep = 'KMG'
arr = 'HGH'
day = '2021-07-03'
list = getDonghang(dep, arr, day)
print(list)

