import operator


def zyh_sortByTime(info):

    sorted_list = sorted(info, key=operator.itemgetter('dTime'))

    response = {"data": sorted_list}

    return response



def zyh_sortByCompany(info):

    sorted_list = sorted(info, key=operator.itemgetter('company'))

    response = {"data": sorted_list}

    return response


def zyh_sortByPrice(info):

    sorted_list = sorted(info, key=operator.itemgetter('price'))

    response = {"data": sorted_list}

    return response





list = [{'company': '西藏航', 'flightID': 'TV9905', 'dCityName': '双流机场', 'aCityName': '咸阳机场', 'date': '2021-07-24', 'dTime': '2021-07-24 21:45', 'aTime': '2021-07-24 23:20', 'cabin': '经济舱', 'price': 576, 'tzurl': 'https://www.tibetairlines.com.cn/stdair/searchResults/searchResultsOnewayTSDF'}, {'company': '东航', 'flightID': 'MU6795', 'dCityName': '双流机场', 'aCityName': '咸阳机场', 'date': '2021-07-24', 'dTime': '2021-07-24 08:55', 'aTime': '2021-07-24 10:20', 'cabin': '经济舱', 'price': 610, 'tzurl': 'http://www.ceair.com/booking/CTU-XIY-210724_CNY.html?seriesid=ec53ec609db011ebbf7dbff53ea62a3b'}, {'company': '东航', 'flightID': 'MU6391', 'dCityName': '双流机场', 'aCityName': '咸阳机场', 'date': '2021-07-24', 'dTime': '2021-07-24 16:30', 'aTime': '2021-07-24 17:55', 'cabin': '经济舱', 'price': 610, 'tzurl': 'http://www.ceair.com/booking/CTU-XIY-210724_CNY.html?seriesid=ec53ec609db011ebbf7dbff53ea62a3b'}, {'company': '长龙', 'flightID': 'GJ8878', 'dCityName': '双流机场', 'aCityName': '咸阳机场', 'date': '2021-07-24', 'dTime': '2021-07-24 20:45', 'aTime': '2021-07-24 22:05', 'cabin': '经济舱', 'price': 635, 'tzurl': 'https://www.loongair.cn/#/web/ticket/search'}, {'company': '南航', 'flightID': 'CZ6250', 'dCityName': '双流机场', 'aCityName': '咸阳机场', 'date': '2021-07-24', 'dTime': '2021-07-24 19:40', 'aTime': '2021-07-24 21:15', 'cabin': '全价经济舱', 'price': 810, 'tzurl': 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?t=S&c1=CTU&c2=XIY&d1=2021-07-24&at=1&ct=0&it=0&b1=CTU&b2=XIY'}, {'company': '川航', 'flightID': '3U8379', 'dCityName': '双流机场', 'aCityName': '咸阳机场', 'date': '2021-07-24', 'dTime': '2021-07-24 06:30', 'aTime': '2021-07-24 07:50', 'cabin': '全价经济舱', 'price': 970, 'tzurl': 'https://www.sichuanair.com'}, {'company': '川航', 'flightID': '3U8769', 'dCityName': '双流机场', 'aCityName': '咸阳机场', 'date': '2021-07-24', 'dTime': '2021-07-24 13:25', 'aTime': '2021-07-24 14:45', 'cabin': '全价经济舱', 'price': 970, 'tzurl': 'https://www.sichuanair.com'}]

list_time = zyh_sortByTime(list)
list_price = zyh_sortByPrice(list)
list_company = zyh_sortByCompany(list)

print(list_company)
print(list_price)
print(list_time)


