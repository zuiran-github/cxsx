import requests

cookies = {
    'JSESSIONID': 'B51648B2A08D4E138E9C38CDB859FAB5.CHIBEServer10348220.49.1',
    'Webtrends': '58.194.169.213.1620658108555842',
    'X-LB': '2.1d0.20c98750.50',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2217956c03d55280-065781a6932f9e-336a7c08-1296000-17956c03d56b1e%22%2C%22%24device_id%22%3A%2217956c03d55280-065781a6932f9e-336a7c08-1296000-17956c03d56b1e%22%7D',
    'sajssdk_2015_cross_new_user': '1',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Dest': 'document',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'Referer': 'https://www.sichuanair.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

params = (
    ('telassa-id', 'IbeNotLogin~E7D8741D77B6BA7705684F8B0F935979~3u-dev-PRD-0adc3101-450182-130646'),
    ('_catRootMessageId', '3u-dev-PRD-0adc3101-450182-130646'),
    ('_catParentMessageId', '3u-dev-PRD-0adc3101-450182-130646'),
    ('_catChildMessageId', '3u-dev-PRD-0adc3101-450182-130717'),
)

response = requests.get('https://flights.sichuanair.com/3uair/ibe/ticket/bjs-ctu.html', headers=headers, params=params, cookies=cookies)
print(response.status_code)
print(response.text)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://flights.sichuanair.com/3uair/ibe/ticket/bjs-ctu.html?telassa-id=IbeNotLogin%7EE7D8741D77B6BA7705684F8B0F935979%7E3u-dev-PRD-0adc3101-450182-130646&_catRootMessageId=3u-dev-PRD-0adc3101-450182-130646&_catParentMessageId=3u-dev-PRD-0adc3101-450182-130646&_catChildMessageId=3u-dev-PRD-0adc3101-450182-130717', headers=headers, cookies=cookies)
