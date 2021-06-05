import requests
import json

url = 'https://b2c.csair.com/portal/flight/direct/query'


headers = {
    "Host": "b2c.csair.com",
    'Connection': 'keep-alive',
    'Content-Length': '227',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Content-Type': 'application/json',
    'Origin': 'https://b2c.csair.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?t=S&c1=BJS&c2=SHA&d1=2021-05-20&at=1&ct=0&it=0&b1=PEK-PKX&b2=SHA-PVG',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    "Cookie": "JSESSIONID=1B41F222F1506C8B374FED8E1815A222; likev_user_id=286b9ea3-071b-4b9a-82c2-49b196d21373; _gscu_422057653=14841486g9gpq115; _gcl_au=1.1.1434185319.1614841509; sid=b59095d034474eaea6e83cf60390dc87; acw_tc=2f6a1feb16189198672307645eae3f333829e951f4f7a59b91e9508488abe3; language=zh_CN; last_session_stm_8mrmut7r76ntg21b=1618919867920; likev_session_id_8mrmut7r76ntg21b=bf51f48d-8f9e-4e9d-d175-16ef2a183583; last_session_id_8mrmut7r76ntg21b=bf51f48d-8f9e-4e9d-d175-16ef2a183583; _gscbrs_422057653=1; WT.al_flight=WT.al_hctype(S)%3AWT.al_adultnum(1)%3AWT.al_childnum(0)%3AWT.al_infantnum(0)%3AWT.al_orgcity1(BJS)%3AWT.al_dstcity1(SHA)%3AWT.al_orgdate1(2021-05-20); ticketBoolingSearch=%7B%22segType%22%3A%22S%22%2C%22adultNum%22%3A%221%22%2C%22childNum%22%3A%220%22%2C%22infantNum%22%3A%220%22%2C%22citys%22%3A%5B%7B%22id%22%3A%22single-formCity%22%2C%22value%22%3A%22%E5%8C%97%E4%BA%AC%22%7D%2C%7B%22id%22%3A%22single-formCityCode%22%2C%22value%22%3A%22BJS%22%7D%2C%7B%22id%22%3A%22isdepair%22%2C%22value%22%3Afalse%7D%2C%7B%22id%22%3A%22single-toCity%22%2C%22value%22%3A%22%E4%B8%8A%E6%B5%B7%22%7D%2C%7B%22id%22%3A%22single-toCityCode%22%2C%22value%22%3A%22SHA%22%7D%2C%7B%22id%22%3A%22isarrair%22%2C%22value%22%3Afalse%7D%5D%2C%22dates%22%3A%5B%7B%22id%22%3A%22single-formCalender%22%2C%22value%22%3A%222021-05-20%22%2C%22minDate%22%3A%22%2B0d%22%7D%5D%7D; WT-FPC=id=222.175.103.33-2839966592.30871748:lv=1618919881920:ss=1618919867913:fs=1614841486574:pn=2:vn=5; _gscs_422057653=18919867kxvwi599|pv:2; likev_session_etm_8mrmut7r76ntg21b=1618919900694; temp_zh=cou%3D1%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-04-20%3B%E5%8C%97%E4%BA%AC-%E4%B8%8A%E6%B5%B7%3B1%2C0%2C0%3B00%3B%26cou%3D2%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-05-05%3B%E5%8D%97%E4%BA%AC-%E6%AD%A6%E6%B1%89%3B1%2C0%2C0%3B00%3B%26cou%3D3%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-06-15%3B%E5%8C%97%E4%BA%AC-%E4%B8%8A%E6%B5%B7%3B1%2C0%2C0%3B00%3B%26cou%3D4%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-05-20%3B%E5%8C%97%E4%BA%AC-%E4%B8%8A%E6%B5%B7%3B1%2C0%2C0%3B00%3B%26cou%3D5%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-05-20%3B%E5%8C%97%E4%BA%AC-%E4%B8%8A%E6%B5%B7%3B1%2C0%2C0%3B00%3B%26",
}


data = {
    "depCity":"PKX",
    "arrCity":"SHA",
    "flightDate":"20210520",
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


r = requests.post(url, json.dumps(data), headers)
print(r.status_code)
print(r.text)
