import requests
import json

def nanhang(dep, arr, dayBZ):

    '''
    南方航空
    :param dep: 大写城市代码
    :param arr: 大写城市代码
    :param day: 2021-05-06
    :return: 列表
    '''

    day = dayBZ[:4]+dayBZ[5:7]+dayBZ[8:]  # 南方航空传参要求20210505

    cookies = {
        'JSESSIONID': 'F86101DAA3B76D734D8E0660284E73D3',
        'likev_user_id': '286b9ea3-071b-4b9a-82c2-49b196d21373',
        '_gscu_422057653': '14841486g9gpq115',
        '_gcl_au': '1.1.1434185319.1614841509',
        'sid': 'b59095d034474eaea6e83cf60390dc87',
        'language': 'zh_CN',
        'last_session_stm_8mrmut7r76ntg21b': '1618996887244',
        'likev_session_id_8mrmut7r76ntg21b': '87ebea95-d4cd-4878-de64-ede1c2364c42',
        'last_session_id_8mrmut7r76ntg21b': '87ebea95-d4cd-4878-de64-ede1c2364c42',
        '_gscbrs_422057653': '1',
        'acw_tc': 'ac11000116189968870303046e00ee9035de15d1faa194db5c39af5d30f751',
        'temp_zh': 'cou%3D2%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-05-05%3B%E5%8D%97%E4%BA%AC-%E6%AD%A6%E6%B1%89%3B1%2C0%2C0%3B00%3B%26cou%3D3%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-06-15%3B%E5%8C%97%E4%BA%AC-%E4%B8%8A%E6%B5%B7%3B1%2C0%2C0%3B00%3B%26cou%3D4%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-05-20%3B%E5%8C%97%E4%BA%AC-%E4%B8%8A%E6%B5%B7%3B1%2C0%2C0%3B00%3B%26cou%3D5%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-05-20%3B%E5%8C%97%E4%BA%AC-%E4%B8%8A%E6%B5%B7%3B1%2C0%2C0%3B00%3B%26cou%3D5%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-05-21%3B%E5%8C%97%E4%BA%AC-%E4%B8%8A%E6%B5%B7%3B1%2C0%2C0%3B00%3B%26',
        'WT.al_flight': 'WT.al_hctype(S)%3AWT.al_adultnum(1)%3AWT.al_childnum(0)%3AWT.al_infantnum(0)%3AWT.al_orgcity1(BJS)%3AWT.al_dstcity1(SHA)%3AWT.al_orgdate1(2021-05-21)',
        'ticketBoolingSearch': '%7B%22segType%22%3A%22S%22%2C%22adultNum%22%3A%221%22%2C%22childNum%22%3A%220%22%2C%22infantNum%22%3A%220%22%2C%22citys%22%3A%5B%7B%22id%22%3A%22single-formCity%22%2C%22value%22%3A%22%E5%8C%97%E4%BA%AC%22%7D%2C%7B%22id%22%3A%22single-formCityCode%22%2C%22value%22%3A%22BJS%22%7D%2C%7B%22id%22%3A%22isdepair%22%2C%22value%22%3Afalse%7D%2C%7B%22id%22%3A%22single-toCity%22%2C%22value%22%3A%22%E4%B8%8A%E6%B5%B7%22%7D%2C%7B%22id%22%3A%22single-toCityCode%22%2C%22value%22%3A%22SHA%22%7D%2C%7B%22id%22%3A%22isarrair%22%2C%22value%22%3Afalse%7D%5D%2C%22dates%22%3A%5B%7B%22id%22%3A%22single-formCalender%22%2C%22value%22%3A%222021-05-21%22%2C%22minDate%22%3A%22%2B0d%22%7D%5D%7D',
        'WT-FPC': 'id=222.175.103.33-2839966592.30871748:lv=1618996898914:ss=1618996887237:fs=1614841486574:pn=2:vn=6',
        'likev_session_etm_8mrmut7r76ntg21b': '1618996898919',
        '_gscs_422057653': '18996887ehy4sb99|pv:2',
    }

    headers = {
        'Connection': 'keep-alive',
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
        'Referer': 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?t=S&c1=BJS&c2=SHA&d1=2021-05-21&at=1&ct=0&it=0&b1=PEK-PKX&b2=SHA-PVG',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    data = '{' \
           '"depCity":"'+dep+'",' \
           '"arrCity":"'+arr+'",' \
           '"flightDate":"'+day+'",' \
           '"adultNum":"1",' \
           '"childNum":"0",' \
           '"infantNum":"0",' \
           '"cabinOrder":"0",' \
           '"airLine":1,' \
           '"flyType":0,' \
           '"international":"0",' \
           '"action":"0",' \
           '"segType":"1",' \
           '"cache":0,' \
           '"preUrl":"",' \
           '"isMember":""}'

    response = requests.post('https://b2c.csair.com/portal/flight/direct/query', headers=headers, cookies=cookies,
                             data=data)

    print(response.status_code)

    jsdata = json.loads(response.text)['data']['segment'][0]

    acity = json.loads(response.text)['data']['citys'][0]['zhName']
    dcity = json.loads(response.text)['data']['citys'][1]['zhName']

    list = []
    company = '南方航空'

    tzurl1 = 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?' \
            't=S' \
            '&c1=BJS' \
            '&c2=SHA' \
            '&d1=' + dayBZ + \
            '&at=1' \
            '&ct=0' \
            '&it=0' \
            '&b1=PEK-PKX' \
            '&b2=SHA-PVG'

    tzurl2 = 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?' \
            't=S' \
            '&c1=' + dep + \
            '&c2=' + arr + \
            '&d1=2021-05-21' + dayBZ + \
            '&at=1' \
            '&ct=0' \
            '&it=0' \
            '&b1=' + dep + \
            '&b2=' + arr

    tzurl3 = 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?' \
             't=S' \
             '&c1=SHA' \
             '&c2=BJS' \
             '&d1=' + dayBZ + \
             '&at=1' \
             '&ct=0' \
             '&it=0' \
             '&b1=SHA-PVG' \
             '&b2=PEK-PKX'

    tzurl4 = 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?' \
             't=S' \
             '&c1=BJS' \
             '&c2=' + arr + \
             '&d1=' + dayBZ + \
             '&at=1' \
             '&ct=0' \
             '&it=0' \
             '&b1=PEK-PKX' \
             '&b2=' + arr

    tzurl5 = 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?' \
             't=S' \
             '&c1=SHA' \
             '&c2=' + arr + \
             '&d1=' + dayBZ + \
             '&at=1' \
             '&ct=0' \
             '&it=0' \
             '&b1=SHA-PVG' \
             '&b2=' + arr

    tzurl6 = 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?' \
             't=S' \
             '&c1=' + dep + \
             '&c2=SHA' \
             '&d1=' + dayBZ + \
             '&at=1' \
             '&ct=0' \
             '&it=0' \
             '&b1=' + dep + \
             '&b2=SHA-PVG'

    tzurl7 = 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?' \
             't=S' \
             '&c1=' + dep + \
             '&c2=BJS' \
             '&d1=' + dayBZ + \
             '&at=1' \
             '&ct=0' \
             '&it=0' \
             '&b1=' + dep + \
             '&b2=PEK-PKX'



    if (dep == 'PEK' or dep == 'PKX') and (arr == 'SHA' or arr == 'PVG'):
        tzurl = tzurl1
    elif (dep == 'SHA' or dep == 'PVG') and (arr == 'PEK' or arr == 'PKX'):
        tzurl = tzurl3
    elif dep == 'PEK' or dep == 'PKX':
        tzurl = tzurl4
    elif dep == 'SHA' or dep == 'PVG':
        tzurl = tzurl5
    elif arr == 'SHA' or arr == 'PVG':
        tzurl = tzurl6
    elif arr == 'PEK' or arr == 'PKX':
        tzurl = tzurl7
    else:
        tzurl = tzurl2



    info = jsdata['dateFlight']['flight']
    for i in info:
        date = i['arrDate']
        flightID = i['flightNo']

        atime = i['arrTime'][:2] + ':' + i['arrTime'][2:]
        dtime = i['depTime'][:2] + ':' + i['depTime'][2:]
        # print(atime)

        cabin = i['cabin'][len(i['cabin']) - 1]['adultFareBasis']
        price = i['cabin'][len(i['cabin']) - 1]['adultPrice']

        list.append({'company': company,
                     'flightID': flightID,
                     'dCityName': dcity,
                     'aCityName': acity,
                     'date': date,
                     'dTime:': dtime,
                     'aTime': atime,
                     'cabin': cabin,
                     'price': price,
                     'tzurl': tzurl
                     })
    print(list)

nanhang('XIY', 'PVG', '2021-05-20')







