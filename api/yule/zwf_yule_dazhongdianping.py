import requests
from bs4 import BeautifulSoup
import re
import my_fake_useragent as mfu
from fuzzywuzzy import process
from time import sleep
import random
from urllib.parse import quote
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse


class DazhongSpider:
    def __init__(self):
        user_agent = mfu.UserAgent()
        self.headers = {
            "User-Agent": user_agent.random(),
            "Cookie": "_lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=167ffca928ec8-0e654d87ed4011-4d045769-100200-167ffca928ec8; __mta=210679722.1546184730073.1546184730073.1546184730073.1; _lxsdk=167ffca928ec8-0e654d87ed4011-4d045769-100200-167ffca928ec8; _ga=GA1.2.268215992.1546188830; _gid=GA1.2.2085490335.1546188830; mtcdn=K; lsu=; token2=k5KFzZOmjNtI4RXwSn-MBwHYS_QFAAAAqgcAAM17q21drlYFsEkrWY8nBciWgigr_vFCL5FDakc3B15Z318X6W3X_Dkc15OrK0yCPQ; u=646978641; n=XwR964951585; lt=k5KFzZOmjNtI4RXwSn-MBwHYS_QFAAAAqgcAAM17q21drlYFsEkrWY8nBciWgigr_vFCL5FDakc3B15Z318X6W3X_Dkc15OrK0yCPQ; ci=146; rvct=146%2C224%2C527%2C1114%2C1268%2C758%2C835%2C811%2C729%2C113%2C402; unc=XwR964951585; uuid=d927d5e7a70f4031900e.1546184723.2.0.0; client-id=03aeb51b-56e7-4809-b3a0-1fd44f5b4ea4; lat=40.74812; lng=107.400892; _lxsdk_s=16803187a83-b3c-b35-5ba%7C%7C171",
        }
        self.start_url = "http://t.dianping.com/citylist"
        self.store = ''
        self.discountList = []
        self.storeList = []
        self.cookie = [
            '__guid=169583271.2127607620695126000.1618218440470.8167; _lxsdk_cuid=175bae02240c8-09a81e2cb0072f-376b4502-1fa400-175bae02241c8; _lxsdk=175bae02240c8-09a81e2cb0072f-376b4502-1fa400-175bae02241c8; _hc.v=8cc5f797-6103-3af5-abdb-f8baea888bad.1618218444; s_ViewType=10; ua=dpuser_8342278047; ctu=221cf049b9b2e4851a051dc19e113dc7457d5ccf8b929510e97ec6f95a5b6125; cityid=22; default_ab=shopList%3AC%3A5; _lx_utm=utm_source%3Dso.com%26utm_medium%3Dorganic; fspop=test; cy=22; cye=jinan; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1618658692,1618741564,1618745811,1618825724; dper=965e5e629ab69e006a873be31a15f0f5530e016824b2ee5217dfdb51e726c29e64c0e8182775f9d4eec550fdf72032b4157151fbf06393277d8eca821d67b29d9a4e50782a937ce01e24c4e5c87978acd7d79976a6ac115a95a294891bc878b8; ll=7fd06e815b796be3df069dec7836c3df; uamo=15662652209; monitor_count=90; dplet=2ab439395a6417e1c18d480e2c28b2b8; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1618825850; _lxsdk_s=178e9883cb9-dee-7b-1c%7C%7C77',
            'fspop=test; __guid=169583271.2127607620695126000.1618218440470.8167; _lxsdk_cuid=175bae02240c8-09a81e2cb0072f-376b4502-1fa400-175bae02241c8; _lxsdk=175bae02240c8-09a81e2cb0072f-376b4502-1fa400-175bae02241c8; _hc.v=8cc5f797-6103-3af5-abdb-f8baea888bad.1618218444; s_ViewType=10; ua=dpuser_8342278047; ctu=221cf049b9b2e4851a051dc19e113dc7457d5ccf8b929510e97ec6f95a5b6125; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1618218444,1618316416,1618571673,1618658692; dper=965e5e629ab69e006a873be31a15f0f579a0845eb2b3c176d6f00668ca011e840b98b8a129bf16d49dedcc1a42f7785ec1709dbe52244a9360e9868811b109712cb170512f86402e4a51395e5b3d9ab1213fdfb136f210a870d092056f663db6; ll=7fd06e815b796be3df069dec7836c3df; uamo=15662652209; dplet=da5c43b3460109b9c3507790ceb00f4f; cy=22; cye=jinan; _lx_utm=utm_source%3Dso.com%26utm_medium%3Dorganic; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1618667476; _lxsdk_s=178df9386bd-1a-2e0-50%7C%7C672; monitor_count=41',

        ]
        self.index = 0
        self.length = 2



    def choseCookie(self):
        '''
        抽取一个cookie
        :return:
        '''
        if self.index == self.length:
            self.index = 0
        c = self.cookie[self.index]
        self.index = self.index + 1
        return c



    def getHtml(self, url, host):
        '''
        获取网页text内容
        :param url:
        :param host:
        :return:
        '''
        try:
            self.headers['User-Agent'] = mfu.UserAgent().random()
            self.headers['Cookie'] = self.choseCookie()
            #self.headers['Host'] = host
            #self.headers['Referer'] = url
            resp = requests.get(url, headers=self.headers)
            resp.raise_for_status()
            resp.encoding = 'utf-8'
            return resp.text
        except:
            return ""
        #return resp.content.decode(resp.apparent_encoding)



    def getRHtml(self, url):
        '''
        添加host信息获取网页
        :param url:
        :return:
        '''
        try:
            s = quote('密室逃脱')
            #y = 'http://www.dianping.com/search/keyword/22/0_'+s
            #y = 'http://www.dianping.com/search/keyword'
            y = 'https://www.dianping.com/search/keyword/22/0_%E9%AB%98%E7%AC%AC%E8%A1%97'
            #' + str(random.randint(1, 30)) + '
            header = {}
            header['User-Agent'] = mfu.UserAgent().random()
            header['Cookie'] = self.choseCookie()
            header['Host'] = 'www.dianping.com'
            header['Referer'] = y
            resp = requests.get(url, headers=header)
            resp.raise_for_status()
            resp.encoding = 'utf-8'
            return resp.text
        except:
            return ""



    def get_cityID(self,city):
        '''
        获取城市ID
        :param city:
        :return:
        '''
        url = 'https://www.dianping.com'+self.getCityUrl(city)
        html = self.getHtml(url, 'www.dianping.com')
        soup = BeautifulSoup(html, "html.parser")
        script = soup.find('script', {'type': 'text/javascript'})
        r = re.compile(r"'cityId': '")
        t = script.text
        g = ''
        m = r.search(t)
        if m:
            endpos = m.end()
            while t[endpos] != '\'':
                g = g + t[endpos]
                endpos = endpos + 1
        return g


    def search_store(self, keyword, city):
        '''

        :param keyword:
        :param city:
        :return:
        '''
        url = 'https://www.dianping.com/search/keyword/'
        id = self.get_cityID(city)
        url = url + id + '/0_' + keyword
        p = 1;
        while( 1 ):
            html = self.getRHtml(url+'/p'+str(p))
            #html = self.getHtml(url+'/p'+str(p) ,'www.dianping.com')
            while '验证中心' in html:
                print('出现验证码')
                sleep(random.randint(1, 3))
                #html = self.getHtml(url+'/p'+str(p), 'www.dianping.com')
                html = self.getRHtml(url + '/p' + str(p))
            soup = BeautifulSoup(html, "html.parser")
            d = soup.find_all('div', {'class': 'not-found'})
            if len(d) != 0:
                break
            print(len(d))
            stores = soup.find_all('a', {'data-click-name': 'shop_title_click'})
            discounts = soup.find_all('div', {'deal-type': 'DEAL_GROUP'})
            for store in stores:
                self.storeList.append([store['title'], store['href']])
            for discount in discounts:
                dis = []
                d = discount.find_all('a', {'data-click-name': 'shop_info_groupdeal_click'})
                for a in d:
                    dis.append([a['title'],a['href']])
                self.discountList.append(dis)
            p = p + 1
            #sleep(random.randint(1,3))#随即停止一到三秒
        return self.storeList



    def search_Shop(self, keyword, city):#方法一，返回店铺名字和链接集合
        '''
        keyword 用户输入的关键词
        city 用户所在城市
        '''
        stores = self.search_store(keyword, city)
        return stores



    def showDiscount(self, index):#返回相对应的优惠集合
        '''

        :param index: 指定位置
        :return:
        '''
        return self.discountList[index]



    def search_discount(self, keyword, city):#方法二，返回关键词所对应的所有优惠信息
        '''
        返回关键词所对应的所有优惠信息
        :param keyword:
        :param city:
        :return:
        '''
        cityUrl = self.getCityUrl(city)
        cityUrl = 'http://t.dianping.com/list' + cityUrl
        html = self.getHtml(cityUrl + '?q=' + keyword, 't.dianping.com')
        l = self.getStoreInfo(keyword, html)#获取的信息是搜索结果，不以店铺为单位
        return l
        # storeUrl = self.getStoreUrl(keyword, html)#获取的是最符合关键词的某家店铺的优惠信息的URL
        # storePage = self.getHtml(storeUrl,'')
        # self.getDetails(storePage)#从URL中获取详细信息


    def getStoreInfo(self,keyword,html):
        '''
        获取店铺的详细信息
        :param keyword:
        :param html:
        :return:
        '''
        soup = BeautifulSoup(html, "html.parser")
        stores = soup.find('div', {'class': 'tg-list Fix'}).find_all('li', {'class': 'tg-floor-item'})
        l = []
        for store in stores:
            title = store.find('a', {'class':'tg-floor-title'}).find('h3').text.replace('\n', '')
            content = store.find('a', {'class':'tg-floor-title'}).find('h4').text.replace('\n', '').replace(' ','')
            url = 'http://t.dianping.com'+(store.find('a',{'class':'tg-floor-title'}))['href']
            Nprice = store.find('span', {'class':'tg-floor-price-new'}).find('em').string.replace('\n', '')
            Oprice = store.find('span', {'class':'tg-floor-price-old'}).find('del').string.replace('\n', '')
            sold = store.find('span', {'class':'tg-floor-sold'}).string.replace('\n', '').replace(' ','')
            l.append({'name':title, 'description':content, 'link':url, 'nowprice':Nprice, 'pastprice':Oprice, 'count':sold})
            # l.append([title, content, url, Nprice, Oprice, sold])
        return l



    def getStoreUrl(self, keyword, html):#爬取搜索结果之后的页面，找到店铺
        '''
        爬取搜索结果之后的页面，找到店铺
        :param keyword:
        :param html:
        :return:
        '''
        soup = BeautifulSoup(html, "html.parser")
        stores = soup.find('div', {'class': 'tg-list Fix'}).find_all('a', {'class': 'tg-floor-title'})
        storeList = {}
        for store in stores:
            title = store.find('h3').text
            storeList[title] = 'http://t.dianping.com'+store['href']
        result = process.extractBests(keyword, storeList.keys(), score_cutoff=80, limit=10)
        return storeList[result[0][0]]



    def getCityUrl(self,city):
        '''
        爬取城市列表，并返回所在城市的网址
        :param city:
        :return:
        '''

        html = self.getHtml(self.start_url, 't.dianping.com')
        soup = BeautifulSoup(html, "html.parser")
        citys = soup.find('div', {'class': 'letter-city'}).find_all('a')
        citylist = {}
        for c in citys:
            citylist[c['title']] = c['href']
        result = process.extractBests(city, citylist.keys(), score_cutoff=80, limit=1)
        return citylist[result[0][0]]


@require_http_methods(["GET"])
def getYouhuiInfo(request):
    '''
    获取优惠信息
    :param request:
    :return:
    '''
    keyword = request.GET.get('keyword')
    city = request.GET.get('city')
    print(keyword)
    print(city)
    mt = DazhongSpider()
    b = mt.search_discount(keyword, city)
    response = {'data': b}
    return JsonResponse(response)


if __name__ == '__main__':
    mt = DazhongSpider()
    # a = mt.search_Shop("呷哺呷哺", "济南市")
    # c = mt.showDiscount(0)
    b = mt.search_discount("呷哺呷哺", "济南市")
    # print(a)
    # print(c)
    print(b)