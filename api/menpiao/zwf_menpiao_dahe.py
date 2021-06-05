import requests
from bs4 import BeautifulSoup
import my_fake_useragent as mfu
from fuzzywuzzy import fuzz


class DaheSpider:
    def __init__(self):
        user_agent = mfu.UserAgent()
        self.headers = {
            "User-Agent": user_agent.random(),
            "Cookie": "p_phone_400=4007-999-999; p_phone_level=0; p_global_phone=%2B0086-25-8685-9999; _tacau=MCw4NjkwMmRjMi0yMmMxLWFlZmUtNTc5NC1jNzRlYTliNmI0OTUs; _tact=MGZhZmNjMTgtZjZmNC04ODJlLTNiM2YtMTdhOThlMzVmM2Vj; _tacz2=taccsr%3D%28direct%29%7Ctacccn%3D%28none%29%7Ctaccmd%3D%28none%29%7Ctaccct%3D%28none%29%7Ctaccrt%3D%28none%29; _tacc=1; _ga=GA1.2.697330034.1618750045; _gid=GA1.2.1481901232.1618750045; PageSwitch=1%2C213612736; OLBSESSID=gus2q36s4pog0o2v4hsbec22a6; PcHomeVisit=1; smidV2=20210418204730d1a4357137884d6a8cfbb49e7a12f61100f9c9152ac53cc00; tuniu_partner=MTUyOTEsMCwsYzQ1YjA0MjRjZDliMzA4ZDU0NzE5Y2I2ODlhOWE5NzA%3D; _taca=1618750044531.1618750044531.1618758928733.2; _tacb=ZDAyZjNjMjgtMjJkZi01MjJmLWVlM2QtNTQzODI2MjRmMjUw; Hm_lvt_fe3fbe4228e14b1544525f058df92f91=1618750046,1618758937; isHaveShowPriceTips=1; Hm_lvt_51d49a7cda10d5dd86537755f081cc02=1618758988; Hm_lpvt_51d49a7cda10d5dd86537755f081cc02=1618759159; tuniuuser_ip_citycode=MTAwOA==; ssxmod_itna=eqfxBQDQitG=qiIx0dD=n2uDUgjDuADx=ppmW40H2eGzDAxn40iDt=PHOG4pDrmGT3Gs36AyfGoF1ebfPq/m8o33DU4i8DCMqoqTDeW=D5xGoDPxDeDADYo6DAqiOD7k=DEDmb8DaxDoDY362DitD4qDBzxdDKqGgbLhNbY=D2+ig7eUNDCGxbqDMCeGXY7W3rmWTTYXWKqGyzPGuATUnzwrDCO4YfYpzvGvXG0GsLGD1S7qeI7wzkDA4iELKfAdtFAmoRI+eDD3P0G44eD=; ssxmod_itna2=eqfxBQDQitG=qiIx0dD=n2uDUgjDuADx=ppmDnKSIheDskaiDLC=HWgjBtW=qnR5ssYBSyGPnKlgFwNsFWl5mKu/iqR5wHLp7Km=KLjOKxji9t03TYKQ4/LxLq93VqOYMtS1GSlKpTUV/hGR/+Usfffr9Rfknu5sRijk/3hKafhKakG0YlLXnwIwU2Tc4fWHl4c4BxA450=st+u0F4YBi+vrpYcQ0pEoE4YOIwvaV1RPDfuWoMAGqTUwG=jOoTyOPj4H3luV732BCpNqn8WI4gCIHwlO9D=mvEh17RLLChKXGGkX23jvpt6lQVAps=pXGIphiK6jM=0OjXdEG3coHYAWaA4xIUOY/g+fBqYCo97EtUNnBwZ6qtaKnBv5Oetg5nlE/lPUh0kIpyD31r3b1DHZ=UZjPEEj0jPam3B6+Z2wWhEP+kYcKWe8mUHFEvAf36G1mc73vznUppvXGnf/p0AmujLgWwHzXaRw8cploo90bICFUEAXWe=RF7lUipX3RRY/t=PURRAr6u63ttU397fPTDexvMpuMj7E3TX1uNAomrqOmXfeecnnl4Q4TGaZW=cDdX2KG4DQKbCGIUExbDOUq9W023q4U25UHk90XauxBnRv24jpHYi2+DnL05Cu=2UkgTsttx0/=iLTjPn=seF94IAHz0Oy0RiRag9=pNkLNe3Rn5rajxNxkPxUDaxGXuDt4D08DG7Hb47DC5x7d1GfB81+xYDD; __guid=84647874.3517961395735585300.1618759287150.3435; monitor_count=1; tuniuuser_citycode=MTkwMw%3D%3D; _pzfxsvpc=1254673435147030907%7C1618758933444%7C4%7Chttp%3A%2F%2Fwww.tuniu.com%2F%3Fp%3D15291%26utm_source%3D360%26utm_medium%3Dcpc%26utm_campaign%3DPP; _pzfxuvpc=1618750044912%7C1057153772146331711%7C5%7C1618759314866%7C2%7C6257891389600454241%7C1254673435147030907; Hm_lpvt_fe3fbe4228e14b1544525f058df92f91=1618759315; _gat=1; clickCache=%5B%7B%22key%22%3A1618759288172%2C%22url%22%3A%22https%3A%2F%2Fjn.tuniu.com%2F%22%2C%22pageName%22%3A%22%E5%BA%A6%E5%81%87%3A%E6%B5%8E%E5%8D%97%3A%E9%A6%96%E9%A1%B5%3Ajn%22%2C%22referer%22%3A%22%22%2C%22events%22%3A%5B%7B%22text%22%3A%22%E7%82%B9%E5%87%BB_%E5%B7%A6%E4%BE%A7%E5%AF%BC%E8%88%AA_%E4%B8%80%E7%BA%A7%E5%AF%BC%E8%88%AA_6_%E9%97%A8%E7%A5%A8%20%E7%8E%A9%E4%B9%90%22%2C%22x%22%3A400%2C%22y%22%3A333%2C%22lg%22%3A1618759888442%7D%5D%7D%5D"
        }
        self.spots = []
        self.tickets = []
        '''记录景点门票信息'''
        self.spotsInfo = {}
        self.name = '大河票务'
        # 标记查询是否完成
        self.done = False


    def getHtml(self, url):
        '''
        获得网页的text内容
        :param url:
        :return:
        '''
        try:
            self.headers['User-Agent'] = mfu.UserAgent().random()
            self.headers['Cookie'] = 'Hm_lvt_64941895c0a12a3bdeb5b07863a52466=1618908738,1621066788,1621430892; pt__search_from=channel=scenery&page=scenery-index; __guid=28211134.3027891932986968000.1621433416753.135; _tcudid_v2=Heduqn08MGjn_99CGYUUHN_6jp48JY7iaPNJI2jFoKg; qdid=-9999; 17uCNRefId=RefId=0&SEFrom=&SEKeyWords=; TicketSEInfo=RefId=0&SEFrom=&SEKeyWords=; CNSEInfo=RefId=0&tcbdkeyid=&SEFrom=&SEKeyWords=&RefUrl=; Hm_lvt_c6a93e2a75a5b1ef9fb5d4553a2226e5=1621066808,1621430903,1621479164; __tctma=144323752.1618908737536602.1618908737482.1621430890844.1621479162672.4; __tctmu=144323752.0.0; __tctmz=144323752.1621479162672.4.1.utmccn=(direct)|utmcsr=(direct)|utmcmd=(none); longKey=1618908737536602; __tctrack=0; indexTopSearchHistory=%5B%22%E6%96%B9%E7%89%B9%22%2C%22%E6%B5%8E%E5%8D%97%E6%96%B9%E7%89%B9%22%2C%22%E6%B5%8E%E5%8D%97%E6%B5%8E%E5%8D%97%E6%96%B9%E7%89%B9%22%2C%22%E4%B8%8A%E6%B5%B7%E8%BF%AA%E5%A3%AB%E5%B0%BC%22%2C%22%E9%9D%92%E5%B2%9B%E6%96%B9%E7%89%B9%22%2C%22%E6%B7%B1%E5%9C%B3%E6%96%B9%E7%89%B9%22%2C%22%E8%BF%AA%E5%A3%AB%E5%B0%BC%22%5D; wwwscenery=35a2356ff0780dcdca4b45e9a0cd10b0; ASP.NET_SessionId=o2tyazukx3zehx1eeivhuvaj; pagestate=1; Hm_lpvt_c6a93e2a75a5b1ef9fb5d4553a2226e5=1621479269; __tctmc=144323752.210364819; __tctmd=144323752.737325; __tctmb=144323752.1502026337417512.1621479203036.1621479266761.5; monitor_count=13'
            #self.headers['Host'] = 'www.tuniu.com'
            self.headers['Referer'] = 'https://so.ly.com/scenery?q=%E6%96%B9%E7%89%B9'
            resp = requests.get(url, headers=self.headers)
            resp.raise_for_status()
            resp.encoding = 'utf-8'
            return resp.text
        except:
            return ""


    def search_spots(self, keyword, city):
        '''

        :param keyword: 关键词
        :param city: 在哪所城市搜索
        :return:
        '''
        self.spotsInfo={}
        Ncity = city.replace('市', '').replace('县', '').replace('省', '')
        # 添加城市名，提高搜索精度
        url = 'https://www.dahepiao.com/search_new?fenlei=2&keyword='+Ncity+keyword
        # p = 1;
        try:
            html = self.getHtml(url)
            soup = BeautifulSoup(html,"html.parser")
            items = soup.find_all('a',{'class':'info-title'})
            for item in items:
                # 名称
                title = item['title']
                # 跳转链接
                href = item['href']
                # 进一步筛选
                result = fuzz.token_sort_ratio(title, keyword)
                if result <= 20:
                    continue
                detailhtml = self.getHtml(href)
                dsoup = BeautifulSoup(detailhtml, "html.parser")
                tbody = dsoup.find('tbody',{'id':'ticket_body'})
                trs = tbody.find_all('tr')
                tickets = {}
                for tr in trs:
                    # 门票的详细描述
                    dis = tr.find('div',{'class':'link_text'}).find_all('p')
                    discription = ''
                    for di in dis:
                        discription = discription + di.text + '\n'
                    # 用try except包装，提高容错
                    try:
                        type= tr.find('td',{'class':'ptdname'}).text.replace('\n','').replace(' ','')
                    except:
                        type=''
                    try:
                        ttitle = tr.find('a',{'class':'ptlink'}).text.replace('订票须知','').replace('\n','').replace(' ','')
                    except:
                        ttitle = ''
                    try:
                        booktime = tr.find('dd',{'class':'ticket_bookingTime'}).string.replace('\n','').replace(' ','')
                    except:
                        booktime = ''
                    try:
                        price = tr.find('dd',{'class':'ticket_price'}).text.replace('￥', '').replace('\n','').replace(' ','')
                    except:
                        price = ''
                    tickets.setdefault(type,[])
                    tickets[type].append({'name':ttitle,'type':type,'price':price,'url':href,'buy':'','from':'大河票务网','isReturnable':'',
                                    'bookTime':booktime,'outTime':'','useTime':'','discription':discription})
                self.spotsInfo[title] = tickets
                # print(self.spotsInfo)

        except Exception as e:
            print(e)
        self.done = True


if __name__ == '__main__':
    mt = DaheSpider()
    mt.search_spots('方特','青岛')