import math
import urllib.parse as p
import requests
import time as t
import json
import re

#相对应城市Code
def getCity():
    with open('tuniu.txt','r', encoding='utf-8') as f:
        data = f.read()  # 读取文件
        find_city = re.findall(r'cityName.*?\"\:\"(.*?)\"', data)
        find_city_code=re.findall(r'cityCode.*?\"\:(.*?)\,',data)
    city_dict = {}
    for city,code in zip(find_city,find_city_code):
        city_dict[city] = code
    #with open('dict.txt','w', encoding='utf-8') as f:
        #f.write(str(city_dict))
    return city_dict

#所有酒店名单
def getList(city,checkin,checkout):
    session = requests.session()
    start = 1
    res, session, end_num = getData(session, start, city, checkin, checkout)
    print(res.status_code)
    if res.status_code==403:
        print("ip被封")
    else:
        print("page1")
        printList(res, checkin, checkout)
        total_page =math.ceil(end_num/20)
        for start in range(2,3,1):
            t.sleep(3)
            a = str(start)
            print("page"+a)
            res, session = getData(session,start,city,checkin,checkout)
            printList(res,checkin,checkout)

def getData(session,start,city,checkin,checkout):
    city_code = getCity()
    url = 'https://hotel.tuniu.com/hotel-api/hotel/list?c=%7B%22ct%22%3A20000%7D'
    r_url = 'https://hotel.tuniu.com/list/{}p0s0b0?checkindate={}&checkoutdate={}&cityName={}&city={}&poi=0&stars=0&brands=0'.format(city_code[city],checkin,checkout,p.quote(city),city_code[city])
    data = {
        "primary": {
            "checkIn": checkin,
            "checkOut": checkout,
            "cityCode": city_code[city],
            "cityType": 0,
            'adultNum': 2,
            "childNum": 0, "childAges": [], "keyword": "", "roomNum": 1
        },
        "secondary": {
            "poi": {"locationType": 2, "pois": []}, "prices": [], "stars": [], "brands": [], "features": [],
            "facilities": [], "commentScore": "", "bedTypes": []
        },
        "threeStages": [], "suggest": {}, "sort": 0, "customerClient": 2,
        "returnDistance": 'true',
        "secondaryDist": {"pValue": "", "userType": 0},
        "pageNo": start,
        "PageSize": 20
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'referer': r_url,
        'cookie': 'tuniu_partner=MTAxLDAsLDlmZDgyZThjYTZkNGMwMTlmZTUyNzdlYjJmNTcxYzQ1; tuniuuser_citycode=MjQwMg%3D%3D; p_phone_400=4007-999-999; p_phone_level=0; p_global_phone=%2B0086-25-8685-9999; _tacau=MCwyOWU0YzIxNi05MWVkLTVkYTYtOTMwMS0xMjdjNGZhZjE1MTUs; _tact=YjI3NWI0YTktMGVlMS02NGQ2LTk1ZDktZTU2ZDZlODA3MmNh; _tacz2=taccsr%3D%28direct%29%7Ctacccn%3D%28none%29%7Ctaccmd%3D%28none%29%7Ctaccct%3D%28none%29%7Ctaccrt%3D%28none%29; _tacc=1; _ga=GA1.2.648685931.1618063126; Hm_lvt_fe3fbe4228e14b1544525f058df92f91=1618063128; UM_distinctid=178bc1406f35f-0da2346b537fa2-71667960-144000-178bc1406f4714; __utmc=1; __utmz=1.1618064085.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=1.648685931.1618063126.1618064085.1618367214.2; PageSwitch=1%2C213612736; _gid=GA1.2.1662076870.1618738929; OLBSESSID=ukudckqscaabvh04kbtnmlss27; ssxmod_itna=iq+xgCG=GQqCq7KGHPoorDBeuIa4f2Ru4GN4G8mDnqD=GFDK40oEyhQD7mFRHiu6Ee0oEGmAWIeqthS7o5A7bBmPoDU4i8DCdmmQbDCeGyKqBQDjxAQDGD73DypPGODAu1dDhxGQcDmLeRtk=9DYE6D7QDCh5IeOvPDq+b+e+QF0httR+YuQxv+n4Y42hPG0GCWhDo9OcCDD34ROcPjiD===; ssxmod_itna2=iq+xgCG=GQqCq7KGHPoorDBeuIa4f2RqA=bG8RFDBdle7pP67qXaD7zx8hBZA1HNYeFcd5x5LG2uH++dTBdufPgn=0HRpZnj3SrYzs1nDc2=2PdIq+lGedyGTLCqH3ZQ/zyay+PLXLXA4x=z08K/RwDUIw5P=Yi4t+dvSMY5R+t4GhGV8iuumenZKGtjtjQ1zM03VL5OAMXClTuVGOh0Bo5tLWRH7au1hdFslEn/3U3iv6jz0lmm+4Esd=tsIMNQ26AiobAQ2bSmRONvIP6wUdZdB/NY4MNjzvMZb8cLENuHunTZaLLqPUI=db=5wl+hDhbp51A=vnqInpyA3sWIV0epoLMjet=UGW2aGpLmEoFtUhQ71i9=rNg=Y9EhPPzCLmjDKIGljDd42xDo7Zh10G7eIT7pPxwx0+xQrQl+eBe1UwP0ET04mPPqnAC+Esn07BfWgfO1qUo6EnwCtPU/KYQPVeqgcQt29b1hmpeYh25Fbebml+p+U4Q=RgEbuZ2gOP99f1DQ1YutbjrRtICmq52Kxr24xbDG2i0DfMUfbQFndD11MravpEu0oD08DijkYD==; checkIn=2021-04-22; checkOut=2021-04-25; _taca=1618063125788.1618738918178.1618745196536.5; _tacb=YWE2Y2FjY2QtYzlhOC0wNGFiLTc5ZjQtN2UwYmI1Y2VhYWIy; CNZZDATA5726564=cnzz_eid%3D1640569903-1618062927-https%253A%252F%252Fwww.tuniu.com%252F%26ntime%3D1618740865; rg_entrance=010000%2F003001%2F000013%2F000000; _pzfxuvpc=1618063125885%7C1202355970107220930%7C27%7C1618745205794%7C4%7C1537570221108570918%7C4488065447683468012; _pzfxsvpc=4488065447683468012%7C1618745198013%7C2%7C; Hm_lpvt_fe3fbe4228e14b1544525f058df92f91=1618745206'
    }
    jdata = json.dumps(data)
    res = session.post(url=url, data=jdata, headers=headers)
    if res.status_code == 403:
        print("ip被封")
    else:

        if start == 1:
            return res, session, json.loads(res.text)["data"]["count"]
        else:
            return res, session

#打印输出
def printList(res,checkin,checkout):
    list = res.text
    ID = re.findall(r'\"hotelId\"\:(.*?)\,', list)
    Name = re.findall(r'\"chineseName\"\:\"(.*?)\"\,', list)
    Score = re.findall(r'\"score\"\:(.*?)\,', list)
    Star = re.findall(r'\"starName\"\:\"(.*?)\"\,', list)
    comment = re.findall(r'\,\"count\"\:(.*?)\}', list)
    Pic = re.findall(r'\"firstPic\"\:\"(.*?)\"\,', list)
    Price = re.findall(r'\"lowestPrice\"\:(.*?)\,', list)
    for i in range(20):
        print('-------------------------------------')
        url = 'https://hotel.tuniu.com/detail/{}?checkindate={}&chckoutdate={}'.format(ID[i],checkin,checkout)
        print(Name[i]+Score[i]+' '+Star[i])
        print(url)
        print(comment[i]+'条住客点评')
        print('CNY '+Price[i])

def main():
    #city = input("目的地:")
    #checkin = input("入住时间 xxxx-xx-xx:")
    #checkout = input("退房时间 xxxx-xx-xx:")
    #getList(city,checkin,checkout)
    getList('济南', '2021-4-24', '2021-4-28')

if __name__ == '__main__':
    main()



