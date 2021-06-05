import requests
import json


def getCityID(cityname):
    '''
    :param cityname:
    :return: 大写
    '''
    dict = {'安庆': 'AQG', '阿克苏': 'AKU', '北海': 'BHY', '毕节': 'BFJ', '包头': 'BAV', '北京大兴': 'PKX', '北京首都': 'PEK', '常州': 'CZX', '常德': 'CGD', '成都': 'CTU', '池州': 'JUH', '长春': 'CGQ', '重庆': 'CKG', '长沙': 'CSX', '承德': 'CDE', '大同': 'DAT', '大连': 'DLC', '敦煌': 'DNH', '大庆': 'DQA', '大理': 'DLU', '恩施': 'ENH', '福州': 'FOC', '贵阳': 'KWE', '广州': 'CAN', '固原': 'GYU', '赣州': 'KOW', '桂林': 'KWL', '杭州': 'HGH', '海拉尔': 'HLD', '呼和浩特': 'HET', '衡阳': 'HNY', '海口': 'HAK', '汉中': 'HZG', '哈尔滨': 'HRB', '黄山': 'TXN', '邯郸': 'HDG', '合肥': 'HFE', '淮安': 'HIA', '九寨': 'JZH', '嘉峪关': 'JGN', '景德镇': 'JDZ', '济宁': 'JNG', '揭阳': 'SWA', '井冈山': 'JGS', '金昌': 'JIC', '济南': 'TNA', '昆明': 'KMG', '库尔勒': 'KRL', '喀什': 'KHG', '拉萨': 'LXA', '柳州': 'LZH', '泸州': 'LZO', '陇南': 'LNL', '临沂': 'LYI', '连云港': 'LYG', '兰州': 'LHW', '连城': 'LCX', '洛阳': 'LYA', '丽江': 'LJG', '牡丹江': 'MDG', '满洲里': 'NZH', '梅州': 'MXZ', '绵阳': 'MIG', '南昌': 'KHN', '南充': 'NAO', '宁波': 'NGB', '南阳': 'NNY', '南京': 'NKG', '南通': 'NTG', '南宁': 'NNG', '鄂尔多斯': 'DSN', '攀枝花': 'PZI', '秦皇岛': 'BPE', '衢州': 'JUZ', '琼海': 'BAR', '青岛': 'TAO', '泉州': 'JJN', '日照': 'RIZ', '石家庄': 'SJW', '三亚': 'SYX', '三清山': 'SQD', '深圳': 'SZX', '沈阳': 'SHE', '上海浦东': 'PVG', '三明': 'SQJ', '松原': 'YSQ', '上海虹桥': 'SHA', '十堰': 'WDS', '唐山': 'TVS', '铜仁': 'TEN', '太原': 'TYN', '腾冲': 'TCZ', '台州': 'HYN', '吐鲁番': 'TLQ', '天津': 'TSN', '温州': 'WNZ', '武夷山': 'WUS', '无锡': 'WUX', '乌鲁木齐': 'URC', '乌海': 'WUA', '万州': 'WXN', '武汉': 'WUH', '威海': 'WEH', '忻州': 'WUT', '西双版纳': 'JHG', '襄阳': 'XFN', '西安': 'XIY', '西昌': 'XIC', '厦门': 'XMN', '兴义': 'ACX', '徐州': 'XUZ', '西宁': 'XNN', '伊宁': 'YIN', '义乌': 'YIW', '宜昌': 'YIH', '宜春': 'YIC', '盐城': 'YNZ', '宜宾': 'YBP', '银川': 'INC', '扬州': 'YTY', '烟台': 'YNT', '岳阳': 'YYA', '榆林': 'UYN', '运城': 'YCU', '延吉': 'YNJ', '中卫': 'ZHY', '湛江': 'ZHA', '张家口': 'ZQZ', '张家界': 'DYG', '遵义新舟': 'ZYI', '遵义茅台': 'WMT', '临汾': 'LFQ', '珠海': 'ZUH', '郑州': 'CGO', '扎兰屯': 'NZL', '舟山': 'HSN'}
    cityID = dict[cityname]
    return cityID



def shenzhen(dep, arr, day):
    '''
    :param dep: 上海虹桥
    :param arr: 深圳
    :param day: 2021-05-12
    :return:
    '''

    depcode = getCityID(dep)
    arrcode = getCityID(arr)

    cookies = {
        'JSESSIONID': '33331A58C1016F06D49DFD384A980616',
        'x-s3-sid': 'S123Xxuxdpu8514515jur6nzj',
        'A_JNID': '50a67a76e465568dc3f661316e74b937082c880a18de0878aa6e8%3B%3BRMKMXU%2FRqsjuyJ1NrTMVpz6QRkqW74WHtVwy7zyRYKr%2BxBTgUWJGIXC7%2FZ6B0QJAFrRBePesFEbhAiD3zNxIWhe%2FrfJTaF%2FPDjFOUXyJZffitQyTEkptEiVESyKpaENzyMy6mHgzaFxlVlAglWKheNsHv5eTJ8EUdU6xWXRdHE3qTlg5YltOHpKQ2uGb%2B8u%2BmYkHzQ6sU%2FeAk8Uh4Oqrn6QWqX7q3FwOmg2pVwC8CXRXZfcVB43RcMG9t%2F8CqsSY2Ug%2BxuxnHSuguNjmOb%2Bjv4PqFZ8axdnZ3IaLvYrA0eHCFjtpFlVkwwOuPJANk3Xqm%2BwawjmityWiGOYlvEE3%2FH2%2F46zGpKkK57uRPC2Rq5FjnDakbcygfVswgqfRM8k2vHG6IzBhWpGaCLzQf%2FObkA%3D%3D',
        'A_SSID': '440a3f432c39eb7b923e5aabecd298d3',
        '_gscu_1739384231': '188399133q88wx13',
        # 'AlteonP': f"BKKzUm9ADgqd9cNJgocdLg{$}",
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22178ea60c78d5b2-039e2cc5d09aa6-336a7c08-1296000-178ea60c78eea3%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22178ea60c78d5b2-039e2cc5d09aa6-336a7c08-1296000-178ea60c78eea3%22%7D',
        'x-s3-tid': 'b2a3006eaf0d6c1f4aa97280d210d6b57880c5be:95:b215fccd-a24b-11eb-9343-3cd2e55daed6:ae97f500c0',
        '_gscbrs_1739384231': '1',
        'x-s3-s4e': 'W6kCgewc0bF0RUDv0GCM21wuZCaBZT2092GQwdKAL%2Fcaqq1njR6ya2Fzsh9HLwkZP4LW7ZoAs5D3B9to%2Fhuhtdhl%2Fr4erzygIJ4xwX2RedD0EZbt2hVpdH1ZNNH%2Fug92F8Pz9R1JB2ieJfEvIjZnCzn3BGSiK%2Bf0UjOE%2Fgin36bf4%2FvNq0G3XBIZ%2BiBYO4dGtLLXbtK9NkI%2BbvLCGu1UjCOaVsEz6689GsETy9pjR31bEfxQghWdayQzoAuGsbhZzoB3KL%2FIzgHVTuZMbbxyNr7WOb6k4HqJF6lbnUvael8mL4eM1jsk%2FrSBJX3AQsgObe9%2Fb%2FOGgeEezBiyMK90CI%2F6cHVAPwLab1%2Ff47Wz4w2mxquMyd3Tq4be0j7f4%2FD%2FAXGmzlXhABO9JVu%2BftLmRF230%2FrhrjB23%2Fa6J22u3v3Qi6dNRQCGE8uVKSxfMFKHD6zuwwEJWVtgXTpQoYQvXwPkKBj15WasNPdj5G5rE9rpgQQlo1gsvBM6opA56LNSsvWXJdp4ZSePPJTHfLI9YLIEbltipQXylJhGERq1LyR6v9%2BdO4lPehI9iHJNXcUhNHki1sgOENqXFJuBJ4dcaIDZ%2BHvBpZl%2B%2B2cu75efCHy4dXAh9DTQr7Fanz%2FAObsT86nCcqHRdyPRvqwaGgIMShLOUN7twU52m6VAZMv75PMAVQT268uvkurIBEc4hGk9twD8eb56XbXCNz9q0Aku1kL6PpaqtL%2Bz8Uaw9Uau4osP63DrNWlnm%2BlJRYzR%2FChOL%2FEa2GqmXuUC%2FOKGSqwZsznSJGBztwZuzsozWlUYDd1cuJFUhoYFZklCsaW4c0eN1IMIpeHTimcKcdFkbzfTxwiuP139s6HkVf6WOWZ5aw9iveOy3W6x7apBAlQvbSuHrxxJHhx77Da7ECskC53F2iMEJUUA5k1ddyfM2XLgsZRrjZYbUYc%2BKW6Rd7WVV07W4VKwEIjHznJYH5EJRGgn94fkeSQwfMeIdGtgrQrQUinz3aJH%2FJsz%2BTMGUP0l4zbn3sSsb2a3006eaf0d6c1f4aa97280d210d6b57880c5be:95:b215fccd-a24b-11eb-9343-3cd2e55daed6:ae97f500c0',
        'fromPage': '%7BfromPage%3A%22flightSearch%22%7D',
        'sccode': '%7BsccodeInfo%3A%22%u822A%u73ED%u5217%u8868%u9875%26%u91CD%u65B0%u67E5%u8BE2%22%7D',
        'A_CKPC': 'nS64pPhAXifyseDBfryk89haRaaXXGTbZ29hS7SA5HkoUcl3nvfEyQ%2FhN8jhHDXtXDyuF8weO280MzYqZFw8AMkKzTiWlC3rqxs9mrCp78AuMAoLQTicY8E3Bm4DcOcvLTfxbMPLJ9Iuaf5UpCkD6w%3D%3D',
        '_gscs_1739384231': '18973156o1fdwt18|pv:2',
    }

    headers = {
        'Proxy-Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://www.shenzhenair.com',
        'Referer': 'http://www.shenzhenair.com/szair_B2C/flightsearch.action?orgCityCode=SHA&dstCityCode=SZX&hcType=DC&orgCity=%E4%B8%8A%E6%B5%B7%E8%99%B9%E6%A1%A5&dstCity=%E6%B7%B1%E5%9C%B3&orgDate=2021-05-13&dstDate=2021-05-13&easyFlyFlag=0&constId=',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    data = {
        'condition.orgCityCode': depcode,
        'condition.dstCityCode': arrcode,
        'condition.hcType': 'DC',
        'condition.orgDate': day,
        'condition.dstDate': day,
    }

    response = requests.post('http://www.shenzhenair.com/szair_B2C/flightSearch.action', headers=headers,
                             cookies=cookies, data=data, verify=False)

    print(response.status_code)
    # print(response.text)
    jsdata = json.loads(response.text)['flightSearchResult']
    # print(type(jsdata))

    company = '深圳航空'
    tzurl = 'http://www.shenzhenair.com/szair_B2C/flightsearch.action?' \
            'orgCityCode='+depcode+ \
            '&dstCityCode='+arrcode+ \
            '&hcType=DC&orgCity=%E4%B8%8A%E6%B5%B7%E8%99%B9%E6%A1%A5&dstCity=%E6%B7%B1%E5%9C%B3' \
            '&orgDate='+day+ \
            '&dstDate='+day+ \
            '&easyFlyFlag=0&constId='

    # 仓位
    cabindict = jsdata['classTypes']
    # print(type(cabindict))
    # print(cabindict)

    flightinfo = jsdata['flightInfoList']

    date = jsdata['departureTime']

    dict = {}
    count = 0

    for item in flightinfo:
        # print(type(item))
        flightID = item['flightNo']
        # print(flightID)

        dcity = item['orgCityCH']
        dtime = item['orgTime']
        acity = item['dstCityCH']
        atime = item['dstTime']

        pricelist = item['classInfoList']
        i = len(pricelist)
        price = pricelist[i - 1]['classPrice']
        cabin = cabindict[pricelist[i - 1]['classType']]

        dict[count] = {
            'company': company,
            'flightID': flightID,
            'dCityName': dcity,
            'aCityName': acity,
            'date': date,
            'dTime:': dtime,
            'aTime': atime,
            'cabin': cabin,
            'price': price,
            'tzurl': tzurl,
        }
        count += 1

    print(dict)


departure = '上海虹桥'
arrival = '广州'
day = '2021-05-15'
shenzhen(departure, arrival, day)