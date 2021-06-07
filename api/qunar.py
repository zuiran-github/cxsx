import requests
import json
import re
import urllib.parse as p
from pypinyin import lazy_pinyin
import time as t
'''
顺序是从 getList->getData获取每页酒店->printList提取数据然后输出
每页20笔
'''
def getCityName(city):
    if city =='天津' or city =='上海' or city =='北京' or city =='重庆':
        citypinyin = "".join(lazy_pinyin(city))+'_city'
        #print(citypinyin)
    else:
        citypinyin = "".join(lazy_pinyin(city))
        #print(citypinyin)
    return citypinyin

def getData(session,start,city,checkin,chekout):
    citypinyin = getCityName(city) #获得城市的拼音
    url = "https://hotel.qunar.com/napi/list"
    # p.quote() 字符转为 %xx 的形式
    r_url = 'https://hotel.qunar.com/cn/{}/?toCity={}&fromDate={}&toDate={}'.format(citypinyin, p.quote(city), checkin, chekout)
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "content-length": "389",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://hotel.qunar.com",
        "referer": r_url,
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        'cookie': 'QN1=00006b80319831417c587f3b; '
                  'HN1=v1b3e65c4cf9b99a2bc4f025fc4f48c09e; '
                  'HN2=quqnqkuqrcugz; _'
                  'i=ueHd86MuqGR9xHjXUKDBTFS9ga1X; '
                  'fid=b73acec9-42e6-42a1-92d4-8c5af8f4d504; '
                  'QN99=9847; QunarGlobal=10.86.213.148_1147fecb_178bbfd264f_-1ff5|1618061814750; '
                  'QN269=D96FF5109A0111EB8723FA163EBA5ACF; QN163=0; QN667=B; '
                  'QN48=tc_ffe1c4bf43f46f07_178bc006815_5608; QN601=92ec0cbf6905809653d3531a2352dfd7;'
                  ' QN243=5; QN57=16180621053660.30429924612820614; QN58=1618062105363%7C1618062105363%7C1; '
                  'QN5=index_tab_remcs; QN25=917f5100-8fb3-4ded-8ec9-a513bbe8973a-9f992f90; QN42=epbf6902; _'
                  'q=U.cddmacs2292; _t=27212209; csrfToken=UoBrbjtqIZmunRMlesraxxuxfehYSEzS; _s=s_5WGM64AQ7VOD4NWOIH27OGKHXY; _'
                  'v=WgGTr_9pulmJuZ-lkG5C15RAm5NqXm548_fc9jMmtMOTZoe_4We5mzaPcTNbKYsWg7s_vqg20oa3XHp2USnpuPhGX5oH0QOL1WbsdWyOyEkEuoE3ERB9Mbn-C7LprVBUumfRkVyn86A-ssoG5-hpnBjHd9i0ZMyZVBODkDbl92H6; '
                  'QN44=cddmacs2292; '
                  'tabIndex=0;  '
                  'QN300=auto_4e0d874a; QN205=auto_4e0d874a; QN277=auto_4e0d874a; QN6=auto_4e0d874a; _'
                  'vi=O5VzVQ5m1qFL3nEuUTNMisybVom9CcDqqqicr76IAu3LETANcZ93eosNrgKTnyF1fi0GjiE09k9dzMhQ92LomyR8CUwWwCdN1JlgOIp6ZJMId2vUUgdZNPW4sTFipEqVJ1mMHiXHT62MPFPvs45xKo4tSQxgzby15acdEpi7geL9; '
                  'JSESSIONID=2C8BBAE59C38A9A4498A2E5BD58C46C0; QN267=1019909321d4bc1a10; QN271=8ec89c49-1aca-4e02-8f3d-534f1287a989; __'
                  'qt=v1%7CVTJGc2RHVmtYMS9HQkdDclNUYTlZRGdxNW5RNDgrRXkrMnl4ODhrV25vY2ZiUlpTZWh1RmNEaFBpMXNPVmpaU0tyREk0U3B6MzU4Zy96QityeGhQVjdhL0hiUXV2RkxuUVVvamR4TVRqclA1SFhQVm9COE9UV2tQaHBNcDVMMUFQWTZqL3JwVForeUNDT0lia3JrZkI5cGNWZTUweHFNd2YwOENUdWt2NTdFPQ%3D%3D%7C1618226989646%7CVTJGc2RHVmtYMTlTYVp6YU4yU1dzOGFxeURpQ2lILzhrdWhzUmNaaHBPYjBiQTVBMlJBN1RuWXpodm5tMVpPZDZydndUWmZWbFRYZEVKVjFmSlNqQ2c9PQ%3D%3D%7CVTJGc2RHVmtYMSthaEQ1aVBhckZpTWNJTndxb2o3SElrenEzQUlRYWloaVV3TXRGcTRsYkUvY0hsamorRmh3Z0s1Slh4M1BmU1N6c3NtN29jZTA4RnJEc0xwNUI0eXlZR3ZXdjRERlN3K2FRV3E4V3hVV21EdTJNQ3BEY3dJajhLUzMvQjMxbElXRHZwNlIzYjNhdzRBVE9aUTEyNU1kdkNhU1FxcERPa3R6RnJLb2FvNGpwTTZvRytDVHFLYjU1cWR6N0lSUDVQeGIzaFNOQmVhV2Q3cjhDN3FqK3NmQmpMQVVRTXY0SXk4cXJDS3o5REtrQnRYMjdXNjlEZkd2b3hiZHo0SEkxQnF2bUJkY0VTMUpWV3pXN0ZWT0hKY0NpcVAwRHRpb1orWldxamZuaSs1c0ZCdWkyY1p4WVJkYTdiLytYbzBVdmdVSWZLd0VucEJDMDFxOWhwYVBpTHdXZDNqR1hYRXdDMUphcVNmcHdmOHE1OEhDQXhvdGhzczNBU3F0YlRPNms1VFJNVTl2UEFmb2xPRWxvcGRlN1JqL0owbStKVkdOcGhpSEluL01RK1pRUENOaVRpREx4d3RnK0FLTGJ6N0xZd1BMZ2txMituZnB3cnNlVEpVdytGWlNNRUlJYitKc0VhRkkzYU1lYlBmUWZuRTByLzV0NzNhTm9pVFBZU1dGZ0tRUVJYeW9KL09peDhqa1h1ZkZJNEpPN1hOZnUxT2pwdDVvVXh2SWdUc1hINWU1SnY2TjFZaFBOKy9raENmcnhJdTRhQXkrTjIrMVJmNmlPNThMZkliN2YxUEJCdzgwWjdRMEZoZHkrZ1F5R1JPdWpBNkpWaTNNOUwyN0lCcjRCcm90TEN1bkJHcGErTktEOWFEQVBOa3dnZjFLWkRDeHhhRVE9'

    }
    data ={
        "b":
            {"bizVersion": "17", "cityUrl": citypinyin, "fromDate": checkin,
             "toDate": chekout, "q": "",#关键字
              "qFrom": 3, "start": start, "num": 20,
             "minPrice": 0, "maxPrice": -1, "level": "", "sort": 0, "cityType": 1,
             "fromForLog": 1, "uuid": "", "userName": "", "userId": "",
             "fromAction": "", "searchType": 0, "hourlyRoom": False,
             "locationAreaFilter": [], "comprehensiveFilter": [],
             "channelId": 1},
             "qrt": "h_hlist", "source": "website"
    }
    jdata = json.dumps(data) #转换成json格式
    res = session.post(url=url, data=jdata, headers=headers)
    print(res.status_code)
    print(res.text)
    if start == 0:
        return res,session,json.loads(res.text)["data"]["tcount"] #酒店总数
    else:
        return res,session

def getList(city,checkin,chekout):
    session = requests.session()#用session保持状态
    start = 0 #页面开始的酒店编号
    res, session, end_num = getData(session,start,city,checkin,chekout)
    print("page1")
    printList(res,city,checkin,chekout)

    #end_num为总共的酒店数，如果只要获取前n页，end_num改成(20*n)
    for start in range(20,40,20):
        t.sleep(2)
        a = str(int(start/20+1))
        print("page"+a)
        res, session = getData(session,start,city,checkin,chekout)
        printList(res,city,checkin,chekout)


#提取数据 打印输出
def printList(res,city,checkin,chekout):
    list = res.text
    citypinyin = getCityName(city)
    Name = re.findall(r'\"name\"\:\"(.*?)\"\,', list)
    ID = re.findall(r'\"seqNo\"\:\".*?\_.*?\_(.*?)\"\,', list)
    pic = re.findall(r'\,\"imageid\"\:\"(.*?)\"\,', list)
    Score = re.findall(r'\"score\"\:\"(.*?)\"\,', list)
    Star = re.findall(r'\"dangciText\"\:\"(.*?)\"\,',list)
    Price = re.findall(r'\"price\"\:\"(.*?)\"\,', list)
    Comment = re.findall(r'\"commentCount\"\:\"(.*?)\"\,', list)
    for i in range(20):
        print('-------------------------------------')
        url = 'https://hotel.qunar.com/cn/{}/dt-{}?fromDate={}&toDate={}/'.format(citypinyin,ID[i],checkin,chekout)
        print(Name[i] + Score[i] + ' ' + Star[i])
        print(pic)
        print(url)
        print(Comment[i] + '条住客点评')
        print('CNY ' + Price[i])

def main():
    #city = input("目的地:")
    #checkin = input("入住时间 xxxx-xx-xx:")
    #chekout = input("退房时间 xxxx-xx-xx:")
    #getList(city, checkin, chekout)

    getList('上海','2021-04-22','2021-04-25')

if __name__ == '__main__':
    main()