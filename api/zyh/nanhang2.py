import requests
import json

listfordict = []
def nanhang(dep, arr, dayBZ):

    '''
    南方航空
    :param dep: 大写城市代码
    :param arr: 大写城市代码
    :param day: 2021-05-06
    :return: 列表
    '''

    try:
        day = dayBZ[:4] + dayBZ[5:7] + dayBZ[8:]  # 南方航空传参要求20210505

        cookies = {
            'JSESSIONID': 'EAD71854B3839A16D2B90410D1A9E077',
            'likev_user_id': '286b9ea3-071b-4b9a-82c2-49b196d21373',
            '_gscu_422057653': '14841486g9gpq115',
            '_gcl_au': '1.1.1434185319.1614841509',
            'sid': 'b59095d034474eaea6e83cf60390dc87',
            'temp_zh': 'cou%3D5%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-05-21%3B%E5%8C%97%E4%BA%AC-%E4%B8%8A%E6%B5%B7%3B1%2C0%2C0%3B00%3B%26cou%3D5%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-05-21%3B%E4%B8%8A%E6%B5%B7-%E5%8C%97%E4%BA%AC%3B1%2C0%2C0%3B00%3B%26cou%3D5%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-05-21%3B%E5%8D%97%E4%BA%AC-%E6%98%86%E6%98%8E%3B1%2C0%2C0%3B00%3B%26cou%3D5%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-05-20%3B%E8%A5%BF%E5%AE%89-%E4%B8%8A%E6%B5%B7%3B1%2C0%2C0%3B00%3B%26cou%3D5%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-05-21%3B%E5%8E%A6%E9%97%A8-%E6%B5%8E%E5%8D%97%3B1%2C0%2C0%3B00%3B%26',
            'ticketBoolingSearch': '%7B%22segType%22%3A%22S%22%2C%22adultNum%22%3A%221%22%2C%22childNum%22%3A%220%22%2C%22infantNum%22%3A%220%22%2C%22citys%22%3A%5B%7B%22id%22%3A%22single-formCity%22%2C%22value%22%3A%22%E5%8E%A6%E9%97%A8%22%7D%2C%7B%22id%22%3A%22single-formCityCode%22%2C%22value%22%3A%22XMN%22%7D%2C%7B%22id%22%3A%22isdepair%22%2C%22value%22%3Afalse%7D%2C%7B%22id%22%3A%22single-toCity%22%2C%22value%22%3A%22%E6%B5%8E%E5%8D%97%22%7D%2C%7B%22id%22%3A%22single-toCityCode%22%2C%22value%22%3A%22TNA%22%7D%2C%7B%22id%22%3A%22isarrair%22%2C%22value%22%3Afalse%7D%5D%2C%22dates%22%3A%5B%7B%22id%22%3A%22single-formCalender%22%2C%22value%22%3A%222021-05-21%22%2C%22minDate%22%3A%22%2B0d%22%7D%5D%7D',
            'language': 'zh_CN',
            'WT.al_flight': 'WT.al_hctype(S)%3AWT.al_adultnum(1)%3AWT.al_childnum(0)%3AWT.al_infantnum(0)%3AWT.al_orgcity1(BJS)%3AWT.al_dstcity1(SHA)%3AWT.al_orgdate1(2021-05-20)',
            '_gscbrs_422057653': '1',
            'ssxmod_itna2': 'GqfhiI4AxIhxXWG7zbG=5DQQit50=qO3=NQOFD6pR=D0vmnh403qQsnbsAK3UD8r46QnYBf7rtYo8dB0+Xe9W4vpo=/jg5I3qFLBrhqA2ihP8utZlD=hFBWIuNGBCuAGUqo7tn4Tn/qLLbuE+8Mp+7GKUD4rqEx=4Lr3V7mo4AOEEYdr14dA9mYf/8kuh+xRrXjYOnQAP162xKD=hWGQzQBYj/O51f2Hnm72HmYT+1f31RnBC/ZXpH9O1+kEsN72KxOY5dLfqeM7y/DgKS3LdCTwneXASK3CS+T4b3whV7y2qqgLMfh7QDKcLKDEFEh7qB57gNt+zOY5QBDxhQM2oDhed4wpgqlD15rwjMYO8srRPmm1X0FwTpUr1XGQ4rk0B1U8ogiY/oYlGQcLa2Bq7D1=bwV+tmW4mrQBlp/MFX8W924Nk4e75N24PaxO8K3QWDeWt4jHbjS7Yk8KSg+E1akTWz2rX16YkYUP7XfjRSLyP628Y+ELnDGqGiPOzUot+LkEfrL3vHQO4xrNO2PE26xYgAb1LTNg1gAh2WuW9=1FYsKXrtt=/1IUzYtcLnREDDwpxHDGcDG7OiDD',
            'acw_tc': '2f6a1fcc16203948788415739e0adb3250520cc8cb757b0bb490ff2712ea5f',
            'ssxmod_itna': 'iqmx9iDt0=i=0QXe0LxYIEPxGgxROG2w77YdqGNLIoDZDiqAPGhDC83tCk+7wAOqqWDsmEnKWz9Gn4xdoWxePh5TTWn4KD=xYQDwxYoDUxGtDpxG6QeIQ/Q8DADi3DEDDeDaxDoDeO50rDY5HDDydDmIHDQv1KlDbUpI1wgPDUQ2wAlBeMADITO24/Br4oeeNpUrxQnDKZWST=BrLvjutFYD',
            'acw_sc__v2': '60954380be853fb5109c43476f3bfdeb58a92abe',
            'WT-FPC': 'id=222.175.103.33-2839966592.30871748:lv=1620394880765:ss=1620394880765:fs=1614841486574:pn=1:vn=14',
            'last_session_stm_8mrmut7r76ntg21b': '1620394880772',
            'likev_session_etm_8mrmut7r76ntg21b': '1620394880772',
            'likev_session_id_8mrmut7r76ntg21b': 'd0ef0cd4-6cfb-4510-9677-3e4c26097981',
            'last_session_id_8mrmut7r76ntg21b': 'd0ef0cd4-6cfb-4510-9677-3e4c26097981',
            '_gscs_422057653': 't20394880shwknd17|pv:1',
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
            'Referer': 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?t=S&c1=BJS&c2=SHA&d1=2021-05-20&at=1&ct=0&it=0&b1=PEK-PKX&b2=SHA-PVG',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        }


        data = '{' \
               '"depCity":"' + dep + '",' \
                                     '"arrCity":"' + arr + '",' \
                                                           '"flightDate":"' + day + '",' \
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
        # print(response.text)

        jsdata = json.loads(response.text)['data']['segment'][0]

        for i in json.loads(response.text)['data']['airports']:
            if i['code'] == dep:
                dcity = i['zhName']
            if i['code'] == arr:
                acity = i['zhName']

        # acity = json.loads(response.text)['data']['citys'][0]['zhName']
        # dcity = json.loads(response.text)['data']['citys'][1]['zhName']

        # list = []
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
                 '&d1=' + dayBZ + \
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

            atime = dayBZ + ' ' + i['arrTime'][:2] + ':' + i['arrTime'][2:] + ':00'
            dtime = dayBZ + ' ' + i['depTime'][:2] + ':' + i['depTime'][2:] + ':00'
            # print(atime)

            arrPort = i['arrPort']
            depPort = i['depPort']


            cabin = i['cabin'][len(i['cabin']) - 1]['adultFareBasis']
            price = i['cabin'][len(i['cabin']) - 1]['adultPrice']

            listfordict.append({
                'company': company,
                'flightID': flightID,
                'dCityName': dcity,
                'aCityName': acity,
                'date': date,
                'dTime': dtime,
                'aTime': atime,
                'cabin': cabin,
                'price': price,
                'tzurl': tzurl
                         })

        print("南方航空搜索完成")
    except:
        print("南方航空报错或未查询到数据")

    return listfordict








#
# cookies = {
#     'JSESSIONID': '2EA81546C9C8907FDA2161AFB6F4F448',
#     'likev_user_id': '286b9ea3-071b-4b9a-82c2-49b196d21373',
#     '_gscu_422057653': '14841486g9gpq115',
#     '_gcl_au': '1.1.1434185319.1614841509',
#     'sid': 'b59095d034474eaea6e83cf60390dc87',
#     'last_session_stm_8mrmut7r76ntg21b': '1619055584510',
#     'last_session_id_8mrmut7r76ntg21b': '1be3306f-dff7-45a1-db6a-37e58c32afe0',
#     'temp_zh': 'cou%3D5%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-05-21%3B%E5%8C%97%E4%BA%AC-%E4%B8%8A%E6%B5%B7%3B1%2C0%2C0%3B00%3B%26cou%3D5%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-05-21%3B%E4%B8%8A%E6%B5%B7-%E5%8C%97%E4%BA%AC%3B1%2C0%2C0%3B00%3B%26cou%3D5%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-05-21%3B%E5%8D%97%E4%BA%AC-%E6%98%86%E6%98%8E%3B1%2C0%2C0%3B00%3B%26cou%3D5%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-05-20%3B%E8%A5%BF%E5%AE%89-%E4%B8%8A%E6%B5%B7%3B1%2C0%2C0%3B00%3B%26cou%3D5%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-05-21%3B%E5%8E%A6%E9%97%A8-%E6%B5%8E%E5%8D%97%3B1%2C0%2C0%3B00%3B%26',
#     'ticketBoolingSearch': '%7B%22segType%22%3A%22S%22%2C%22adultNum%22%3A%221%22%2C%22childNum%22%3A%220%22%2C%22infantNum%22%3A%220%22%2C%22citys%22%3A%5B%7B%22id%22%3A%22single-formCity%22%2C%22value%22%3A%22%E5%8E%A6%E9%97%A8%22%7D%2C%7B%22id%22%3A%22single-formCityCode%22%2C%22value%22%3A%22XMN%22%7D%2C%7B%22id%22%3A%22isdepair%22%2C%22value%22%3Afalse%7D%2C%7B%22id%22%3A%22single-toCity%22%2C%22value%22%3A%22%E6%B5%8E%E5%8D%97%22%7D%2C%7B%22id%22%3A%22single-toCityCode%22%2C%22value%22%3A%22TNA%22%7D%2C%7B%22id%22%3A%22isarrair%22%2C%22value%22%3Afalse%7D%5D%2C%22dates%22%3A%5B%7B%22id%22%3A%22single-formCalender%22%2C%22value%22%3A%222021-05-21%22%2C%22minDate%22%3A%22%2B0d%22%7D%5D%7D',
#     'WT-FPC': 'id=222.175.103.33-2839966592.30871748:lv=1619056561017:ss=1619055584502:fs=1614841486574:pn=7:vn=11',
#     'likev_session_etm_8mrmut7r76ntg21b': '1619056561024',
#     'acw_tc': '2f6a1f8416203906439045955e5e01944640b156aa1aed00f8187a23165ee1',
#     'ssxmod_itna': 'QqUO0KiIeGxAgBDzgD2YL39DmqdSm0pY=Qax0HPi=bDSxGKidDqxBmmjqDtQb=oF275xW45G2hqKAl0jb+3Mi6C8+xf/Gg4GIDeKG2DmeDyDi5GRD0KKbpTLKD3Dm4i3DDxiaDi4DryxBYDmudDGqKDbqQDIMUqKGEyFMURDqDH3hoYp0ve9EeW++DKeOvz/nuz4hAaUAxTp8Pt8Pqt664DG8DmlE4xD',
#     'ssxmod_itna2': 'QqUO0KiIeGxAgBDzgD2YL39DmqdSm0pY=BDn9Eqi=CDl1GDjbcfQMMx6/hMD6q8Ql6T9DHoD3MaR3emxD5HQAxPBnfK29iKh6Wp4ApGaj39FPtr1PFy4hjaVUHB3WgU+6cQdOkXAHh658aeviRmH7farPZayNQ9ps=rcdcrB8cPmtxKEt+arb9iysoOEaVnoaVCS=bFHwVD3a=48i902oDQ9iDjKD+2GDD==',
#     'language': 'zh_CN',
#     'WT.al_flight': 'WT.al_hctype(S)%3AWT.al_adultnum(1)%3AWT.al_childnum(0)%3AWT.al_infantnum(0)%3AWT.al_orgcity1(BJS)%3AWT.al_dstcity1(SHA)%3AWT.al_orgdate1(2021-05-20)',
#     'acw_sc__v2': '609532f5342955e58f02a3dadfcd2e3053917892',
# }
#
# headers = {
#     'Connection': 'keep-alive',
#     'Pragma': 'no-cache',
#     'Cache-Control': 'no-cache',
#     'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
#     'Accept': 'application/json, text/javascript, */*; q=0.01',
#     'X-Requested-With': 'XMLHttpRequest',
#     'sec-ch-ua-mobile': '?0',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
#     'Content-Type': 'application/json',
#     'Origin': 'https://b2c.csair.com',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Dest': 'empty',
#     'Referer': 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?t=S&c1=BJS&c2=SHA&d1=2021-05-20&at=1&ct=0&it=0&b1=PEK-PKX&b2=SHA-PVG',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
# }
#
#
# data = '{"depCity":"PKX","arrCity":"SHA","flightDate":"20210521","adultNum":"1","childNum":"0","infantNum":"0","cabinOrder":"0","airLine":1,"flyType":0,"international":"0","action":"0","segType":"1","cache":0,"preUrl":"","isMember":""}'
#
# response = requests.post('https://b2c.csair.com/portal/flight/direct/query', headers=headers, cookies=cookies, data=data)
#
# print(response.status_code)
# # print(response.text)
#
# jsdata = json.loads(response.text)['data']['segment'][0]
#
# acity = json.loads(response.text)['data']['citys'][1]['zhName']
# dcity = json.loads(response.text)['data']['citys'][0]['zhName']
#
#
# list = []
# company = '南方航空'
#
# tzurl = 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?' \
#         't=S' \
#         '&c1=BJS' \
#         '&c2=SHA' \
#         '&d1=2021-05-21' \
#         '&at=1' \
#         '&ct=0' \
#         '&it=0' \
#         '&b1=PEK-PKX' \
#         '&b2=SHA-PVG'
#
# info = jsdata['dateFlight']['flight']
# for i in info:
#
#     date = i['arrDate']
#     flightID = i['flightNo']
#
#     atime = i['arrTime'][:2] + ':' + i['arrTime'][2:]
#     dtime = i['depTime'][:2] + ':' + i['depTime'][2:]
#     # print(atime)
#
#     cabin = i['cabin'][len(i['cabin'])-1]['adultFareBasis']
#     price = i['cabin'][len(i['cabin'])-1]['adultPrice']
#
#     list.append({'company': company,
#                  'flightID': flightID,
#                  'dCityName': dcity,
#                  'aCityName': acity,
#                  'date': date,
#                  'dTime:': dtime,
#                  'aTime': atime,
#                  'cabin': cabin,
#                  'price': price,
#                  'tzurl': tzurl
#                             })
#
#
#
# #############################################
#
# #
# # cookies = {
# #     'JSESSIONID': 'F86101DAA3B76D734D8E0660284E73D3',
# #     'likev_user_id': '286b9ea3-071b-4b9a-82c2-49b196d21373',
# #     '_gscu_422057653': '14841486g9gpq115',
# #     '_gcl_au': '1.1.1434185319.1614841509',
# #     'sid': 'b59095d034474eaea6e83cf60390dc87',
# #     'language': 'zh_CN',
# #     'last_session_stm_8mrmut7r76ntg21b': '1618996887244',
# #     'likev_session_id_8mrmut7r76ntg21b': '87ebea95-d4cd-4878-de64-ede1c2364c42',
# #     'last_session_id_8mrmut7r76ntg21b': '87ebea95-d4cd-4878-de64-ede1c2364c42',
# #     '_gscbrs_422057653': '1',
# #     'acw_tc': 'ac11000116189968870303046e00ee9035de15d1faa194db5c39af5d30f751',
# #     'temp_zh': 'cou%3D2%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-05-05%3B%E5%8D%97%E4%BA%AC-%E6%AD%A6%E6%B1%89%3B1%2C0%2C0%3B00%3B%26cou%3D3%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-06-15%3B%E5%8C%97%E4%BA%AC-%E4%B8%8A%E6%B5%B7%3B1%2C0%2C0%3B00%3B%26cou%3D4%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-05-20%3B%E5%8C%97%E4%BA%AC-%E4%B8%8A%E6%B5%B7%3B1%2C0%2C0%3B00%3B%26cou%3D5%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-05-20%3B%E5%8C%97%E4%BA%AC-%E4%B8%8A%E6%B5%B7%3B1%2C0%2C0%3B00%3B%26cou%3D5%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2021-05-21%3B%E5%8C%97%E4%BA%AC-%E4%B8%8A%E6%B5%B7%3B1%2C0%2C0%3B00%3B%26',
# #     'WT.al_flight': 'WT.al_hctype(S)%3AWT.al_adultnum(1)%3AWT.al_childnum(0)%3AWT.al_infantnum(0)%3AWT.al_orgcity1(BJS)%3AWT.al_dstcity1(SHA)%3AWT.al_orgdate1(2021-05-21)',
# #     'ticketBoolingSearch': '%7B%22segType%22%3A%22S%22%2C%22adultNum%22%3A%221%22%2C%22childNum%22%3A%220%22%2C%22infantNum%22%3A%220%22%2C%22citys%22%3A%5B%7B%22id%22%3A%22single-formCity%22%2C%22value%22%3A%22%E5%8C%97%E4%BA%AC%22%7D%2C%7B%22id%22%3A%22single-formCityCode%22%2C%22value%22%3A%22BJS%22%7D%2C%7B%22id%22%3A%22isdepair%22%2C%22value%22%3Afalse%7D%2C%7B%22id%22%3A%22single-toCity%22%2C%22value%22%3A%22%E4%B8%8A%E6%B5%B7%22%7D%2C%7B%22id%22%3A%22single-toCityCode%22%2C%22value%22%3A%22SHA%22%7D%2C%7B%22id%22%3A%22isarrair%22%2C%22value%22%3Afalse%7D%5D%2C%22dates%22%3A%5B%7B%22id%22%3A%22single-formCalender%22%2C%22value%22%3A%222021-05-21%22%2C%22minDate%22%3A%22%2B0d%22%7D%5D%7D',
# #     'WT-FPC': 'id=222.175.103.33-2839966592.30871748:lv=1618996898914:ss=1618996887237:fs=1614841486574:pn=2:vn=6',
# #     'likev_session_etm_8mrmut7r76ntg21b': '1618996898919',
# #     '_gscs_422057653': '18996887ehy4sb99|pv:2',
# # }
# #
# # headers = {
# #     'Connection': 'keep-alive',
# #     'Pragma': 'no-cache',
# #     'Cache-Control': 'no-cache',
# #     'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
# #     'Accept': 'application/json, text/javascript, */*; q=0.01',
# #     'X-Requested-With': 'XMLHttpRequest',
# #     'sec-ch-ua-mobile': '?0',
# #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
# #     'Content-Type': 'application/json',
# #     'Origin': 'https://b2c.csair.com',
# #     'Sec-Fetch-Site': 'same-origin',
# #     'Sec-Fetch-Mode': 'cors',
# #     'Sec-Fetch-Dest': 'empty',
# #     'Referer': 'https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?t=S&c1=BJS&c2=SHA&d1=2021-05-21&at=1&ct=0&it=0&b1=PEK-PKX&b2=SHA-PVG',
# #     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
# # }
# #
# # data1 = '{"depCity":"PKX","arrCity":"PVG","flightDate":"20210521","adultNum":"1","childNum":"0","infantNum":"0","cabinOrder":"0","airLine":1,"flyType":0,"international":"0","action":"0","segType":"1","cache":0,"preUrl":"","isMember":""}'
# #
# # response1 = requests.post('https://b2c.csair.com/portal/flight/direct/query', headers=headers, cookies=cookies, data=data1)
# #
# # print(response1.status_code)
# # # print(response.text)
# #
# # jsdata = json.loads(response1.text)['data']['segment'][0]
# #
# # acity = json.loads(response1.text)['data']['citys'][0]['zhName']
# # dcity = json.loads(response1.text)['data']['citys'][1]['zhName']
# #
# #
# #
# #
# # info = jsdata['dateFlight']['flight']
# # for i in info:
# #
# #     date = i['arrDate']
# #     flightID = i['flightNo']
# #
# #     atime = i['arrTime'][:2] + ':' + i['arrTime'][2:]
# #     dtime = i['depTime'][:2] + ':' + i['depTime'][2:]
# #     # print(atime)
# #
# #     cabin = i['cabin'][len(i['cabin'])-1]['adultFareBasis']
# #     price = i['cabin'][len(i['cabin'])-1]['adultPrice']
# #
# #     list.append({'company': company,
# #                  'flightID': flightID,
# #                  'dCityName': dcity,
# #                  'aCityName': acity,
# #                  'date': date,
# #                  'dTime:': dtime,
# #                  'aTime': atime,
# #                  'cabin': cabin,
# #                  'price': price,
# #                  'tzurl': tzurl
# #                             })
# #
# #
# #
# # dict = {"data": list}
# print(list)
