import requests
from bs4 import BeautifulSoup
import re
import my_fake_useragent as mfu
import json


class FeizhuSpider:
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
        self.name = '飞猪旅游'
        self.done = False


    def getHtml(self, url):
        '''
        获得网页的text内容
        :param url:
        :return:
        '''
        try:
            self.headers['User-Agent'] = mfu.UserAgent().random()
            self.headers['Cookie'] = 'cna=FSuVFNVw/BsCATrCqL/Y8XoE; hng=CN%7Czh-CN%7CCNY%7C156; lid=tb334618007; enc=B4cUDsXKdA8gJmSiKtsf8cVZ7uyCx3b8hPNtjyd%2BmrvnuXtP5KVL0gXoKr43Vcg%2FcgkEMi4UwRB7KfHKy9pTuQ%3D%3D; __guid=193720296.3164744941186917000.1618907822741.9824; xlly_s=1; sgcookie=E1007eLfxDiWyniR9XZNElBK%2B2ynEj2%2Fe4B%2FwctTfIkHWqf8mV3V6TaQN8umGEaEiru%2BjTaCNUZGcxaiV7EGpm0TDg%3D%3D; t=78173eadd36134ce7d3315518701b9f7; tracknick=tb334618007; _tb_token_=lC0uef4rj1KNLMd0Q1cQ; cookie2=12b099818172aca75e8ca3547ca99df0; _mw_us_time_=1620539512334; l=eBIdpZARjBKfqxS1BO5Zourza7794QRf1sPzaNbMiIncC6hFTWv9Ip-QDUcMTd-RR8XcGULp4kkZIseteUsgJ_MmndLn5n95LbkWCef..; isg=BDU145IcuWOlId02tRY8AfJHRLHvsunEoBI1d7dYIq6IjlaAfgaSlA5P2FK4zgF8; tfstk=cuecBRMPESlj-fcuOtMbD8_SK87Ral9Z-Ry7URPpcHWYmONS0sYeaB5XDg0mLPd1.; monitor_count=13'
            #self.headers['Host'] = 'www.tuniu.com'
            self.headers['Referer'] = 'https://travelsearch.fliggy.com/index.htm?searchType=product&keyword=%20%E8%BF%AA%E5%A3%AB%E5%B0%BC%20'
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
        self.spotsInfo = {}
        Ncity = city.replace('市', '').replace('县', '').replace('省', '')
        url = 'https://travelsearch.fliggy.com/index.htm?searchType=product&keyword='+Ncity+keyword+'&category=SCENIC&pagenum=1&conditions=dest%3A'+Ncity
        p = 1;
        try:
            html = self.getHtml(url)
            soup = BeautifulSoup(html,"html.parser")
            '''获得景点列表'''
            scenics = soup.find_all('a',{'href':re.compile(r'https://s.fliggy.com/scenic/')})
            list = set()
            for scenic in scenics:
                list.add(scenic['href'])
            for scenic in list:
                detail = self.getHtml(scenic)
                detail_soup = BeautifulSoup(detail,"html.parser")
                title = detail_soup.find('h3',{'class':'scenic-tit'}).text.replace(' ','').replace('\n','')
                ticketList = {}
                # print(title)
                scripts = detail_soup.find_all('script')
                for script in scripts:
                    text = script.string
                    if text is None:
                        continue
                    text = text.replace(' ', '').replace('\n', '')
                    if( text.find('window.TICKETS') != -1 ):
                        '''获取json格式的数据'''
                        text = text[text.find('window.TICKETS') + 15:]
                        tickets = json.loads(text)
                        sid = tickets['sid']
                        list = tickets['ticketTypes']
                        for ticket in list:
                            '''门票的类型'''
                            ticktype = ticket['ticketType']
                            tick = ticket['chargingItemGroupList']
                            for t in tick:
                                tic = t['chargeItems']
                                for ti in tic:
                                    '''分类'''
                                    product = ti['value']   #{"discountPrice":"330.00","soldRecnet":155387,"value":"1日门票"}
                                    pagenum = 1
                                    '''跳转链接'''
                                    buy_url = 'https://traveldetail.fliggy.com/item.htm?id='
                                    while(1):
                                        detail_url = 'https://s.alitrip.com/scenic/item.htm?format=json&sid='+str(sid)+'&ticketkindname='+ticktype+'&productname='+product+'&jumpto='+str(pagenum)+'&_input_charset=utf-8'
                                        info = self.getHtml(detail_url)
                                        ticketinfo = json.loads(info)
                                        pagenum = pagenum+1
                                        if(ticketinfo['code']==500):
                                            break
                                        itemList = ticketinfo['itemList']
                                        for item in itemList:
                                            #景点名称，门票（名称name，类别type，价格price，url，已售buy，旅行社from，可退isReturnable，预定时间bookTime,出票时间outTime，
                                            # 可用时间useTime,说明discription)
                                            '''名称'''
                                            ttitle = item['title']
                                            '''已售'''
                                            buy = item['soldNum']
                                            '''类型'''
                                            type = item['tcatName']
                                            '''门票ID'''
                                            itemid = item['itemid']
                                            '''退款政策'''
                                            try:
                                                isreturn = item['refund']
                                            except:
                                                isreturn = ''
                                            '''来源'''
                                            fromw = '飞猪 '+item['sellerName']
                                            '''价格'''
                                            price = item['price']
                                            '''描述'''
                                            dis = item['refundDesc']
                                            fea = item['featureShow']
                                            count = 0
                                            bookTime = ''
                                            outTime = ''
                                            useTime = ''
                                            for f in fea:
                                                if count == 0:
                                                    bookTime = f['text']
                                                    count = count+1
                                                elif count == 1:
                                                    outTime = f['text']
                                                    count = count+1
                                                elif count == 2:
                                                    useTime = f['text']
                                                    count = count+1
                                            ticketList.setdefault(type, [])
                                            ticketList[type].append({'name':ttitle,'type':type,'price':price,'url':buy_url+str(itemid),'buy':buy,'from':fromw,'isReturnable':isreturn,
                                    'bookTime':bookTime,'outTime':outTime,'useTime':useTime,'discription':dis})



                        break
                self.spotsInfo[title] = ticketList
                # print(self.spotsInfo)


        except Exception as e:
            print(e)
        self.done = True


if __name__ == '__main__':
    mt = FeizhuSpider()
    mt.search_spots('方特','青岛')