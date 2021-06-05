import requests
from bs4 import BeautifulSoup
import my_fake_useragent as mfu
import json
import re
from fuzzywuzzy import process
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse



class TupianSpider:
    def __init__(self):
        user_agent = mfu.UserAgent()
        self.headers = {
            "User-Agent": user_agent.random(),
            "Cookie": "p_phone_400=4007-999-999; p_phone_level=0; p_global_phone=%2B0086-25-8685-9999; _tacau=MCw4NjkwMmRjMi0yMmMxLWFlZmUtNTc5NC1jNzRlYTliNmI0OTUs; _tact=MGZhZmNjMTgtZjZmNC04ODJlLTNiM2YtMTdhOThlMzVmM2Vj; _tacz2=taccsr%3D%28direct%29%7Ctacccn%3D%28none%29%7Ctaccmd%3D%28none%29%7Ctaccct%3D%28none%29%7Ctaccrt%3D%28none%29; _tacc=1; _ga=GA1.2.697330034.1618750045; _gid=GA1.2.1481901232.1618750045; PageSwitch=1%2C213612736; OLBSESSID=gus2q36s4pog0o2v4hsbec22a6; PcHomeVisit=1; smidV2=20210418204730d1a4357137884d6a8cfbb49e7a12f61100f9c9152ac53cc00; tuniu_partner=MTUyOTEsMCwsYzQ1YjA0MjRjZDliMzA4ZDU0NzE5Y2I2ODlhOWE5NzA%3D; _taca=1618750044531.1618750044531.1618758928733.2; _tacb=ZDAyZjNjMjgtMjJkZi01MjJmLWVlM2QtNTQzODI2MjRmMjUw; Hm_lvt_fe3fbe4228e14b1544525f058df92f91=1618750046,1618758937; isHaveShowPriceTips=1; Hm_lvt_51d49a7cda10d5dd86537755f081cc02=1618758988; Hm_lpvt_51d49a7cda10d5dd86537755f081cc02=1618759159; tuniuuser_ip_citycode=MTAwOA==; ssxmod_itna=eqfxBQDQitG=qiIx0dD=n2uDUgjDuADx=ppmW40H2eGzDAxn40iDt=PHOG4pDrmGT3Gs36AyfGoF1ebfPq/m8o33DU4i8DCMqoqTDeW=D5xGoDPxDeDADYo6DAqiOD7k=DEDmb8DaxDoDY362DitD4qDBzxdDKqGgbLhNbY=D2+ig7eUNDCGxbqDMCeGXY7W3rmWTTYXWKqGyzPGuATUnzwrDCO4YfYpzvGvXG0GsLGD1S7qeI7wzkDA4iELKfAdtFAmoRI+eDD3P0G44eD=; ssxmod_itna2=eqfxBQDQitG=qiIx0dD=n2uDUgjDuADx=ppmDnKSIheDskaiDLC=HWgjBtW=qnR5ssYBSyGPnKlgFwNsFWl5mKu/iqR5wHLp7Km=KLjOKxji9t03TYKQ4/LxLq93VqOYMtS1GSlKpTUV/hGR/+Usfffr9Rfknu5sRijk/3hKafhKakG0YlLXnwIwU2Tc4fWHl4c4BxA450=st+u0F4YBi+vrpYcQ0pEoE4YOIwvaV1RPDfuWoMAGqTUwG=jOoTyOPj4H3luV732BCpNqn8WI4gCIHwlO9D=mvEh17RLLChKXGGkX23jvpt6lQVAps=pXGIphiK6jM=0OjXdEG3coHYAWaA4xIUOY/g+fBqYCo97EtUNnBwZ6qtaKnBv5Oetg5nlE/lPUh0kIpyD31r3b1DHZ=UZjPEEj0jPam3B6+Z2wWhEP+kYcKWe8mUHFEvAf36G1mc73vznUppvXGnf/p0AmujLgWwHzXaRw8cploo90bICFUEAXWe=RF7lUipX3RRY/t=PURRAr6u63ttU397fPTDexvMpuMj7E3TX1uNAomrqOmXfeecnnl4Q4TGaZW=cDdX2KG4DQKbCGIUExbDOUq9W023q4U25UHk90XauxBnRv24jpHYi2+DnL05Cu=2UkgTsttx0/=iLTjPn=seF94IAHz0Oy0RiRag9=pNkLNe3Rn5rajxNxkPxUDaxGXuDt4D08DG7Hb47DC5x7d1GfB81+xYDD; __guid=84647874.3517961395735585300.1618759287150.3435; monitor_count=1; tuniuuser_citycode=MTkwMw%3D%3D; _pzfxsvpc=1254673435147030907%7C1618758933444%7C4%7Chttp%3A%2F%2Fwww.tuniu.com%2F%3Fp%3D15291%26utm_source%3D360%26utm_medium%3Dcpc%26utm_campaign%3DPP; _pzfxuvpc=1618750044912%7C1057153772146331711%7C5%7C1618759314866%7C2%7C6257891389600454241%7C1254673435147030907; Hm_lpvt_fe3fbe4228e14b1544525f058df92f91=1618759315; _gat=1; clickCache=%5B%7B%22key%22%3A1618759288172%2C%22url%22%3A%22https%3A%2F%2Fjn.tuniu.com%2F%22%2C%22pageName%22%3A%22%E5%BA%A6%E5%81%87%3A%E6%B5%8E%E5%8D%97%3A%E9%A6%96%E9%A1%B5%3Ajn%22%2C%22referer%22%3A%22%22%2C%22events%22%3A%5B%7B%22text%22%3A%22%E7%82%B9%E5%87%BB_%E5%B7%A6%E4%BE%A7%E5%AF%BC%E8%88%AA_%E4%B8%80%E7%BA%A7%E5%AF%BC%E8%88%AA_6_%E9%97%A8%E7%A5%A8%20%E7%8E%A9%E4%B9%90%22%2C%22x%22%3A400%2C%22y%22%3A333%2C%22lg%22%3A1618759888442%7D%5D%7D%5D"
        }
        self.list = {}



    def getHtml(self, url):
        '''
        虎丘网页text内容
        :param url:
        :return:
        '''
        try:
            self.headers['User-Agent'] = mfu.UserAgent().random()
            self.headers['Cookie'] = '__jsluid_h=a36cc55b4bf978581c27b5a0c5c38ecd; __guid=186442287.2875075106880838700.1621242079265.626; mfw_uuid=60a230e2-caec-fed0-1f63-726051666864; oad_n=a%3A3%3A%7Bs%3A3%3A%22oid%22%3Bi%3A1029%3Bs%3A2%3A%22dm%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222021-05-17+17%3A01%3A22%22%3B%7D; __mfwc=direct; uva=s%3A91%3A%22a%3A3%3A%7Bs%3A2%3A%22lt%22%3Bi%3A1621242084%3Bs%3A10%3A%22last_refer%22%3Bs%3A23%3A%22http%3A%2F%2Fwww.mafengwo.cn%2F%22%3Bs%3A5%3A%22rhost%22%3BN%3B%7D%22%3B; __mfwurd=a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1621242084%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A6%3A%22f_host%22%3Bs%3A3%3A%22www%22%3B%7D; __mfwuuid=60a230e2-caec-fed0-1f63-726051666864; UM_distinctid=179798efea715-0839cc2a865b56-376b4502-1fa400-179798efea82b1; bottom_ad_status=0; PHPSESSID=hgla0nidhpna2qfe5othdi0of2; __mfwa=1621242083107.22706.2.1621242083107.1621255595846; __mfwlv=1621255595; __mfwvn=2; Hm_lvt_8288b2ed37e5bc9b4c9f7008798d2de0=1621242085,1621255596; __omc_chl=; __omc_r=; __jsl_clearance=1621257482.651|0|EmCk5dxrQc0Gxh14q4LThKkHf1A%3D; __jsluid_s=4dd191ae77bb2389976da37e6fecfc4d; CNZZDATA30065558=cnzz_eid%3D1690025938-1621239949-http%253A%252F%252Fwww.mafengwo.cn%252F%26ntime%3D1621258179; __jsl_clearance_s=1621260980.181|0|Fzx2Pddtt2RW5Lq3Tv2JnNYOdIA%3D; monitor_count=53; __mfwb=b283048fa80a.29.direct; __mfwlt=1621261029; Hm_lpvt_8288b2ed37e5bc9b4c9f7008798d2de0=1621261030'
            #self.headers['Host'] = 'www.tuniu.com'
            self.headers['Referer'] = 'http://www.mafengwo.cn/mdd/'
            resp = requests.get(url, headers=self.headers)
            resp.raise_for_status()
            resp.encoding = 'utf-8'
            return resp.text
        except:
            return ""



    def getAllImg(self):
        '''
        获取所有图片
        :return:
        '''
        html = self.getHtml('http://www.mafengwo.cn/mdd/')
        soup = BeautifulSoup(html,'html.parser')
        china1 = soup.find('div',{'class':'hot-list clearfix'})
        china2 = soup.find('div',{'class':'hot-list clearfix hide'})
        allCityList = {}
        allCity = china1.find_all('dd')
        for city in allCity:
            c = city.find_all('a')
            for a in c:
                'http://www.mafengwo.cn/jd/11065/gonglve.html'
                allCityList[a.string] = 'https://www.mafengwo.cn/jd/'+a['href'][29:a['href'].find('.html')]+'/gonglve.html'
                # allCityList[a.string]=a['href'][29:a['href'].find('.html')]
        for city,url in allCityList.items():
            detail = self.getHtml(url)
            detail = detail.replace(' ','').replace('\n','')
            detail = detail[detail.find('mapponints')+11:detail.find('M.closure(function(require)')-1]
            try:
                info = json.loads(detail)
            except:
                continue
            onecitylist = {}
            for scenic in info:
                name = scenic['name'].encode("utf-8").decode("utf-8")
                fname = scenic['foreign_name']
                des = scenic['description'].encode("utf-8").decode("utf-8")
                rank = scenic['rank']
                id = scenic['id']
                img = 'https://n1-q.mafengwo.net/'+scenic['img'].replace('\\','').replace('mfwStorage','s')
                onesceniclist = {}
                onesceniclist['fname'] = fname
                onesceniclist['description'] = des
                onesceniclist['rank'] = rank
                onesceniclist['imgsrc'] = img
                onecitylist[name] = onesceniclist
            self.list[city] = onecitylist
        print(self.list)
        filename = 'allScenic.json'
        with open(filename,'w') as file:
            json.dump(self.list,file)


def to_string(string):
    string.encode('gbk')

@require_http_methods(["GET"])
def getInfo(request):
    '''
    获取某个景点的详细信息
    :param city: 景点所在城市
    :param name: 景点名称
    :return:
    '''
    city = request.GET.get('city')
    name = request.GET.get('name')
    print(request.GET)
    print(name)
    list = {}
    # global file
    try:
        filename = '/Users/zuiran/Documents/大三下/创新实训/proj4/api/yule/allScenic.json'
        with open(filename, 'r') as file:
            # file.encoding = 'gbk'
            # files = file.read()
            # files.encode('gbk')
            list = json.load(file)
            # print(list)
            # print(len(list))
            result = process.extractBests(city, list.keys(), score_cutoff=80, limit=1)
            result1 = process.extractBests(name, list[result[0][0]].keys(), score_cutoff=80, limit=1)
            info = list[result[0][0]][result1[0][0]]
        response = {'data': info}
        print(response)
        return JsonResponse(response)
    except Exception as e:
        print(e)
        response = {'data': {}}
        print(response)
        return JsonResponse(response)


@require_http_methods(["GET"])
def getInfoofCity(request):
    '''

    :param city:
    :return: 该城市所有景点
    '''
    city = request.GET.get('city')
    list = {}
    try:
        filename = 'allScenic.json'
        with open(filename, 'r') as file:
            list = json.load(file)
            result = process.extractBests(city, list.keys(), score_cutoff=80, limit=1)
            info = list[result[0][0]]
        response = {'data': info}
        return JsonResponse(response)
    except:
        response = {'data': {}}
        return JsonResponse(response)


if __name__ == '__main__':
    print(getInfo('北京市', '故宫'))
    print(getInfoofCity('杭州'))