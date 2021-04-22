import math
import time as t
import socket
import requests
import re
import urllib.parse as p

def getCityId(cityn):
    with open('pig.txt','r', encoding='utf-8') as f:
        data = f.read().replace(' ','')  # 读取文件
        data = data.replace('区','').replace('市','').replace('县','')
        find_city = re.findall(r'\"name.*?\"\:\"(.*?)\"', data)
        find_city_code=re.findall(r'code.*?\"\:\"(.*?)\"\,',data)
    city_dict = {}
    for city,code in zip(find_city,find_city_code):
        city_dict[city] = code
    cityc = city_dict[cityn]
    return cityc
    #del city_dict["辖"]
    #with open('123.txt','w', encoding='utf-8') as f:
        #f.write(str(city_dict))

def getTotal(city,checkin,checkout):
    cityCode = getCityId(city)
    url = 'https://hotel.fliggy.com/hotel_list3.htm?_input_charset=utf-8&cityName={}&city={}&keywords=&checkIn={}&checkOut={}&_output_charset=utf8'.format(p.quote(city),cityCode,checkin,checkout)
    header ={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75',
        'cookie': 'cna=OQEbFwo0PDACAQGj0kXs9Yu1; hng=TW%7Czh-TW%7CTWD%7C158; t=541feab924f74bf0636cff621be3a944; tracknick=%5Cu845B%5Cu6E58%5Cu7F9A; lid=%E8%91%9B%E6%B9%98%E7%BE%9A; enc=fiMMRxt%2BHzrq50%2B8sXnqj3gZbxU925mVWKpkN4SP6pjqym2fHJK73Ed26j46sDrsNJCINY7VplFP2578GEuRFQ%3D%3D; _tb_token_=eb05bebe8ebee; cookie2=1cdd5e032006480d3342ac6db8b3db0f; UM_distinctid=178ce39871f453-06dd622087e5a1-71667960-144000-178ce3987207db; dnk=%5Cu845B%5Cu6E58%5Cu7F9A; VISITED_HOTEL_TOKEN=5011b935-f6e2-4c62-8b54-f34e8dc05e20; chanelStat="NA=="; _uab_collina=161836816968261151747997; CNZZDATA1253581663=2089767974-1618366393-https%253A%252F%252Fwww.fliggy.com%252F%7C1618755754; xlly_s=1; tfstk=cJ2RBPtaLZblaqiYb7CDAQEbXkzdapx--3gppgQ7IraD8BOets4uIRent_iEvajA.; l=eBLqh36VjwG7CYwTBO5CFurza779qIRb8sPzaNbMiInca6CFNep2HNCQJ4yDldtjgtfUxetruJ9D3RFJJHzdNxDDBe4DcatJexJ6-; isg=BLi43jaaLGdkq0Dp9lSI7jGfiWZKIRyrMeow7vIpx_OuDVn3mjFXO8ZsxQW9XdSD; uc1=cookie14=Uoe1iufrvFFsIg%3D%3D&pas=0&existShop=false&cookie15=WqG3DMC9VAQiUQ%3D%3D&cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&cookie21=WqG3DMC9FxUx; _l_g_=Ug%3D%3D; unb=2794081654; cookie1=W8nRNFCJ7dWyKPe838mVpe2gIslghNm1E0sVkB4X%2BG0%3D; login=true; cookie17=UU8BqJbDCVfeIg%3D%3D; _nk_=%5Cu845B%5Cu6E58%5Cu7F9A; sgcookie=E1000NZCFqy1QpU691Bnd%2F0IRtIiakuVZAJFmsNui%2FuyY%2BMmxQ9hufR30wZ8VRn4A6tLb%2FdqkbXn7sIU4yXjRl3BYA%3D%3D; sg=%E7%BE%9A4f; csg=5fffd259'
    }
    param ={
        '_input_charset': 'utf-8',
        'cityName': city,
        'city': cityCode,
        'keywords': '',
        'checkIn': checkin,
        'checkOut': checkout,
        '_output_charset': 'utf8'
    }
    res =requests.get(url=url,headers=header,params=param)
    # list转str，找总数
    total_item = "".join(re.findall(r'totalItem\"\:(.*?)\,', res.text))
    page = math.ceil(int(total_item) / 20)
    return total_item,page

def get_host_ip():

    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip=s.getsockname()[0]
    finally:
        s.close()

    return ip

def getdata(session, city, checkin, checkout,npage,total_item,page):
    ip = get_host_ip()
    citycode = getCityId(city)
    ktsts = t.time()
    cookie = 'cna=OQEbFwo0PDACAQGj0kXs9Yu1; hng=TW%7Czh-TW%7CTWD%7C158; t=541feab924f74bf0636cff621be3a944; tracknick=%5Cu845B%5Cu6E58%5Cu7F9A; lid=%E8%91%9B%E6%B9%98%E7%BE%9A; enc=fiMMRxt%2BHzrq50%2B8sXnqj3gZbxU925mVWKpkN4SP6pjqym2fHJK73Ed26j46sDrsNJCINY7VplFP2578GEuRFQ%3D%3D; _tb_token_=eb05bebe8ebee; cookie2=1cdd5e032006480d3342ac6db8b3db0f; UM_distinctid=178ce39871f453-06dd622087e5a1-71667960-144000-178ce3987207db; dnk=%5Cu845B%5Cu6E58%5Cu7F9A; VISITED_HOTEL_TOKEN=5011b935-f6e2-4c62-8b54-f34e8dc05e20; chanelStat="NA=="; _uab_collina=161836816968261151747997; CNZZDATA1253581663=2089767974-1618366393-https%253A%252F%252Fwww.fliggy.com%252F%7C1618662281; xlly_s=1; uc1=cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&pas=0&existShop=false&cookie21=WqG3DMC9FxUx&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&cookie14=Uoe1iua%2FAe7IgA%3D%3D; _l_g_=Ug%3D%3D; unb=2794081654; cookie1=W8nRNFCJ7dWyKPe838mVpe2gIslghNm1E0sVkB4X%2BG0%3D; login=true; cookie17=UU8BqJbDCVfeIg%3D%3D; _nk_=%5Cu845B%5Cu6E58%5Cu7F9A; sgcookie=E100sVOxGwsKNx7UjgWT9uqfrCp3sZThQZY5w2Otli906kWMckoBYwXjWf%2BdobSRx4GjwSr9qzJYUg23X6iS4x2Ssw%3D%3D; sg=%E7%BE%9A4f; csg=51f76ab8; tfstk=cOiGBFxHPVzsLV4nPhZsCsrGuTJRaoTa1moEYmXgODLbadmUQsbh8a81BpV9nJbf.; l=eBLqh36VjwG7CA6NBO5Cnurza7794IOb8sPzaNbMiInca1oRsgAiaNCQ797k-dtjgt5vteKruJ9D3ReD8uaLREOXh9D3XP740nJw8e1..; isg=BLu7SN94X7hdbmMAyeW756ZeSp8lEM8ShktTB615xLvNDNruNOHzYloKJqxCLCcK'
    _ksTS = '%s_%s' % (int(ktsts * 1000), str(ktsts)[-3:])
    callback = "jsonp%s" % (int(str(ktsts)[-3:]) + 1)
    url = 'https://hotel.fliggy.com/ajax/hotelList.htm?pageSize=20&currentPage={}&totalItem={}&startRow=0&endRow=19&city={}&tid=null&market=0&previousChannel=&u=null&detailLinkCity={}&cityName={}&checkIn={}&checkOut={}&browserUserAgent=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F89.0.4389.114%20Safari%2F537.36%20Edg%2F89.0.774.75&userClientIp=58.194.168.58&userSessionId=2794081654&offset=0&keywords=null&priceRange=R0&dangcis=null&brands=null&services=null&order=DEFAULT&dir=DESC&client=null&tagids=null&searchPoiName=undefined&pByRadiusLng=-1&pByRadiusLat=-1&radius=-1&pByRectMinLat=-1&pByRectMinLng=-1&pByRectMaxLat=-1&pByRectMaxLng=-1&lowPrice=-1&highPrice=-1&filterByKezhan=false&searchBy=&searchByTb=false&businessAreaId=null&skipKeywords=false&district=null&backCash=false&shids=null&activity=null&filterDoubleEleven=false&filterByRoomTickets=false&filterHxk=false&filterCxk=false&filterByRoomTicketsAndNeedLogin=false&filterByRoomTicketsAndNeedBuyTicket=false&activityCode=null&searchId=null&userId=null&hotelTypes=null&filterByB2g=false&filterByAgreement=false&bizNo=null&bizType=null&region=0&newYearSpeOffer=false&laterPay=false&sellerId=null&sellerIds=null&isMemberPrice=false&isLaterPayActivity=false&isFilterByTeHui=false&keyWordsType=null&userUniqTag=null&iniSearchKW=false&poiNameFilter=&isFreeCancel=false&isInstantConfirm=false&activityCodes=&adultChildrenCondition=%26roomNum%3D1%26aNum_1%3D2%26cNum_1%3D0&overseaMarket=false&roomNum=1&notFilterActivityCodeShotel=false&poisearch=false&totalPage=1042&previousPage=1&nextPage=2&pageFirstItem=1&firstPage=true&lastPage=false&pageLastItem=20&aNum_1=2&cNum_1=0&cAge_1_1=0&cAge_1_2=0&cAge_1_3=0&_input_charset=utf-8&laterPaySwitch&_ksTS={}&callback={}'.format(npage,total_item,citycode,citycode,p.quote(city),checkin,checkout,_ksTS,callback)
    r_url= "https://hotel.fliggy.com/hotel_list3.htm?_input_charset=utf-8&cityName={}&city={}&keywords=&checkIn={}&checkOut={}&_output_charset=utf8".format(p.quote(city),citycode,checkin,checkout)
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75',
        'x-requested-with': 'XMLHttpRequest',
        "referer": r_url,
        "accept": 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'cookie': cookie
    }
    params = {
        'pageSize': 20,
        'currentPage': npage,
        'totalItem': total_item,
        'startRow': 0,
        'endRow': 19,
        'city': citycode,
        'tid': 'null','market': 0,'previousChannel': '','u': 'null',
        'detailLinkCity': citycode,
        'cityName': city,
        'checkIn': checkin,
        'checkOut': checkout,
        'browserUserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75',
        'userClientIp': ip,
        'userSessionId': 2794081654,
        'offset': 0,'keywords': 'null','priceRange': 'R0','dangcis': 'null','brands': 'null','services': 'null','order': 'DEFAULT','dir': 'DESC',
        'client': 'null','tagids': 'null','searchPoiName': 'undefined','pByRadiusLng': -1,'pByRadiusLat': -1,'radius': -1,'pByRectMinLat': -1,'pByRectMinLng': -1,'pByRectMaxLat': -1,'pByRectMaxLng': -1,'lowPrice': -1,'highPrice': -1,'filterByKezhan': 'false','searchBy': '','searchByTb': 'false','businessAreaId': 'null','skipKeywords': 'false','district': 'null','backCash': 'false','shids': 'null','activity': 'null','filterDoubleEleven': 'false','filterByRoomTickets': 'false',
        'filterHxk': 'false','filterCxk': 'false','filterByRoomTicketsAndNeedLogin': 'false','filterByRoomTicketsAndNeedBuyTicket': 'false','activityCode': 'null','searchId': 'null','userId': 'null','hotelTypes': 'null','filterByB2g': 'false','filterByAgreement': 'false','bizNo': 'null','bizType': 'null','region': 0,'newYearSpeOffer': 'false','laterPay': 'false','sellerId': 'null','sellerIds': 'null','isMemberPrice': 'false','isLaterPayActivity': 'false','isFilterByTeHui': 'false',
        'keyWordsType': 'null','userUniqTag': 'null','iniSearchKW': 'false','poiNameFilter': '','isFreeCancel': 'false','isInstantConfirm': 'false','activityCodes': '','adultChildrenCondition': '&roomNum=1&aNum_1=2&cNum_1=0','overseaMarket': 'false','roomNum': 1,'notFilterActivityCodeShotel': 'false','poisearch': 'false',
        'totalPage': page,'previousPage': 1,'nextPage': 2,'pageFirstItem': 1,
        'lastPage': 'false','pageLastItem': 20,'aNum_1': 2,'cNum_1': 0,'cAge_1_1': 0,'cAge_1_2': 0,'cAge_1_3': 0,'_input_charset': 'utf-8','laterPaySwitch': '',
        '_ksTS': _ksTS,
        'callback': callback,
    }
    res = session.get(url=url,params=params,headers=header)
    print(res.status_code)
    print(res.text)
    return res, session

def getList(city,checkin,checkout):
    session = requests.session()  # 用session保持状态
    total_item,page =getTotal(city,checkin,checkout)
    npage = 1 #当前页数
    res, session = getdata(session, city, checkin, checkout,npage,total_item,page)
    print("page1")
    printList(res, city, checkin, checkout)
    for npage in range(2,page,1):
        t.sleep(2)
        print("page" + str(npage))
        res, session = getdata(session, city, checkin, checkout,npage,total_item,page)
        printList(res, city, checkin, checkout)

def printList(res,city,checkin,checkout):
    citycode = getCityId(city)
    list = res.text
    ID_Name = re.findall(r'\"shid\"\:(.*?)\,\"name\"\:\"(.*?)\"\,', list)
    Score = re.findall(r'\"rateScore\"\:\"(.*?)\"\,', list)
    Star = re.findall(r'\"star\"\:\"(.*?)\"\,', list)
    Price = re.findall(r'\"priceDesp\"\:\"(.*?)\"\,', list)
    Comment = re.findall(r'\"rateNum\"\:(.*?)\,', list)
    for i in range(20):
        print('-------------------------------------')
        url = 'https://hotel.fliggy.com/hotel_detail2.htm?shid={}&city={}&checkIn={}&checkOut={}&searchId=4811e8b3defc48fe92d7698b9842bbb5&_output_charset=utf8'.format(ID_Name[i][0],citycode,checkin,checkout)
        print(ID_Name[i][1]+' '+Score[i] + ' ' + Star[i]+'星级')
        print(url)
        print(Comment[i] + '条住客点评')
        if Price[i]=='暂无报价'or Price[i]=='已订完':
            print(Price[i])
        else:
            print('CNY ' + Price[i])

def main():
    #city = input("目的地:")
    #checkin =input("入住时间 xxxx-xx-xx:")
    #chekout =input("退房时间 xxxx-xx-xx:")
    #getList(city,checkin,chekout)
    getList('上海','2021-05-01','2021-05-04')

if __name__ == '__main__':
    main()

