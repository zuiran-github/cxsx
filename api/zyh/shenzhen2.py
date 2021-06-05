import os
import requests

# $ = os.getenv('$')

cookies = {
    'JSESSIONID': '33331A58C1016F06D49DFD384A980616',
    'x-s3-sid': 'S123Xxuxdpu8514515jur6nzj',
    'A_JNID': '50a67a76e465568dc3f661316e74b937082c880a18de0878aa6e8%3B%3BRMKMXU%2FRqsjuyJ1NrTMVpz6QRkqW74WHtVwy7zyRYKr%2BxBTgUWJGIXC7%2FZ6B0QJAFrRBePesFEbhAiD3zNxIWhe%2FrfJTaF%2FPDjFOUXyJZffitQyTEkptEiVESyKpaENzyMy6mHgzaFxlVlAglWKheNsHv5eTJ8EUdU6xWXRdHE3qTlg5YltOHpKQ2uGb%2B8u%2BmYkHzQ6sU%2FeAk8Uh4Oqrn6QWqX7q3FwOmg2pVwC8CXRXZfcVB43RcMG9t%2F8CqsSY2Ug%2BxuxnHSuguNjmOb%2Bjv4PqFZ8axdnZ3IaLvYrA0eHCFjtpFlVkwwOuPJANk3Xqm%2BwawjmityWiGOYlvEE3%2FH2%2F46zGpKkK57uRPC2Rq5FjnDakbcygfVswgqfRM8k2vHG6IzBhWpGaCLzQf%2FObkA%3D%3D',
    'A_SSID': '440a3f432c39eb7b923e5aabecd298d3',
    '_gscu_1739384231': '188399133q88wx13',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22178ea60c78d5b2-039e2cc5d09aa6-336a7c08-1296000-178ea60c78eea3%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22178ea60c78d5b2-039e2cc5d09aa6-336a7c08-1296000-178ea60c78eea3%22%7D',
    '_gscbrs_1739384231': '1',
    # 'AlteonP': f"A9lSJm9ADgph64lPWgmFEg{$}",
    'x-s3-s4e': 'GPF40SYPcsMb1%2FIFMJd90tysEN0B1vlOJe%2FeymYiRR2h%2BrnqSDqF5ikTiZJvC8%2BA2HaApurPW8K%2F48W35lmwy4aXzm5JYEu3u6cbHXyS4theaJQ6x4HKeKTBdoKKXZQxBKhyaJ4KJ305o84aY%2B0gZI28pqe5ha4D9mzvinL%2Bvu%2BYPvI4ef%2FfmMr89WQ368KRtB6B9kNB07pC0uzNHVX%2BScXQDZKeapNJ1hOC5LKxr3RxDnCAIoDmjNnxX%2FFwaD2lOJlGur6%2FAD6TRDVtv0DugfLJ6Ry3fe1k1cwoxKRFrbsmyVApdWY0stgSqyB6kT5JSLR%2FiyD8Kp9iXqBNfBbbvbE4wzPNKdL4vlEe0fskBrLfgz7SkknGwk5YV%2FPy20IvyrIfq5%2BBuAWi2ybr5ZcMtfFyZFHvWcTije6QzlTlmddWGwNX%2B8fA9Nz554pW%2F7W5qeLJWcSsGnBGjiHic9gysILBTTrkuGxh3F4hAgBpoFw%2BZSZhm4MJb0ci%2B%2FhI%2BEIk8eN1JoIbVHy481pZk7mzPljkVaJk%2BLb8UBuO41s4oN7odKnaUhqjrux62L6K%2FI2rGbVqvqbqlJyxz7EuYmtm2jYZvJpl6g1wvBT0BAHjT1QOyjthxUO%2BM1XH2s%2Bdd2WbZZcGXcDVstx6prPVgg836DXn7wE3tpGB5YVfqRThlko%2Bn4xKXYkrkyT6joMri1hl3sSs6de011ecf3e72b878fcad99eea755382022435fc:LE:fa6039bd-a293-11eb-9343-3cd2e55daed6:ae97f5046e',
    'fromPage': '%7BfromPage%3A%22index%22%7D',
    'sccode': '%7BsccodeInfo%3A%22%u9996%u9875%26%22%7D',
    'x-s3-tid': 'a8ca981c903a9486759070fb690bb7a305f9f259:ir:0537ddf9-a294-11eb-9343-3cd2e55daed6:ae97f50087',
    'A_CKPC': 'NQ6wyyLMogYSwP0%2Ftxaj1WqJTIMi5fsnGSA5JhbdGKrmE8Ukd6s%2FQFxzwHH%2Bo9qdGYdEGMqROj7J7M031tN3e%2FuxnCIj2gnQWBQnKRJ2Fj0HfMtyEFv1YgrBhkLW1UJm9BSYGFcY%2BLMyz3PUogiejgSjp6w9OPjoTL4%2FBh6A9hructX1irA3lFE1YDXpNO4%2BHiz%2Bh5g9VBJvq%2BnwVMEZZnRz8m5KV4wVaXSkminMUt7aS3aQcKReB9hjqq8D4wTI8mPBE8YKISzK6aq%2FuO2PINs%2FsEeG6eIq9wnBlmGklOA%3D',
    '_gscs_1739384231': 't19004219zphely79|pv:2',
}

headers = {
    'Proxy-Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://www.shenzhenair.com',
    'Referer': 'http://www.shenzhenair.com/szair_B2C/flightsearch.action?hcType=DC&constId=&type=%E5%8D%95%E7%A8%8B&orgCity=%E5%B9%BF%E5%B7%9E&orgCityCode=CAN&dstCity=%E4%B8%8A%E6%B5%B7%E8%99%B9%E6%A1%A5&dstCityCode=SHA&orgDate=2021-05-11&dstDate=2021-05-11&quiz=Y&quiz=1',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

data = {
  'condition.orgCityCode': 'CAN',
  'condition.dstCityCode': 'SHA',
  'condition.hcType': 'DC',
  'condition.orgDate': '2021-05-11',
  'condition.dstDate': '2021-05-11'
}

response = requests.post('http://www.shenzhenair.com/szair_B2C/flightSearch.action', headers=headers, cookies=cookies, data=data, verify=False)
