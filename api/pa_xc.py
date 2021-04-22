import io
from bs4 import BeautifulSoup as BS
import time
import re
import requests
import my_fake_useragent as mfu
from fuzzywuzzy import process
import random
import json

"""从网上爬取数据"""
class xcSpider:
    def __init__(self):
        self.headers = {
        "Origin": "https://piao.ctrip.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        }
        self.cityList = {}
        self.cityUrlList = {}
        self.base = "https://you.ctrip.com/fooditem/";
        self.base2 = "https://you.ctrip.com";



    def getXC(self, city):
        url = self.base + self.getCityUrl(city) + ".html"
        p = 1
        l = []
        count = 1;
        while p != 3:
            tmp = self.base + self.getCityUrl(city) + "/s0-p" + str(p) + ".html"
            html = self.getHtml(tmp)
            soup = BS(html, 'html.parser')
            vs = soup.find_all(name="div", attrs={"class": "rdetailbox"})
            print("len(vs)", len(vs))
            for j in range(len(vs)):
                try:
                    # 获取子网页链接地址
                    href = vs[j].find(name="a", attrs={"target": "_blank"}).attrs["href"];

                    # print("href",href)
                    # 再次请求子网页，获取景点详细信息
                    res = self.getHtml(self.base2 + href)
                    soupi = BS(res, "html.parser")  # 该网页的html代码
                    vis = soupi.find_all(name="li", attrs={"class": "infotext"});  # 获取此时的dom文件位置所在
                    introduce = []
                    for i in range(len(vis)):
                        introduce.append(vis[i].get_text())
                    imgs = [];
                    imglinks = soupi.find_all(name="a", attrs={"href": "javascript:void(0)"})
                    # print(imte)
                    # print(imglinks)
                    # print(type(imglinks))
                    # for img in imte:
                    # imgs.append(img.attrs["src"])
                    tmp = {};
                    tmp["id"] = count;
                    tmp["name"] = vs[j].find(name="a", attrs={"target": "_blank"}).string;
                    tmp["name"] = tmp["name"].replace(" ", "").replace("\n", "");
                    tmp["introduce"] = introduce
                    tmp["img"] = imglinks
                    tmp["city"] = city
                    count = count + 1;
                    l.append(tmp);
                    #time.sleep(1);
                except Exception as e:
                    print(e)
                    pass
                '''with io.open("D:\\py\\aaaaaaaaa\cxsx\zwfpachong\\" + tmp["name"] + ".txt", 'w',
                            encoding="utf-8") as f:
                    f.write(str(tmp))'''
            p = p+1
        # print(l)
        for i in l:
            print((i))

    def getCityUrl(self,city):
        if len(self.cityUrlList) == 0:
            self.getCityUrlList()
        result = process.extractBests(city, self.cityUrlList.keys(), score_cutoff=80, limit=1)
        return self.cityUrlList[result[0][0]]

    def getCityUrlList(self):
        html = self.getHtml('https://you.ctrip.com/place/')
        soup = BS(html, "html.parser")
        cities = soup.find_all('dl',{'class':'item itempl-60'})
        for city in cities:
            c = city.find_all('a')
            for ci in c:
                self.cityUrlList[ci.string] = ci['href'].replace('/place/','').replace('.html','')

    def getHtml(self, url):
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


    def getCityID(self,city):
        if len(self.cityList) == 0:
            self.getCityList()
        result = process.extractBests(city, self.cityList.keys(), score_cutoff=80, limit=1)
        return self.cityList[result[0][0]]


    def getCityList(self):
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


if __name__ == '__main__':
    mt = xcSpider()
    mt.getXC('杭州')