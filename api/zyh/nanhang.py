import requests
import json


def nanhang(dep, arr, date):

    url = 'https://b2c.csair.com/portal/flight/direct/query'

    headers = {
        'Accept': 'application/json, text/javascript, */*, q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?t=S&c1=BJS&c2=SHA&d1=2021-06-15&at=1&ct=0&it=0&b1=PEK-PKX&b2=SHA-PVG',
        'sec-ch-ua': 'Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': 'JSESSIONID=EB6333D2B247C8014287F8A1277F56E5; likev_user_id=286b9ea3-071b-4b9a-82c2-49b196d21373; _gscu_422057653=14841486g9gpq115; _gcl_au=1.1.1434185319.1614841509; sid=b59095d034474eaea6e83cf60390dc87; acw_tc=2f6a1faf16188369825198387e41edea8f9dbefbd2fc67402daf0f4a1231b6; language=zh_CN; last_session_stm_8mrmut7r76ntg21b=1618836984229; likev_session_id_8mrmut7r76ntg21b=079940fa-3cde-475a-ee16-157a2763566d; last_session_id_8mrmut7r76ntg21b=079940fa-3cde-475a-ee16-157a2763566d; _gscbrs_422057653=1; temp_zh=cou%3D0%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-04-20%3B%E5%8C%97%E4%BA%AC-%E5%8D%97%E4%BA%AC%3B1%2C0%2C0%3B00%3B%26cou%3D1%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-04-20%3B%E5%8C%97%E4%BA%AC-%E4%B8%8A%E6%B5%B7%3B1%2C0%2C0%3B00%3B%26cou%3D2%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-05-05%3B%E5%8D%97%E4%BA%AC-%E6%AD%A6%E6%B1%89%3B1%2C0%2C0%3B00%3B%26cou%3D3%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-06-15%3B%E5%8C%97%E4%BA%AC-%E4%B8%8A%E6%B5%B7%3B1%2C0%2C0%3B00%3B%26; WT.al_flight=WT.al_hctype(S)%3AWT.al_adultnum(1)%3AWT.al_childnum(0)%3AWT.al_infantnum(0)%3AWT.al_orgcity1(BJS)%3AWT.al_dstcity1(SHA)%3AWT.al_orgdate1(2021-06-15); ticketBoolingSearch=%7B%22segType%22%3A%22S%22%2C%22adultNum%22%3A%221%22%2C%22childNum%22%3A%220%22%2C%22infantNum%22%3A%220%22%2C%22citys%22%3A%5B%7B%22id%22%3A%22single-formCity%22%2C%22value%22%3A%22%E5%8C%97%E4%BA%AC%22%7D%2C%7B%22id%22%3A%22single-formCityCode%22%2C%22value%22%3A%22BJS%22%7D%2C%7B%22id%22%3A%22isdepair%22%2C%22value%22%3Afalse%7D%2C%7B%22id%22%3A%22single-toCity%22%2C%22value%22%3A%22%E4%B8%8A%E6%B5%B7%22%7D%2C%7B%22id%22%3A%22single-toCityCode%22%2C%22value%22%3A%22SHA%22%7D%2C%7B%22id%22%3A%22isarrair%22%2C%22value%22%3Afalse%7D%5D%2C%22dates%22%3A%5B%7B%22id%22%3A%22single-formCalender%22%2C%22value%22%3A%222021-06-15%22%2C%22minDate%22%3A%22%2B0d%22%7D%5D%7D; _gscs_422057653=188369847iar4299|pv:3; WT-FPC=id=222.175.103.33-2839966592.30871748:lv=1618837023971:ss=1618836984217:fs=1614841486574:pn=3:vn=4; likev_session_etm_8mrmut7r76ntg21b=1618837023976',
        'Host': 'b2c.csair.com',
        'Origin': 'https://b2c.csair.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }

    data = {
        "depCity":"PKX",
        "arrCity":"SHA",
        "flightDate":"20210615",
        "adultNum":"1",
        "childNum":"0",
        "infantNum":"0",
        "cabinOrder":"0",
        "airLine":1,
        "flyType":0,
        "international":"0",
        "action":"0",
        "segType":"1",
        "cache":0,
        "preUrl":"",
        "isMember":""
    }

    jsdata = json.dumps(date)
    r = requests.post(url, jsdata, headers)
    print(r.status_code)

    jsdata1 = json.loads(r.text)
    print(jsdata1)


nanhang(1,1,1)