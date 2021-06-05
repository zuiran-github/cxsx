import re
import time
import requests
import urllib3
from bs4 import BeautifulSoup as BS
from lxml import etree
import my_fake_useragent as mfu
from selenium.webdriver import Chrome
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import json
from selenium.webdriver.chrome.options import Options


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class XiechengSpider(object):
    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        # 使用chorme的selenium模拟操作
        self.chrome = Chrome(executable_path='/usr/local/bin/chromedriver', options=options)
        self.chrome.get(
            'https://huodong.ctrip.com/things-to-do/list?pagetype=city&citytype=dt&keyword=%E6%8F%AD%E9%98%B3&pshowcode=Ticket2')
        # time.sleep(3)
        self.page = 1
        self.headers = {
            'cookie': 'Session=SmartLinkCode=U155952&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; _RSG=KqK3qETfa143fOqQl4rFXB; _RDG=282f24100640c82731283334fcc3364464; _RGUID=4064a5d3-b40d-4d14-b84f-d44bdad18a43; Union=OUID=index&AllianceID=4897&SID=155952&SourceID=&createtime=1600831032&Expires=1601435831593; MKT_OrderClick=ASID=4897155952&AID=4897&CSID=155952&OUID=index&CT=1600831031597&CURL=https%3A%2F%2Fwww.ctrip.com%2F%3Fsid%3D155952%26allianceid%3D4897%26ouid%3Dindex&VAL={"pc_vid":"1600831028743.427gzc"}; MKT_CKID=1600831031634.5olt5.f6pj; MKT_CKID_LMT=1600831031635; _ga=GA1.2.248639397.1600831032; _gid=GA1.2.1954297618.1600831032; MKT_Pagesource=PC; GUID=09031031210931119554; nfes_isSupportWebP=1; appFloatCnt=1; nfes_isSupportWebP=1; ASP.NET_SessionSvc=MTAuNjAuMzUuMTQ2fDkwOTB8amlucWlhb3xkZWZhdWx0fDE1ODkwMDMyMjQ5NDI; U_TICKET_SELECTED_DISTRICT_CITY=%7B%22value%22%3A%7B%22districtid%22%3A%22835%22%2C%22districtname%22%3A%22%E6%8F%AD%E9%98%B3%22%2C%22isOversea%22%3Anull%7D%2C%22createTime%22%3A1600847243848%2C%22updateDate%22%3A1600847243848%7D; _RF1=113.118.204.141; _gat=1; _pd=%7B%22r%22%3A1%2C%22d%22%3A614%2C%22_d%22%3A613%2C%22p%22%3A634%2C%22_p%22%3A20%2C%22o%22%3A655%2C%22_o%22%3A21%2C%22s%22%3A668%2C%22_s%22%3A13%7D; _bfa=1.1600831028743.427gzc.1.1600843833503.1600847244099.5.49.10650038368; _bfs=1.30; _bfi=p1%3D290510%26p2%3D290510%26v1%3D49%26v2%3D48; _jzqco=%7C%7C%7C%7C1600831031803%7C1.1555887407.1600831031625.1600849509140.1600849530503.1600849509140.1600849530503.0.0.0.19.19; __zpspc=9.4.1600846262.1600849530.14%232%7Cwww.baidu.com%7C%7C%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        }
        # 储存城市列表
        self.cityList = {}
        # 储存携程里的景点门票数据
        self.spotsInfo = {}
        self.name = '携程旅游'
        # 标记是否已完成查询
        self.done = False



    def get_url(self,keyword):
        '''
        获得景点url
        :param keyword:
        :return:
        '''
        while True:
            content = self.chrome.find_element_by_class_name('right-content-list').get_attribute('innerHTML')
            cons = re.findall(r'href="(.*?)" title="(.*?)"', content)
            # print(content)
            for con in cons:
                self.detail_url = 'https:' + con[0]
                self.title = con[1]
                result = fuzz.token_sort_ratio(self.title, keyword)
                if result <= 20:
                    # print(self.title,result)
                    continue
                # print(self.detail_url, self.title)
                self.get_detail()
            return
            # print(self.spotsInfo)
            pagenums = self.chrome.find_elements_by_class_name('pagination_div_content')
            i = self.chrome.find_elements_by_class_name('item_wrap_font')
            # print(len(i))
            totalpage = -1;
            # print(len(pagenums))
            for pagenum in pagenums:
                totalpage = pagenum.find_element_by_class_name('item_wrap_font').text
                # print(totalpage)
            totalpagenum = int(totalpage)
            self.page = self.page + 1
            # print(totalpage)

            # icon = self.chrome.find_element_by_css_selector('.u_icon_ttd.undefined.u_icon_enArrowforward')
            # icon = self.chrome.find_element_by_class_name('u_icon_ttd')
            # print(type(icon))
            # icon.click()
            if totalpagenum<0:
                self.page = self.page-1
                continue
            if self.page > totalpagenum:
                break
            self.chrome.find_element_by_class_name('pagination_div_jump_input').click()
            self.chrome.find_element_by_class_name('pagination_div_jump_input').send_keys(str(self.page))
            self.chrome.find_element_by_class_name('pagination_div_button').click()
            # time.sleep(1)


    def search_spots(self, keyword, city):
        '''
        核心方法，获取景点数据
        :param keyword:
        :param city:
        :return:
        '''
        self.spotsInfo = {}
        try:
            id = self.getCityID(city)
            Ncity = city.replace('市', '').replace('县', '').replace('省', '')
            #url = 'https://huodong.ctrip.com/things-to-do/list?pagetype=city&citytype=dt&keyword=%E6%8F%AD%E9%98%B3&pshowcode=Ticket2'
            url = 'https://huodong.ctrip.com/things-to-do/list?pagetype=city&citytype=dt&keyword=' + Ncity+keyword + '&id=' + str(self.getCityID(city)) + '&pshowcode=Ticket2'
            self.chrome.get(url)
            self.get_url(keyword)

        except:
            pass
        self.done = True



    def getCityID(self,city):
        '''
        获得城市ID
        :param city:
        :return:
        '''
        if len(self.cityList) == 0:
            self.getCityList()
        result = process.extractBests(city, self.cityList.keys(), score_cutoff=80, limit=1)
        return self.cityList[result[0][0]]



    def getCityList(self):
        '''
        爬取所有城市
        :return:
        '''
        html = self.getHtml('https://piao.ctrip.com/ticket/?districtid=1')
        soup = BS(html, "html.parser")
        script = soup.find_all('script')
        i = 0
        for s in script:
            if i == 4:
                #cities = json.loads(s.text)
                #break
                text = s.text.replace(' ','').replace('\n','')
                text = text[text.find('window.__INITIAL_STATE__')+25:text.find('window.__APP_SETTINGS__=')]
                cities = json.loads(text)
                city = cities['citiesData']['domesticcity']['cities']
                for c in city:
                    for ci in c['cities']:
                        self.cityList[ci['name']] = ci['id']
                break
            i = i+1



    def to_unicode(self, string):
        '''
        unicode编码
        :param string:
        :return:
        '''

        ret = ''
        for v in string:
            ret = ret + hex(ord(v)).upper().replace('0X', '\\u')

        return ret



    def get_detail(self):
        '''
        进入景点详细页面，爬取详细信息
        :return:
        '''
        # detail_con = requests.get(self.detail_url, verify=False, headers=self.headers).text
        # # time.sleep(2)
        # '''使用正则获取信息'''
        # self.rank = ''.join(re.findall(r'rankText">(.*?)<', detail_con, re.DOTALL))
        # self.address = ''.join(re.findall(r'景点地址</p><p class="baseInfoText">(.*?)<', detail_con, re.DOTALL))
        # self.mobile = ''.join(re.findall(r'官方电话</p><p class="baseInfoText">(.*?)<', detail_con, re.DOTALL))
        # print(self.rank, self.address, self.mobile)
        # '''使用xpath获取信息'''
        # ret = etree.HTML(detail_con)
        # desc_cons = ret.xpath('//div[@class="detailModule normalModule"]//div[@class="moduleContent"]')
        # desc_titles = ret.xpath('//div[@class="detailModule normalModule"]//div[@class="moduleTitle"]')
        # desc_list = []
        # desc_title_list = []
        # for d in desc_cons:
        #     des = ''.join(d.xpath('.//text()'))
        #     desc_list.append(des)
        # for d in desc_titles:
        #     des = ''.join(d.xpath('.//text()'))
        #     desc_title_list.append(des)
        # desc_dict = dict(zip(desc_title_list, desc_list))
        # print(desc_dict)
        # '''获取图片链接'''
        # img_list = []
        # imgs = re.findall(r'background-image:url\((.*?)\)', detail_con, re.DOTALL)
        # for img in imgs:
        #     '''匹配到的同一张图片会有两种尺寸，我们只要大图，所以把尺寸为521*391的匹配出来即可'''
        #     image = re.search(r'521_391', img)
        #     if image:
        #         img_list.append(img)
        # print(img_list)
        self.get_ticket()



    def get_ticket(self):
        '''
        获取景点门票信息
        :return:
        '''
        id = self.detail_url.split('/')[-1]
        # print(id)
        ticket_url = f'https://piao.ctrip.com/ticket/dest/{id}?onlyContent=true&onlyShelf=true'
        # print(ticket_url)
        ticket_res = requests.get(ticket_url, verify=False, headers=self.headers).text
        # time.sleep(1)
        ticket_res = ticket_res.replace('\n','').replace(' ','')
        ticket_res = ticket_res[ticket_res.find('window.__INITIAL_STATE__')+25:ticket_res.find('window.__APP_SETTINGS__')]
        info = json.loads(ticket_res)
        ticketinfos = info['detailInfo']['ressHash']
        slist = {}
        for ticketinfo in ticketinfos.values():
            '''解析字典数据'''
            title = ticketinfo['name']
            price = ticketinfo['price']
            type = ticketinfo['saleunitinfo']['propleproperty']
            fromw = '携程旅游 '+ticketinfo['brandname']
            '''数据合并'''
            slist.setdefault(type, [])
            slist[type].append(
                {'name': title, 'type': type, 'price': price, 'url': self.detail_url,
                 'buy': '', 'from': fromw, 'isReturnable': '',
                 'bookTime': '', 'outTime': '', 'useTime': '',
                 'discription': ''})
        self.spotsInfo[self.title] = slist


        # ticket_ret = etree.HTML(ticket_res)
        # ticket = ticket_ret.xpath('//table[@class="ticket-table"]//div[@class="ttd-fs-18"]/text()')
        # price = ticket_ret.xpath(
        #     '//table[@class="ticket-table"]//td[@class="td-price"]//strong[@class="ttd-fs-24"]/text()')
        # print(ticket)
        # print(price)
        # '''拿到的列表里可能存在不确定数量的空值，所以这里用while True把空值全部删除，这样才可以确保门票种类与价格正确对应上'''
        # while True:
        #     try:
        #         ticket.remove(' ')
        #     except:
        #         break
        # while True:
        #     try:
        #         price.remove(' ')
        #     except:
        #         break
        # '''
        #     这里多一个if判断是因为我发现有些详情页即便拿到门票信息并剔除掉空值之后仍然存在无法对应的问题，原因是网页规则有变动，
        #     所以一旦出现这种情况需要使用新的匹配规则，否则会数据会出错（不会报错，但信息对应会错误）
        # '''
        # if len(ticket) != len(price):
        #     ticket = ticket_ret.xpath(
        #         '//table[@class="ticket-table"]/tbody[@class="tkt-bg-gray"]//a[@class="ticket-title "]/text()')
        #     price = ticket_ret.xpath('//table[@class="ticket-table"]//strong[@class="ttd-fs-24"]/text()')
        #     while True:
        #         try:
        #             ticket.remove(' ')
        #         except:
        #             break
        #     while True:
        #         try:
        #             price.remove(' ')
        #         except:
        #             break
        #     print(ticket)
        #     print(price)
        # ticket_dict = dict(zip(ticket, price))
        # print(ticket_dict)



    def getHtml(self, url):
        '''
        获得网页的text内容
        :param url:
        :return:
        '''
        try:
            self.headers['User-Agent'] = mfu.UserAgent().random()
            self.headers['Cookie'] = '_abtest_userid=128990d6-ec49-40cb-b25d-fc8452c3d8a1; _ga=GA1.2.179469688.1614864484; MKT_CKID=1614864484805.yk39i.z4vz; _RSG=r2q6zDxpRN1sq9uB0iKSXA; _RGUID=15dbcfb3-7d1b-40b5-a85c-52c00be09d36; _RDG=287a9b7a6689de2a903820b27712075311; ibulanguage=CN; ibulocale=zh_cn; cookiePricesDisplayed=CNY; _gid=GA1.2.435881939.1618908478; Union=AllianceID=5376&SID=130860&OUID=&createtime=1618908478&Expires=1619513277722; Session=smartlinkcode=U130860&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; MKT_CKID_LMT=1618908477918; MKT_Pagesource=PC; GUID=09031023413294183609; __utma=1.179469688.1614864484.1618917016.1618917016.1; __utmc=1; __utmz=1.1618917016.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _RF1=223.99.16.76; _jzqco=%7C%7C%7C%7C1618908478117%7C1.94961373.1614864484796.1618917699648.1618917762688.1618917699648.1618917762688.undefined.0.0.7.7; __zpspc=9.3.1618917018.1618917762.3%233%7Cwww.so.com%7C%7C%7C%7C%23; _bfa=1.1614864482896.3146qi.1.1618908639843.1618917016691.3.15.10650038368; _bfs=1.5; _bfi=p1%3D10650034475%26p2%3D10650034475%26v1%3D15%26v2%3D14; appFloatCnt=4; U_TICKET_SELECTED_DISTRICT_CITY={%22value%22:{%22districtid%22:1%2C%22districtname%22:%22%E5%8C%97%E4%BA%AC%22%2C%22isoversea%22:false%2C%22stage%22:%22selectedCity%22}%2C%22updateDate%22:1618919559657%2C%22createTime%22:1618919434692}'
            #self.headers['Host'] = 'www.tuniu.com'
            self.headers['Referer'] = 'https://piao.ctrip.com/ticket'
            resp = requests.get(url, headers=self.headers)
            resp.raise_for_status()
            resp.encoding = 'utf-8'
            return resp.text
        except:
            return ""



if __name__ == '__main__':
    jy_jd = XiechengSpider()
    jy_jd.search_spots('方特','济南')
