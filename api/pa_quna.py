import requests
from bs4 import BeautifulSoup
import re
import my_fake_useragent as mfu
from fuzzywuzzy import process
from lxml import etree
from time import sleep
import traceback
import json

class QunaSpider:
    def __init__(self):
        user_agent = mfu.UserAgent()
        self.headers = {
            "User-Agent": user_agent.random(),
            "Cookie": "QN1=00006700306c31a87bc0c086; QN99=7358; QunarGlobal=10.86.213.148_1147fecb_178ee43b1e9_2f84|1618905465741; _i=ueHd86MuqdAuqc1AU6CwyeJQnI1X; QN601=9d3319d52ed7a25675d2802fd36a5283; QN48=000080802f1031a87bd81b32; QN269=CED74FF0269211EB9D3EFA163E6279D9; fid=121d0b6b-732b-4505-a294-09125f85e731; QN243=10; __guid=11325109.3948886401476819500.1618905602258.9663; QN57=16189056035600.7784914755548995; QN71=\"NTguMTk0LjE2OS4xNTI65rWO5Y2XOjE=\"; QN63=%E6%B5%8E%E5%8D%97%E5%8A%A8%E7%89%A9%E5%9B%AD%7C%E6%96%B9%E7%89%B9%7C%E6%96%B9%E7%89%B9%5B%E6%B5%8E%E5%8D%97%5D%7C%E6%B5%8E%E5%8D%97%E6%96%B9%E7%89%B9%7C%E8%A5%BF%E5%AE%89%E8%B6%B5%E7%AA%81%E6%B3%89%7C%E8%A5%BF%E5%AE%89%E8%B6%B5%E7%AA%81%E6%B3%89%5B%E8%A5%BF%E5%AE%89%5D%7C%E8%B6%B5%E7%AA%81%E6%B3%89%5B%E8%A5%BF%E5%AE%89%5D%7C%E8%B6%B5%E7%AA%81%E6%B3%89%5B%E6%B5%8E%E5%8D%97%5D%7C%E6%B5%8E%E5%8D%97%E6%B5%8E%E5%8D%97%E6%96%B9%E7%89%B9%7C%E6%B5%8E%E5%8D%97%E6%B5%8E%E5%8D%97%E5%8A%A8%E7%89%A9%E5%9B%AD%7C%E5%8A%A8%E7%89%A9%E5%9B%AD%7C%E6%B5%8E%E5%8D%97%E8%B6%B5%E7%AA%81%E6%B3%89; QN67=192250%2C215559%2C215527%2C196094; QN300=auto_5187810b; QN205=auto_5187810b; QN277=auto_5187810b; csrfToken=xpmqALG4a1v9B6SPTPrrPvw1BIlPx9cW; _vi=Eu0g5Wp7dQrg0p1IjSzpGhsekm3dIncKdeqvEM6UEH53RJHZwZYwUg6-9Z7qIeQ-dY4mmbanXaCXddc1Qz5Ae-KTUP9FC9kkgd9aSVCWatKEmkPMVB0WtufBrsomWIvhB1sUu2D9pSNGvNQEi1Bqhq4-BugojwQXWHtoqZFk-fFF; QN163=0; QN6=auto_5187810b; Hm_lvt_15577700f8ecddb1a927813c81166ade=1618905605,1619009041; QN58=1619009039769%7C1619009268902%7C5; Hm_lpvt_15577700f8ecddb1a927813c81166ade=1619009269; QN271=66845d5b-78e4-422a-a910-8e3fa1b0012b; __qt=v1%7CVTJGc2RHVmtYMStaN3RCUnBkVmZ5enF0ZmdOZVdCcmUvU3pQazFZZkZjSkVlbW5qK3h1RWhidzJMNWtPeUFNWXJBOWE3bk9uZVM5QWNzUmN5cUdyTzFsSHZ4VlVJZFBuN1RDazVkMU03TjZpOGhnVVo4WWRpczAxMnkrbEhnOVc0L3Fabk9ZTUliRlFEbzNocHBwY25BdEJockpPdmQyYU5sS01NZmpna2cwPQ%3D%3D%7C1619009279624%7CVTJGc2RHVmtYMTlxME1tOVYvVHp4YjJRSm5LU3NNMjM0QVk3WWxmbE1TcVZ0eG5KRGZKSzQwb0ZkUDlZNjdQcGdBajk3a2d0UnZERnk5akZ5WWZRemc9PQ%3D%3D%7CVTJGc2RHVmtYMS9BSFJJa3RsMTNjUmd4VS85UmhiQjcycUE2ZFAxWlBxVXo2dThObmRJcGkwSjQ2MUU5alNhNENEaEFqUzZKNUdrMjloWTRiYjkvaWdkTzhlYkM5VjJEalhDaGZldThWZjV4WHN4N01BMDhvYlk3ZVdHSjZwQ3Z2Q0drayt6ays0a2xOMTdTdjRnK1NzNEIwSm9INEJOdC8yMGc2ZG1Hak4wK3J5ME5nWHU1N0hBWlpacVdjZDFwK04rNzVoUTl1alE2cWxqNXY4UGdpb0owMFBGOEtlU2hTZklqcWRRcEdwOVRCN280cVA0dFcvc2lmMlZXZGJwc09jbkk1K2Z5bjEyUk9nS0hBTm10RWQ2UmZjWW53cW1TRnFYRFdXUkc1bUhwWlpCc0wzQzlyVFNCTFo3S21oTDBaMm1NdkFhczRSWUJqc242MnhxbFJLTUt5YnM1QkVmc21KVVZxTXdweHU2N29qUzdRSW1WS0pHVElzNk1tQUQxbU9BQU1QYjBmTzBWLzh2anJBNjlacTAvbzQ4V0JTd2U2WWVBb1dSOUpQWk9DUmJvWlhXaGpJS1JXdWJWcE1LKytrblE5L1BoRDBBemNMWmduVXBiWWd2MTdhdTJ3eDRxUS9mV0g0TXEvdXFSV0xKT1ByT3FYdG9xbGF0L2loUmdzOHZ1bnFDay9rNVljUmdvTXhxVkJhSjJ4My91MXU5UGxPT3dKSUJHWTh5NTdmK3REWFAwSFhrbWpaUzlsTEx3WWZZMTNYbGViMTV5WjBGa2E5dDZsU1Y5bTJWVzF3VkFCMi92M2djamtmM3N4aE51SXFlVFNhVTR3NVBYNkhDSFcvTjM1U2xqRVg2WnNyZEY4dGE4VHhqcEtDdjdLZVRoenlQUWVZNno3NEtXbm1HTE9VVWtYSlZ2c0ZwZWs1YkdLSjc3Z1pKd3FUZ3pOcUdsRUlqVFhLWUpYUWhGMVhMbUtDandqS0h6NHJ1Z3RzNEErcGVJR3ZJNE5VdXBYWVFoWkFUaExzT1d5Z3lMOStYRUxNT2dzNjU5c1lIL2cvMVE2OHljZnJ5TlVYSmp3eVVWMFlBdlpFSFQzSWNkTDdDdw%3D%3D; JSESSIONID=7EC69B67C1BFEDFA17C8CE319CC33E4F; monitor_count=6; QN267=012553093731ef52626",
        }
        self.start_url = "https://piao.qunar.com/"
        self.cityList = {}
        self.spots = []
        self.tickets = []

    def getHtml(self, url):
        try:
            self.headers['User-Agent'] = mfu.UserAgent().random()
            #self.headers['Cookie'] = '__guid=131352329.2117375357185893600.1618750037696.1821; p_phone_400=4007-999-999; p_phone_level=0; p_global_phone=%2B0086-25-8685-9999; _tacau=MCw4NjkwMmRjMi0yMmMxLWFlZmUtNTc5NC1jNzRlYTliNmI0OTUs; _tact=MGZhZmNjMTgtZjZmNC04ODJlLTNiM2YtMTdhOThlMzVmM2Vj; _tacz2=taccsr%3D%28direct%29%7Ctacccn%3D%28none%29%7Ctaccmd%3D%28none%29%7Ctaccct%3D%28none%29%7Ctaccrt%3D%28none%29; _ga=GA1.2.697330034.1618750045; _gid=GA1.2.1481901232.1618750045; PageSwitch=1%2C213612736; _uab_collina=161875004597741912116211; smidV2=20210418204730d1a4357137884d6a8cfbb49e7a12f61100f9c9152ac53cc00; tuniu_partner=MTUyOTEsMCwsYzQ1YjA0MjRjZDliMzA4ZDU0NzE5Y2I2ODlhOWE5NzA%3D; isHaveShowPriceTips=1; Hm_lvt_51d49a7cda10d5dd86537755f081cc02=1618758988; tuniuuser_ip_citycode=MTAwOA==; tuniuuser_citycode=MjQwMg%3D%3D; acw_tc=76b20ff416188267636778763e3a7822abed332150bd271d4eed81997d2dcd; acw_sc__v2=607d560ba2d2f37cbacad0ffc568e1b0c8dfb234; monitor_count=8; _taca=1618750044531.1618758928733.1618826770234.3; _tacb=ZjJlODliNGEtMDZlZS0zZmUyLTYzYzctNzRlMGViM2ZmMWUy; _tacc=1; _pzfxuvpc=1618750044912%7C1057153772146331711%7C7%7C1618826770299%7C4%7C1503591366559265886%7C7335018051316751874; _pzfxsvpc=7335018051316751874%7C1618826770291%7C1%7Chttp%3A%2F%2Fwww.tuniu.com%2F; Hm_lvt_fe3fbe4228e14b1544525f058df92f91=1618750046,1618758937,1618826770; Hm_lpvt_fe3fbe4228e14b1544525f058df92f91=1618826770; OLBSESSID=6eb605kbelogi1uge3rju4gm36; ssxmod_itna=CqAx97qQqDqrDXYG7GTueGTKYT3EQW2rA7x0yei=iDSxGKidDqxBeWQrKqe5qv3KOKC3AEoDR2H3hQbEmuomTWCRoX3DU4i8DCTx5YOGDYA8Dt4DTD34DYDixib1xi5GRD09kDbxYp9DWPDYxDr61KDRxi7DDydkx07DQHkKnikeUP+9xo13iBeTnKD9ooDsE+EQnKwvI3qZ1RODl9jDCKz9c9Ci4GdZi0omDxNCQI24TG3SQG3qmrPqi+xx64NGOioKNDbFijyQDDWT00YiA+DD; ssxmod_itna2=CqAx97qQqDqrDXYG7GTueGTKYT3EQW2rADnIgiKitCQDlE70xjRDueZ3Pw2ktGFWik4hsn7iei=Xb4Qvb7tugfo=GeAPRfi+Tt+pBD0qv0Q7gQXfxWgRcH1NOajLqYSdB3+nONgUO0ZmCKPneoZ5HTWT+/2Y1txYTtpawHOGF3DFt3AO=oh0I+1Wb1bSAqafIEfahHpuPcxeww=njBokOwpaHoUyTn/uW0t9XTAMdyxlA8CP5W22NUZeICe=xWFwEhCpQnirQTLiF3lP5V+==CjSneA68mBCKfke53sUFg=VjoZj0XFqtAIEgKLZ+s=XRofKDv/aXUEUuGmr2ID4w3/Kza=77dQ66drec7YcopLWorSQcP6CmmAWvhQt40egiP7mpZjAHmp36bcrmb4LX0b+AEEYIoZ3+e6vD2wEYp/4IzL+lWf3aKZpL4awthXBejFcbta70WeoF71FXWcjtWYpRCRaXInqlWqF96InqPcGDFUUnr4ylI9UK9b+YN74DQ93FhYFObK0D0E49qw1lNRrmvll9xDFqD+op1j4qAEURiKAmKYbaYD='
            #self.headers['Host'] = 'www.tuniu.com'
            self.headers['Referer'] = 'https://piao.qunar.com/'
            resp = requests.get(url, headers=self.headers)
            resp.raise_for_status()
            resp.encoding = 'utf-8'
            return resp.text
        except:
            return ""

    def getRHtml(self,url):
        try:
            self.headers['User-Agent'] = mfu.UserAgent().random()
            #self.headers['Cookie'] = '__guid=131352329.2117375357185893600.1618750037696.1821; p_phone_400=4007-999-999; p_phone_level=0; p_global_phone=%2B0086-25-8685-9999; _tacau=MCw4NjkwMmRjMi0yMmMxLWFlZmUtNTc5NC1jNzRlYTliNmI0OTUs; _tact=MGZhZmNjMTgtZjZmNC04ODJlLTNiM2YtMTdhOThlMzVmM2Vj; _tacz2=taccsr%3D%28direct%29%7Ctacccn%3D%28none%29%7Ctaccmd%3D%28none%29%7Ctaccct%3D%28none%29%7Ctaccrt%3D%28none%29; _ga=GA1.2.697330034.1618750045; _gid=GA1.2.1481901232.1618750045; PageSwitch=1%2C213612736; _uab_collina=161875004597741912116211; smidV2=20210418204730d1a4357137884d6a8cfbb49e7a12f61100f9c9152ac53cc00; tuniu_partner=MTUyOTEsMCwsYzQ1YjA0MjRjZDliMzA4ZDU0NzE5Y2I2ODlhOWE5NzA%3D; isHaveShowPriceTips=1; Hm_lvt_51d49a7cda10d5dd86537755f081cc02=1618758988; tuniuuser_ip_citycode=MTAwOA==; tuniuuser_citycode=MjQwMg%3D%3D; acw_tc=76b20ff416188267636778763e3a7822abed332150bd271d4eed81997d2dcd; acw_sc__v2=607d560ba2d2f37cbacad0ffc568e1b0c8dfb234; monitor_count=8; _taca=1618750044531.1618758928733.1618826770234.3; _tacb=ZjJlODliNGEtMDZlZS0zZmUyLTYzYzctNzRlMGViM2ZmMWUy; _tacc=1; _pzfxuvpc=1618750044912%7C1057153772146331711%7C7%7C1618826770299%7C4%7C1503591366559265886%7C7335018051316751874; _pzfxsvpc=7335018051316751874%7C1618826770291%7C1%7Chttp%3A%2F%2Fwww.tuniu.com%2F; Hm_lvt_fe3fbe4228e14b1544525f058df92f91=1618750046,1618758937,1618826770; Hm_lpvt_fe3fbe4228e14b1544525f058df92f91=1618826770; OLBSESSID=6eb605kbelogi1uge3rju4gm36; ssxmod_itna=CqAx97qQqDqrDXYG7GTueGTKYT3EQW2rA7x0yei=iDSxGKidDqxBeWQrKqe5qv3KOKC3AEoDR2H3hQbEmuomTWCRoX3DU4i8DCTx5YOGDYA8Dt4DTD34DYDixib1xi5GRD09kDbxYp9DWPDYxDr61KDRxi7DDydkx07DQHkKnikeUP+9xo13iBeTnKD9ooDsE+EQnKwvI3qZ1RODl9jDCKz9c9Ci4GdZi0omDxNCQI24TG3SQG3qmrPqi+xx64NGOioKNDbFijyQDDWT00YiA+DD; ssxmod_itna2=CqAx97qQqDqrDXYG7GTueGTKYT3EQW2rADnIgiKitCQDlE70xjRDueZ3Pw2ktGFWik4hsn7iei=Xb4Qvb7tugfo=GeAPRfi+Tt+pBD0qv0Q7gQXfxWgRcH1NOajLqYSdB3+nONgUO0ZmCKPneoZ5HTWT+/2Y1txYTtpawHOGF3DFt3AO=oh0I+1Wb1bSAqafIEfahHpuPcxeww=njBokOwpaHoUyTn/uW0t9XTAMdyxlA8CP5W22NUZeICe=xWFwEhCpQnirQTLiF3lP5V+==CjSneA68mBCKfke53sUFg=VjoZj0XFqtAIEgKLZ+s=XRofKDv/aXUEUuGmr2ID4w3/Kza=77dQ66drec7YcopLWorSQcP6CmmAWvhQt40egiP7mpZjAHmp36bcrmb4LX0b+AEEYIoZ3+e6vD2wEYp/4IzL+lWf3aKZpL4awthXBejFcbta70WeoF71FXWcjtWYpRCRaXInqlWqF96InqPcGDFUUnr4ylI9UK9b+YN74DQ93FhYFObK0D0E49qw1lNRrmvll9xDFqD+op1j4qAEURiKAmKYbaYD='
            #self.headers['Host'] = 'www.tuniu.com'
            self.headers['Referer'] = 'https://piao.qunar.com/'
            resp = requests.get(url, headers=self.headers)
            resp.raise_for_status()
            resp.encoding = 'utf-8'
            return resp
        except:
            return ""

    def get_ticket_id(self, url):  # 获取门票景点的id
        response = self.getRHtml(url)
        while (response.status_code == 404):
            sleep(2)
            response = self.getRHtml(url)
        html = response.text
        try:
            f = re.search(re.compile('"sightId": "(.*)"'), html).group()
            f = "{"+f+"}"
            g = json.loads(f)
            return g['sightId']
        except:
            print(url)
            print(response.status_code)
            return '0'

    def search_spots(self, keyword, city):
        Ncity = city.replace('市', '').replace('县', '').replace('省', '')
        url = 'https://piao.qunar.com/ticket/list.htm?keyword='+Ncity+keyword+'&region='+self.getCityUrl(city)+'&from=mpl_search_suggest&page='
        p = 1;
        try:
            while (1):
                html = self.getHtml(url + str(p))
                soup = BeautifulSoup(html, "html.parser")
                div = soup.find_all('a', attrs={'data-click-type': 'l_title','class':'name'})
                if len(div) == 0:
                    break
                for s in div:
                    title = s.string
                    href = 'https://piao.qunar.com'+s['href']
                    dis = []
                    id = self.get_ticket_id(href)
                    u = 'https://piao.qunar.com/ticket/detail/getTickets.json?sightId=455895&from=detail&supplierId='
                    u = u.replace('455895', id)
                    dicts = json.loads(self.getHtml(u))
                    print(dicts)
                    print(u)
                    self.tickets.append(dis)
                    self.spots.append([title,href])
                p = p + 1
        except:
            traceback.print_exc()
            return
        print(self.tickets)
        print(self.spots)


    def getCityUrl(self,city):
        if len(self.cityList) == 0:
            self.getCityList()
        result = process.extractBests(city, self.cityList.keys(), score_cutoff=80, limit=1)
        return result[0][0]


    def getCityList(self):
        html = self.getHtml(self.start_url)
        soup = BeautifulSoup(html, "html.parser")
        divs = soup.find_all('div', {'class': 'mp-city-list-container mp-privince-city mp-hide'})
        for div in divs:
            citys = div.find_all('li',{'class': 'mp-city-item'})
            for city in citys:
                a = city.find('a')
                title = a.string
                href = a['href']
                self.cityList[title] = href

if __name__ == '__main__':
    mt = QunaSpider()
    mt.search_spots('动物园','济南')