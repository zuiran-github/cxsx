# import requests
#
#
# url = 'https://www.cdal.com.cn/stdair/searchResults/searchResultsOnewayTSDF'
#
# data = "SupplierCode=&route-type=oneway&trpDeparture=%E6%88%90%E9%83%BD&Departure=CITY_CTU_CN&localDeparture=China&trpArrival=%E9%95%BF%E6%B2%99&Arrival=CITY_CSX_CN&localArrival=China&DepartDateInput=2021-05-13&fixTime=YES"
#
#
#

def chengdu(depcode, arrcode, day):
    import requests

    cookies = {
        'Webtrends': '58.194.169.213.1618839223297131',
        'dmid': '8521fd64-253d-46fb-8035-42f6ca1d8009',
        'opvc': 'c71d3436-829f-4152-aa48-529ea9ae4b77',
        'sitevisitscookie': '2',
        'JSESSIONID': 'aldZDd2i1TyDZRE3k45aEJZO.EUCMSServer6',
    }

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'Origin': 'https://www.cdal.com.cn',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://www.cdal.com.cn/',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    data = {
        'SupplierCode': '',
        'route-type': 'oneway',
        'trpDeparture': '\u6210\u90FD',
        'Departure': 'CITY_CTU_CN',
        'localDeparture': 'China',
        'trpArrival': '\u957F\u6C99',
        'Arrival': 'CITY_CSX_CN',
        'localArrival': 'China',
        'DepartDateInput': '2021-05-13',
        'fixTime': 'YES'
    }

    r = requests.post('https://www.cdal.com.cn/stdair/searchResults/searchResultsOnewayTSDF', headers=headers,
                      cookies=cookies, data=data)

    print(r.status_code)
    print(r.text)
