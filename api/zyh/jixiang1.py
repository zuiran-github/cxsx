import requests
import json

# url = 'http://www.juneyaoair.com/UnitOrderWebAPI/Book/QueryFlightFareNew?' #\
#       # 'flightType=OW&tripType=D&directType=D&' \
#       # 'departureDate=2021-05-12&sendCode=PEK&arrCode=SHA&returnDate='
#
#
# headers = {
#     'Host': 'www.juneyaoair.com',
#     'Proxy-Connection': 'keep-alive',
#     'Content-Length': '324',
#     'Pragma': 'no-cache',
#     'Cache-Control': 'no-cache',
#     'Accept': 'application/json, text/javascript, */*; q=0.01',
#     'X-Requested-With': 'XMLHttpRequest',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
#     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     'Origin': 'http://www.juneyaoair.com',
#     'Referer': 'http://www.juneyaoair.com/pages/Flight/flight.aspx?flightType=OW&sendCity=%E5%8C%97%E4%BA%AC&sendCode=PEK&arrCity=%E4%B8%8A%E6%B5%B7&arrCode=SHA&directType=N&tripType=D&departureDate=2021-05-12&returnDate=2021-05-12',
#     'Accept-Encoding': 'gzip, deflate',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
#     'Cookie': 'ASP.NET_SessionId=0zymuwtk3sm3jegrhdjdmhq0;'
# }
#
#
# data = "flightType=OW" \
#        "&tripType=D" \
#        "&directType=D" \
#        "&departureDate=2021-05-20" \
#        "&sendCode=SHA" \
#        "&arrCode=PKX" \
#        "&returnDate="
#
#
# r = requests.post(url=url, data=data, headers=headers)
# print(r.status_code)
# # print(type(r.text))
# jsdata = json.loads(r.text)['FlightInfoList']
# # print(type(jsdata))
#
# companydict = {
#     "HO": "吉祥航空",
#     "MU": "东方航空"
# }
#
# tzurl = 'http://www.juneyaoair.com/pages/Flight/flight.aspx?' \
#         'flightType=OW' \
#         '&sendCity=%E4%B8%8A%E6%B5%B7' \
#         '&sendCode=SHA' \
#         '&arrCity=%E8%A5%BF%E5%AE%89' \
#         '&arrCode=XIY' \
#         '&directType=N' \
#         '&tripType=D' \
#         '&departureDate=2021-05-18&returnDate=2021-05-18'
#
# dict = {}
# count = 0
# for item in jsdata:
#     # print(type(item))
#     # print(item)
#
#     acity = item['ArrCityName']
#     atime = item['ArrDateTime']
#     dcity = item['DepCityName']
#     dtime = item['DepDateTime']
#
#     date = item['FlightDate']
#
#     flightID = item['CarrierNo']
#
#     company = companydict[flightID[:2]]
#
#     price = int(item['CabinFareList'][1]['PriceValue'])+int(item['CabinFareList'][1]['TaxAmount'])
#
#     cabin = item['CabinFareList'][1]['PriceShowType']
#
#     dict[str(count)] = {'company': company,
#                         'flightID': flightID,
#                         'dCityName': dcity,
#                         'aCityName': acity,
#                         'date': date,
#                         'dTime:': dtime,
#                         'aTime': atime,
#                         'cabin': cabin,
#                         'price': price,
#                         'tzurl': tzurl
#                         }
#     count += 1
#
#
# print(dict)


def donghang(dep, arr, day):
    '''
    吉祥航空&东方航空
    :param dep: 大写城市代码
    :param arr: 大写城市代码
    :param day: 2021-05-16
    :return: 列表
    '''

    # url = 'http://www.juneyaoair.com/UnitOrderWebAPI/Book/QueryFlightFareNew?'
    url = 'http://www.juneyaoair.com/UnitOrderWebAPI/Book/QueryFlightFareNew?' \
          'flightType=OW' \
          '&tripType=D' \
          '&directType=D' \
          '&departureDate=' + day + \
          '&sendCode=' + dep + \
          '&arrCode=' + arr + \
          '&returnDate='

    headers = {
        'Host': 'www.juneyaoair.com',
        'Proxy-Connection': 'keep-alive',
        'Content-Length': '324',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://www.juneyaoair.com',
        'Referer': 'http://www.juneyaoair.com/pages/Flight/flight.aspx?flightType=OW'
                   '&sendCity=%E5%8C%97%E4%BA%AC'
                   '&sendCode=PEK'
                   '&arrCity=%E4%B8%8A%E6%B5%B7'
                   '&arrCode=SHA'
                   '&directType=N'
                   '&tripType=D'
                   '&departureDate=2021-05-12'
                   '&returnDate=2021-05-12',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cookie': 'ASP.NET_SessionId=tzcxr5lwqoxzugwquyrukxcp'
    }

    # cookies = {
    #
    #     'gr_user_id': 'c1705de4-048b-4ba0-959c-e93fa023c7ab',
    #     'c': 'flQgSOpS-1618916693630-0285756e309381847311526',
    #     'ASP.NET_SessionId': 'tzcxr5lwqoxzugwquyrukxcp',
    #     'b9d8f773fb7147ad_gr_session_id': '79bf73d5-9718-48c6-9e32-ddba2c5293a5',
    #     'b9d8f773fb7147ad_gr_session_id_79bf73d5-9718-48c6-9e32-ddba2c5293a5': 'true',
    #     'Hm_lvt_f1c672edeacdaef6cb2e00251b466246': '1618924152,1618977810,1619063082,1620446121',
    #     'TDpx': '1245',
    #     'QueryFlightCookie': 'depCity=SHA&arrCity=XIY&depCityName=\xE4\xB8\x8A\xE6\xB5\xB7&arrCityName=\xE8\xA5\xBF\xE5\xAE\x89',
    #     'security_session_verify': '854840e98b26eccee1903af7ba634ed6',
    #     'Hm_lpvt_f1c672edeacdaef6cb2e00251b466246': '1620446263',
    #     '_fmdata': 'sV4KIG8%2B0k4xMJQF9pOL2v4BaO8jNH9gRVsjpQtcOQt0qWARX0oB8%2BjYMO2WvCMYrknV7IHODIB0klx%2BvOhlgCZey4sU%2FEWBI%2FJMbZYo9Mg%3D',
    #     '_xid': 'NdCd5%2Bj6cdLI5QIe6RhWeChUzAv4b%2BJSoBSvEXtyq8%2BZ2qw8nNggeplS%2FvFz4k457psaps3MCW4ptPc5XY4EPA%3D%3D',
    # }


    data = "flightType=OW" \
           "&tripType=D" \
           "&directType=D" \
           "&departureDate="+day+ \
           "&sendCode="+dep+ \
           "&arrCode="+arr+ \
           "&returnDate="

    data = 'blackbox=eyJ2IjoiKzgzY2FnREJIZFFwdHduMzhDQnQ2ZmVSUHNEK2ZwRGxLMGdzdWlJSEFXcDlZby92ZmdsSExxWDBJT2FzSnQzRCIsIm9zIjoid2ViIiwiaXQiOjQwMCwidCI6IkRnSHk1MXBham1OZVhGaDdiVVpiV0oycThITGhGK1ZrSloxQ0FLR05NSmd3US9TcERwejY3czN3MnlSWGR5R2RtNUtnbmVwVmFmWFNrODdWclFWVTVRPT0ifQ%253D%253D' \
           '&sendCity=%E4%B8%8A%E6%B5%B7' \
           '&arrCity=%E8%A5%BF%E5%AE%89'

    r = requests.post(url=url, headers=headers, data=data, verify=False)
    print(r.status_code)
    # print(r.text)
    jsdata = json.loads(r.text)['FlightInfoList']
    # print(type(jsdata))

    companydict = {
        "HO": "吉祥航空",
        "MU": "东方航空"
    }

    tzurl = 'http://www.juneyaoair.com/pages/Flight/flight.aspx?' \
            'flightType=OW' \
            '&sendCity=%E4%B8%8A%E6%B5%B7' \
            '&sendCode='+dep+ \
            '&arrCity=%E8%A5%BF%E5%AE%89' \
            '&arrCode='+arr+ \
            '&directType=N' \
            '&tripType=D' \
            '&departureDate='+day+ \
            '&returnDate='

    dict = {}
    count = 0
    listfordict = []
    for item in jsdata:
        # print(type(item))
        # print(item)

        acity = item['ArrCityName'] + item['ArrAirportName']
        atime = item['ArrDateTime']
        dcity = item['DepCityName'] + item['DepAirportName']
        dtime = item['DepDateTime']

        date = item['FlightDate']

        flightID = item['CarrierNo']

        company = companydict[flightID[:2]]

        if len(item['CabinFareList']) >1:
            price = int(item['CabinFareList'][1]['PriceValue']) + int(item['CabinFareList'][1]['TaxAmount'])

            cabin = item['CabinFareList'][1]['PriceShowType']

        else:
            price = int(item['CabinFareList'][0]['PriceValue']) + int(item['CabinFareList'][0]['TaxAmount'])

            cabin = item['CabinFareList'][0]['PriceShowType']

        dict[str(count)] = {'company': company,
                            'flightID': flightID,
                            'dCityName': dcity,
                            'aCityName': acity,
                            'date': date,
                            'dTime:': dtime,
                            'aTime': atime,
                            'cabin': cabin,
                            'price': price,
                            'tzurl': tzurl
                            }
        count += 1

        listfordict.append({'company': company,
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

    # print(dict)
    print(listfordict)
    return listfordict

donghang('SHA', 'PEK', '2021-05-20')
