import requests

cookies = {
    'ASP.NET_SessionId': '0zymuwtk3sm3jegrhdjdmhq0',
    'gr_user_id': 'c1705de4-048b-4ba0-959c-e93fa023c7ab',
    'c': 'flQgSOpS-1618916693630-0285756e309381847311526',
    'QueryFlightCookie': 'depCity=PEK&arrCity=SHA&depCityName=\xE5\u0152\u2014\xE4\xBA\xAC&arrCityName=\xE4\xB8\u0160\xE6\xB5\xB7',
    'b9d8f773fb7147ad_gr_session_id': 'ea37510f-d3aa-4c6e-a679-5eea196fffbd',
    'Hm_lvt_f1c672edeacdaef6cb2e00251b466246': '1618916693,1618924152',
    'b9d8f773fb7147ad_gr_session_id_ea37510f-d3aa-4c6e-a679-5eea196fffbd': 'true',
    'TDpx': '0',
    'Hm_lpvt_f1c672edeacdaef6cb2e00251b466246': '1618924176',
    '_fmdata': 'sV4KIG8%2B0k4xMJQF9pOL2v4BaO8jNH9gRVsjpQtcOQt0qWARX0oB8%2BjYMO2WvCMYxFbjP%2FWIx9IlwHNGenkQRXGK36NVh0CTsqJ%2F4UsXy5c%3D',
    '_xid': 'jIXrMS1XiNahQv9o36zSt%2BSY8r65UcSsx26yshlf4lVQKzPakL5joaoVj6uctMrymcy%2B6ymWwwswJg07erMrNQ%3D%3D',
    'security_session_verify': '3b925bb3d1938c90088f9a8e13877150',
}

headers = {
    'Proxy-Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://www.juneyaoair.com',
    'Referer': 'http://www.juneyaoair.com/pages/Flight/flight.aspx?flightType=OW&sendCity=%E5%8C%97%E4%BA%AC&sendCode=PEK&arrCity=%E4%B8%8A%E6%B5%B7&arrCode=SHA&directType=N&tripType=D&departureDate=2021-05-19&returnDate=2021-05-19',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

params = (
    ('flightType', 'OW'),
    ('tripType', 'D'),
    ('directType', 'D'),
    ('departureDate', '2021-05-19'),
    ('sendCode', 'PEK'),
    ('arrCode', 'SHA'),
    ('returnDate', ''),
)

data = {
  'blackbox': 'eyJ2IjoiV1JRWlkxMmVmNDhhT3h3RDN2ZmZvY1Q1TWh2aVFTbjIvVWNQSTMrZHZ2TllVK2s5WmpZVGlIZ25RelgrcXFWTyIsIm9zIjoid2ViIiwiaXQiOjYyOSwidCI6ImZzQ2YyUmMwUHNyb1h1LytiZ3R2eDkxMWhHOEdtbFVQV0JUc1RVZldrSUp3cmd4RXI0ek90cXVYaXhQeXBMZzJ0L3JSMm4zT0ZKemd0TmFEQ3FId2lRPT0ifQ%3D%3D',
  'sendCity': '\u5317\u4EAC',
  'arrCity': '\u4E0A\u6D77'
}

# response = requests.post('http://www.juneyaoair.com/UnitOrderWebAPI/Book/QueryFlightFareNew', headers=headers, params=params, cookies=cookies, data=data, verify=False)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
response = requests.post('http://www.juneyaoair.com/UnitOrderWebAPI/Book/QueryFlightFareNew?flightType=OW&tripType=D&directType=D&departureDate=2021-05-19&sendCode=PEK&arrCode=SHA&returnDate=', headers=headers, cookies=cookies, data=data, verify=False)


print(response.status_code)
print(response.text)