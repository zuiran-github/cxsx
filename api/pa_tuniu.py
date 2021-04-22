import requests
from bs4 import BeautifulSoup
import re
import my_fake_useragent as mfu
from fuzzywuzzy import process
from time import sleep
import random

class TuNiuSpider:
    def __init__(self):
        user_agent = mfu.UserAgent()
        self.headers = {
            "User-Agent": user_agent.random(),
            "Cookie": "p_phone_400=4007-999-999; p_phone_level=0; p_global_phone=%2B0086-25-8685-9999; _tacau=MCw4NjkwMmRjMi0yMmMxLWFlZmUtNTc5NC1jNzRlYTliNmI0OTUs; _tact=MGZhZmNjMTgtZjZmNC04ODJlLTNiM2YtMTdhOThlMzVmM2Vj; _tacz2=taccsr%3D%28direct%29%7Ctacccn%3D%28none%29%7Ctaccmd%3D%28none%29%7Ctaccct%3D%28none%29%7Ctaccrt%3D%28none%29; _tacc=1; _ga=GA1.2.697330034.1618750045; _gid=GA1.2.1481901232.1618750045; PageSwitch=1%2C213612736; OLBSESSID=gus2q36s4pog0o2v4hsbec22a6; PcHomeVisit=1; smidV2=20210418204730d1a4357137884d6a8cfbb49e7a12f61100f9c9152ac53cc00; tuniu_partner=MTUyOTEsMCwsYzQ1YjA0MjRjZDliMzA4ZDU0NzE5Y2I2ODlhOWE5NzA%3D; _taca=1618750044531.1618750044531.1618758928733.2; _tacb=ZDAyZjNjMjgtMjJkZi01MjJmLWVlM2QtNTQzODI2MjRmMjUw; Hm_lvt_fe3fbe4228e14b1544525f058df92f91=1618750046,1618758937; isHaveShowPriceTips=1; Hm_lvt_51d49a7cda10d5dd86537755f081cc02=1618758988; Hm_lpvt_51d49a7cda10d5dd86537755f081cc02=1618759159; tuniuuser_ip_citycode=MTAwOA==; ssxmod_itna=eqfxBQDQitG=qiIx0dD=n2uDUgjDuADx=ppmW40H2eGzDAxn40iDt=PHOG4pDrmGT3Gs36AyfGoF1ebfPq/m8o33DU4i8DCMqoqTDeW=D5xGoDPxDeDADYo6DAqiOD7k=DEDmb8DaxDoDY362DitD4qDBzxdDKqGgbLhNbY=D2+ig7eUNDCGxbqDMCeGXY7W3rmWTTYXWKqGyzPGuATUnzwrDCO4YfYpzvGvXG0GsLGD1S7qeI7wzkDA4iELKfAdtFAmoRI+eDD3P0G44eD=; ssxmod_itna2=eqfxBQDQitG=qiIx0dD=n2uDUgjDuADx=ppmDnKSIheDskaiDLC=HWgjBtW=qnR5ssYBSyGPnKlgFwNsFWl5mKu/iqR5wHLp7Km=KLjOKxji9t03TYKQ4/LxLq93VqOYMtS1GSlKpTUV/hGR/+Usfffr9Rfknu5sRijk/3hKafhKakG0YlLXnwIwU2Tc4fWHl4c4BxA450=st+u0F4YBi+vrpYcQ0pEoE4YOIwvaV1RPDfuWoMAGqTUwG=jOoTyOPj4H3luV732BCpNqn8WI4gCIHwlO9D=mvEh17RLLChKXGGkX23jvpt6lQVAps=pXGIphiK6jM=0OjXdEG3coHYAWaA4xIUOY/g+fBqYCo97EtUNnBwZ6qtaKnBv5Oetg5nlE/lPUh0kIpyD31r3b1DHZ=UZjPEEj0jPam3B6+Z2wWhEP+kYcKWe8mUHFEvAf36G1mc73vznUppvXGnf/p0AmujLgWwHzXaRw8cploo90bICFUEAXWe=RF7lUipX3RRY/t=PURRAr6u63ttU397fPTDexvMpuMj7E3TX1uNAomrqOmXfeecnnl4Q4TGaZW=cDdX2KG4DQKbCGIUExbDOUq9W023q4U25UHk90XauxBnRv24jpHYi2+DnL05Cu=2UkgTsttx0/=iLTjPn=seF94IAHz0Oy0RiRag9=pNkLNe3Rn5rajxNxkPxUDaxGXuDt4D08DG7Hb47DC5x7d1GfB81+xYDD; __guid=84647874.3517961395735585300.1618759287150.3435; monitor_count=1; tuniuuser_citycode=MTkwMw%3D%3D; _pzfxsvpc=1254673435147030907%7C1618758933444%7C4%7Chttp%3A%2F%2Fwww.tuniu.com%2F%3Fp%3D15291%26utm_source%3D360%26utm_medium%3Dcpc%26utm_campaign%3DPP; _pzfxuvpc=1618750044912%7C1057153772146331711%7C5%7C1618759314866%7C2%7C6257891389600454241%7C1254673435147030907; Hm_lpvt_fe3fbe4228e14b1544525f058df92f91=1618759315; _gat=1; clickCache=%5B%7B%22key%22%3A1618759288172%2C%22url%22%3A%22https%3A%2F%2Fjn.tuniu.com%2F%22%2C%22pageName%22%3A%22%E5%BA%A6%E5%81%87%3A%E6%B5%8E%E5%8D%97%3A%E9%A6%96%E9%A1%B5%3Ajn%22%2C%22referer%22%3A%22%22%2C%22events%22%3A%5B%7B%22text%22%3A%22%E7%82%B9%E5%87%BB_%E5%B7%A6%E4%BE%A7%E5%AF%BC%E8%88%AA_%E4%B8%80%E7%BA%A7%E5%AF%BC%E8%88%AA_6_%E9%97%A8%E7%A5%A8%20%E7%8E%A9%E4%B9%90%22%2C%22x%22%3A400%2C%22y%22%3A333%2C%22lg%22%3A1618759888442%7D%5D%7D%5D"
        }
        self.start_url = "https://jn.tuniu.com/"
        self.cityList = {}
        self.spots = []
        self.tickets = []

    def getHtml(self, url):
        try:
            self.headers['User-Agent'] = mfu.UserAgent().random()
            self.headers['Cookie'] = '__guid=131352329.2117375357185893600.1618750037696.1821; p_phone_400=4007-999-999; p_phone_level=0; p_global_phone=%2B0086-25-8685-9999; _tacau=MCw4NjkwMmRjMi0yMmMxLWFlZmUtNTc5NC1jNzRlYTliNmI0OTUs; _tact=MGZhZmNjMTgtZjZmNC04ODJlLTNiM2YtMTdhOThlMzVmM2Vj; _tacz2=taccsr%3D%28direct%29%7Ctacccn%3D%28none%29%7Ctaccmd%3D%28none%29%7Ctaccct%3D%28none%29%7Ctaccrt%3D%28none%29; _ga=GA1.2.697330034.1618750045; _gid=GA1.2.1481901232.1618750045; PageSwitch=1%2C213612736; _uab_collina=161875004597741912116211; smidV2=20210418204730d1a4357137884d6a8cfbb49e7a12f61100f9c9152ac53cc00; tuniu_partner=MTUyOTEsMCwsYzQ1YjA0MjRjZDliMzA4ZDU0NzE5Y2I2ODlhOWE5NzA%3D; isHaveShowPriceTips=1; Hm_lvt_51d49a7cda10d5dd86537755f081cc02=1618758988; tuniuuser_ip_citycode=MTAwOA==; tuniuuser_citycode=MjQwMg%3D%3D; acw_tc=76b20ff416188267636778763e3a7822abed332150bd271d4eed81997d2dcd; acw_sc__v2=607d560ba2d2f37cbacad0ffc568e1b0c8dfb234; monitor_count=8; _taca=1618750044531.1618758928733.1618826770234.3; _tacb=ZjJlODliNGEtMDZlZS0zZmUyLTYzYzctNzRlMGViM2ZmMWUy; _tacc=1; _pzfxuvpc=1618750044912%7C1057153772146331711%7C7%7C1618826770299%7C4%7C1503591366559265886%7C7335018051316751874; _pzfxsvpc=7335018051316751874%7C1618826770291%7C1%7Chttp%3A%2F%2Fwww.tuniu.com%2F; Hm_lvt_fe3fbe4228e14b1544525f058df92f91=1618750046,1618758937,1618826770; Hm_lpvt_fe3fbe4228e14b1544525f058df92f91=1618826770; OLBSESSID=6eb605kbelogi1uge3rju4gm36; ssxmod_itna=CqAx97qQqDqrDXYG7GTueGTKYT3EQW2rA7x0yei=iDSxGKidDqxBeWQrKqe5qv3KOKC3AEoDR2H3hQbEmuomTWCRoX3DU4i8DCTx5YOGDYA8Dt4DTD34DYDixib1xi5GRD09kDbxYp9DWPDYxDr61KDRxi7DDydkx07DQHkKnikeUP+9xo13iBeTnKD9ooDsE+EQnKwvI3qZ1RODl9jDCKz9c9Ci4GdZi0omDxNCQI24TG3SQG3qmrPqi+xx64NGOioKNDbFijyQDDWT00YiA+DD; ssxmod_itna2=CqAx97qQqDqrDXYG7GTueGTKYT3EQW2rADnIgiKitCQDlE70xjRDueZ3Pw2ktGFWik4hsn7iei=Xb4Qvb7tugfo=GeAPRfi+Tt+pBD0qv0Q7gQXfxWgRcH1NOajLqYSdB3+nONgUO0ZmCKPneoZ5HTWT+/2Y1txYTtpawHOGF3DFt3AO=oh0I+1Wb1bSAqafIEfahHpuPcxeww=njBokOwpaHoUyTn/uW0t9XTAMdyxlA8CP5W22NUZeICe=xWFwEhCpQnirQTLiF3lP5V+==CjSneA68mBCKfke53sUFg=VjoZj0XFqtAIEgKLZ+s=XRofKDv/aXUEUuGmr2ID4w3/Kza=77dQ66drec7YcopLWorSQcP6CmmAWvhQt40egiP7mpZjAHmp36bcrmb4LX0b+AEEYIoZ3+e6vD2wEYp/4IzL+lWf3aKZpL4awthXBejFcbta70WeoF71FXWcjtWYpRCRaXInqlWqF96InqPcGDFUUnr4ylI9UK9b+YN74DQ93FhYFObK0D0E49qw1lNRrmvll9xDFqD+op1j4qAEURiKAmKYbaYD='
            #self.headers['Host'] = 'www.tuniu.com'
            self.headers['Referer'] = 'https://www.tuniu.com/'
            resp = requests.get(url, headers=self.headers)
            resp.raise_for_status()
            resp.encoding = 'utf-8'
            return resp.text
        except:
            return ""

    def search_spots(self, keyword, city):
        cityUrl = self.getCityUrl(city)
        Ncity = city.replace('市','').replace('县','').replace('省','')
        url = 'https://s.tuniu.com/search_complex/ticket-'+cityUrl+'-0-'+Ncity+keyword+'/'
        p = 1;
        try:
            while (1):
                html = self.getHtml(url + str(p))
                soup = BeautifulSoup(html, "html.parser")
                div = soup.find('div', {'class': 'thelist'})
                if div is None:
                    break
                spot = div.find_all('li')
                for s in spot:
                    title = s.find('dl', {'class': 'detail'}).find('p',{'class':'title ticket'}).text.replace('\n','').replace(' ','')
                    address = s.find('dl', {'class': 'detail'}).find('dd').string.replace(u'\u3000',u'')
                    opentime = s.find('dl', {'class': 'detail'}).find('dd', {'class': 'port'}).text.replace('\n','')
                    price = s.find('div', {'class': 'priceinfo'}).find('span',{'class':'tnPrice'}).text.replace('\n','').replace(' ','')
                    manyi = s.find('p',{'class': 'manyi_inner'}).text.replace('\n','').replace(' ','')
                    href = (s.find('div',{'class':'theinfo ticket clearfix'}).find('a',{'class':'img'}))['href']
                    imgsrc = (s.find('div',{'class':'theinfo ticket clearfix'}).find('img'))['data-src']
                    ticket = s.find('div',{'class': 'ticketlist'}).find_all('div',{'class': 'each-item'})
                    dis = []
                    for t in ticket:
                        ticketTitle = t.find('span', {'class': 'ticketTitle'}).text
                        ticketPrice = t.find('span', {'class': 'tnPrice'}).text
                        ticketBookUrl = (t.find('form'))['action']
                        dis.append([ticketTitle,ticketPrice,ticketBookUrl])
                    self.tickets.append(dis)
                    self.spots.append([title,address,opentime,price,manyi,href,imgsrc])
                p = p + 1
        except:
            return
        print(self.tickets)
        print(self.spots)


    def getCityUrl(self,city):
        if len(self.cityList) == 0:
            self.getCityList()
        result = process.extractBests(city, self.cityList.keys(), score_cutoff=80, limit=1)
        return self.cityList[result[0][0]]


    def getCityList(self):
        html = self.getHtml(self.start_url)
        soup = BeautifulSoup(html, "html.parser")
        divs = soup.find_all('div', {'class': 'line_right'})
        for div in divs:
            citys = div.find_all('a',{'href': re.compile(r'http://(.*)')})
            for city in citys:
                title = city.string
                href = city['href']
                i = 7
                g = ''
                while href[i] != '.':
                    g = g + href[i]
                    i = i+1
                self.cityList[title] = g
        self.cityList['济南'] = 'jn'

if __name__ == '__main__':
    mt = TuNiuSpider()
    mt.search_spots('方特','济南')