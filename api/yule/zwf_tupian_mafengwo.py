import requests
from bs4 import BeautifulSoup
import my_fake_useragent as mfu
import json
import re
from fuzzywuzzy import process
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import execjs
from selenium.webdriver.chrome.options import Options
import re
from selenium.webdriver import Chrome



class TupianSpider:
    def __init__(self):
        user_agent = mfu.UserAgent()
        self.headers = {
            "User-Agent": user_agent.random(),
            "Cookie": "__jsluid_h=c19e9d181bb271865e1be7d61d799c67; mfw_uuid=60b8420e-95c4-eda2-bfc9-5e02d4fd4333; oad_n=a%3A3%3A%7Bs%3A3%3A%22oid%22%3Bi%3A1029%3Bs%3A2%3A%22dm%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222021-06-03+10%3A44%3A30%22%3B%7D; uva=s%3A91%3A%22a%3A3%3A%7Bs%3A2%3A%22lt%22%3Bi%3A1622688271%3Bs%3A10%3A%22last_refer%22%3Bs%3A23%3A%22http%3A%2F%2Fwww.mafengwo.cn%2F%22%3Bs%3A5%3A%22rhost%22%3BN%3B%7D%22%3B; __mfwurd=a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1622688271%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A6%3A%22f_host%22%3Bs%3A3%3A%22www%22%3B%7D; __mfwuuid=60b8420e-95c4-eda2-bfc9-5e02d4fd4333; UM_distinctid=179cfc20b6734d-00221eee7872ec-2363163-144000-179cfc20b68465; __omc_chl=; _r=csdn; _rp=a%3A2%3A%7Bs%3A1%3A%22p%22%3Bs%3A49%3A%22blog.csdn.net%2Fu011291072%2Farticle%2Fdetails%2F81266372%22%3Bs%3A1%3A%22t%22%3Bi%3A1622824665%3B%7D; __mfwothchid=referrer%7Cblog.csdn.net; __omc_r=blog.csdn.net; __mfwc=referrer%7Cblog.csdn.net; bottom_ad_status=0; PHPSESSID=tt8tvp1bg1287j9t4fpd66rpn5; __mfwa=1622688269985.12455.3.1622824668000.1622879218167; __mfwlv=1622879218; __mfwvn=3; Hm_lvt_8288b2ed37e5bc9b4c9f7008798d2de0=1622688271,1622824670,1622879218; CNZZDATA30065558=cnzz_eid%3D1705560339-1622684260-http%253A%252F%252Fwww.mafengwo.cn%252F%26ntime%3D1622878977; __jsl_clearance=1622879888.257|0|MruEnfhwo70geWcDqzscOHYZ%2FGM%3D; Hm_lpvt_8288b2ed37e5bc9b4c9f7008798d2de0=1622879993; __mfwb=0155e7e63b27.4.direct; __mfwlt=1622880000"
        }
        self.list = {}



    def getHtml(self, url):
        '''
        获取网页text内容
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


    def get_dl_info(self,infos, info_name):
        for info in infos:
            if None != info.dt:
                info_title = info.dt.text
                if info_name in info_title:
                    return info.dd.text
        return ''


    def error_http_521res(self,response):
        # 分析521返回的js信息，并返回重新生成的cookie用于重新请求
        res_521_html = response
        # print(res_521_html)

        # 提取js加密函数
        res_521_js_func_str = ''.join(re.findall(r'(function .*?)</script>', res_521_html))
        # print(res_521_jscode_func)

        # 提取js函数参数
        res_521_js_arg = ''.join(re.findall(r'setTimeout\(\"\D+\((\d+)\)\"', res_521_html))
        res_521_js_name = re.findall(r'function (\w+)', res_521_js_func_str)[0]
        # print(res_521_js_arg)
        # print(res_521_js_name)

        # 修改js函数，使其返回cookie内容
        js_func_str = res_521_js_func_str.replace('eval("qo=eval;qo(po);")', 'return po')
        # print(js_func_str)
        js_func = execjs.compile(js_func_str)
        # 执行获取cookie,注意参数顺序
        cookie_str = js_func.call(res_521_js_name, res_521_js_arg)
        # 将cookie 转换成 字典格式
        str = cookie_str.replace("document.cookie='", "")
        clearance = str.split(';')[0]
        cookie_dic = {clearance.split('=')[0]: clearance.split('=')[1]}

        return cookie_dic


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
        allCityidList={}
        allCity = china1.find_all('dd')
        for city in allCity:
            c = city.find_all('a')
            for a in c:
                'http://www.mafengwo.cn/jd/11065/gonglve.html'
                allCityList[a.string] = 'https://www.mafengwo.cn/jd/'+a['href'][29:a['href'].find('.html')]+'/gonglve.html'
                allCityidList[a.string] = a['href'][29:a['href'].find('.html')]
                # allCityList[a.string]=a['href'][29:a['href'].find('.html')]
        for city,id in allCityidList.items():
            onecitylist = {}
            post_url = "http://www.mafengwo.cn/ajax/router.php"
            page = 1
            while True:
                param = {'sAct': 'KMdd_StructWebAjax|GetPoisByTag', 'iMddid': 10065, 'iTagId': 0, 'iPage': page}

                cookies = {
                    '__jsluid_h': 'c19e9d181bb271865e1be7d61d799c67',
                    'mfw_uuid': '60b8420e-95c4-eda2-bfc9-5e02d4fd4333',
                    'oad_n': 'a%3A3%3A%7Bs%3A3%3A%22oid%22%3Bi%3A1029%3Bs%3A2%3A%22dm%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222021-06-03+10%3A44%3A30%22%3B%7D',
                    'uva': 's%3A91%3A%22a%3A3%3A%7Bs%3A2%3A%22lt%22%3Bi%3A1622688271%3Bs%3A10%3A%22last_refer%22%3Bs%3A23%3A%22http%3A%2F%2Fwww.mafengwo.cn%2F%22%3Bs%3A5%3A%22rhost%22%3BN%3B%7D%22%3B',
                    '__mfwurd': 'a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1622688271%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A6%3A%22f_host%22%3Bs%3A3%3A%22www%22%3B%7D',
                    '__mfwuuid': '60b8420e-95c4-eda2-bfc9-5e02d4fd4333',
                    'UM_distinctid': '179cfc20b6734d-00221eee7872ec-2363163-144000-179cfc20b68465',
                    '__omc_chl': '',
                    '_r': 'csdn',
                    '_rp': 'a%3A2%3A%7Bs%3A1%3A%22p%22%3Bs%3A49%3A%22blog.csdn.net%2Fu011291072%2Farticle%2Fdetails%2F81266372%22%3Bs%3A1%3A%22t%22%3Bi%3A1622824665%3B%7D',
                    '__mfwothchid': 'referrer%7Cblog.csdn.net',
                    '__omc_r': 'blog.csdn.net',
                    '__mfwc': 'referrer%7Cblog.csdn.net',
                    'bottom_ad_status': '0',
                    'PHPSESSID': 'tt8tvp1bg1287j9t4fpd66rpn5',
                    '__mfwa': '1622688269985.12455.3.1622824668000.1622879218167',
                    '__mfwlv': '1622879218',
                    '__mfwvn': '3',
                    'Hm_lvt_8288b2ed37e5bc9b4c9f7008798d2de0': '1622688271,1622824670,1622879218',
                    'CNZZDATA30065558': 'cnzz_eid%3D1705560339-1622684260-http%253A%252F%252Fwww.mafengwo.cn%252F%26ntime%3D1622878977',
                    '__jsl_clearance': '1622879888.257|0|MruEnfhwo70geWcDqzscOHYZ%2FGM%3D',
                    'Hm_lpvt_8288b2ed37e5bc9b4c9f7008798d2de0': '1622879993',
                    '__mfwb': '0155e7e63b27.4.direct',
                    '__mfwlt': '1622880000',
                }

                headers = {
                    'Connection': 'keep-alive',
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    'X-Requested-With': 'XMLHttpRequest',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'Origin': 'http://www.mafengwo.cn',
                    'Referer': 'http://www.mafengwo.cn/jd/10065/gonglve.html',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                }

                data = {
                    'sAct': 'KMdd_StructWebAjax|GetPoisByTag',
                    'iMddid': id,
                    'iTagId': '0',
                    'iPage': page,
                    '_ts': '1622880000595',
                    '_sn': 'f10aea0391'
                }
                page = page+1
                response = requests.post('http://www.mafengwo.cn/ajax/router.php', headers=headers, cookies=cookies,
                                         data=data, verify=False)

                data_json = json.loads(response.text)
                print(data_json)
                try:
                    li_list = data_json.get("data").get("list")
                except:
                    break
                # 转为BeautifulSoup对象
                soup = BeautifulSoup(li_list, 'html.parser')
                beijing_pois = soup.find_all({"li"})
                # print(beijing_pois)
                for li in beijing_pois:
                    onesceniclist = {}
                    detail_url = 'http://www.mafengwo.cn'+li.find('a')['href']
                    imgsrc = li.find('img')['src']
                    name = li.find('a')['title']
                    # print(detail_url)
                    try:
                        self.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
                        self.headers[
                            'Cookie'] = '__jsluid_h=c19e9d181bb271865e1be7d61d799c67; mfw_uuid=60b8420e-95c4-eda2-bfc9-5e02d4fd4333; oad_n=a:3:{s:3:"oid";i:1029;s:2:"dm";s:15:"www.mafengwo.cn";s:2:"ft";s:19:"2021-06-03+10:44:30";}; uva=s:91:"a:3:{s:2:"lt";i:1622688271;s:10:"last_refer";s:23:"http://www.mafengwo.cn/";s:5:"rhost";N;}";; __mfwurd=a:3:{s:6:"f_time";i:1622688271;s:9:"f_rdomain";s:15:"www.mafengwo.cn";s:6:"f_host";s:3:"www";}; __mfwuuid=60b8420e-95c4-eda2-bfc9-5e02d4fd4333; UM_distinctid=179cfc20b6734d-00221eee7872ec-2363163-144000-179cfc20b68465; __omc_chl=; _r=csdn; _rp=a:2:{s:1:"p";s:49:"blog.csdn.net/u011291072/article/details/81266372";s:1:"t";i:1622824665;}; __mfwothchid=referrer|blog.csdn.net; __omc_r=blog.csdn.net; __mfwc=referrer|blog.csdn.net; bottom_ad_status=0; PHPSESSID=tt8tvp1bg1287j9t4fpd66rpn5; Hm_lvt_8288b2ed37e5bc9b4c9f7008798d2de0=1622688271,1622824670,1622879218; __jsl_clearance=1622886950.346|0|LB6Pa55KGMvSoQxKRMTXJD57sgU=; __mfwa=1622688269985.12455.4.1622879218167.1622886952813; __mfwlv=1622886952; __mfwvn=4; CNZZDATA30065558=cnzz_eid=1705560339-1622684260-http%3A%2F%2Fwww.mafengwo.cn%2F&ntime=1622884377; __mfwb=eb105c7e9121.2.direct; __mfwlt=1622886975; Hm_lpvt_8288b2ed37e5bc9b4c9f7008798d2de0=1622886976'
                        # self.headers['Host'] = 'www.tuniu.com'
                        self.headers['Referer'] = 'http://www.mafengwo.cn/mdd/'
                        resp = requests.get(detail_url, headers=self.headers)
                        # print(resp.text)
                        # <script>document.cookie=('_')+('_')+('j')+('s')+('l')+('_')+('c')+('l')+('e')+('a')+('r')+('a')+('n')+('c')+('e')+('=')+(-~0+'')+([2]*(3)+'')+((1<<1)+'')+(2+'')+(2+6+'')+((2<<2)+'')+(+!+[]*2+'')+(-~[2]+'')+(1+3+'')+((1<<1)+'')+('.')+(-~[2]+'')+((2^1)+'')+(-~(8)+'')+('|')+('-')+(-~0+'')+('|')+((1+[0])/[2]+'')+('J')+('T')+('c')+('e')+('q')+('b')+(1+5+'')+('U')+('x')+('q')+('X')+('h')+('b')+(3+6+'')+('J')+('V')+('D')+('F')+('H')+('R')+('%')+(0+1+0+1+'')+('F')+('N')+('r')+('%')+(-~1+'')+('F')+('Q')+('c')+('%')+((1+[2]>>2)+'')+('D')+(';')+('m')+('a')+('x')+('-')+('a')+('g')+('e')+('=')+((2^1)+'')+(3+3+'')+(~~''+'')+(~~''+'')+(';')+('p')+('a')+('t')+('h')+('=')+('/');location.href=location.pathname+location.search</script>
                        if resp.status_code == 521:
                            cookie_dic = self.error_http_521res(resp)
                            # 将cookie放入 重新请求
                            cookie_dic = 'ab_jid=caea858d5233a99bb76ddd016cea995a1f4b; Path=/; Domain=miao.baidu.com; Max-Age=2147483647; HttpOnly; Secure; SameSite=None'
                            self.headers['Cookie'] = cookie_dic
                            print(cookie_dic)
                            resp = requests.get(detail_url, headers=self.headers)
                        resp.raise_for_status()
                        resp.encoding = 'utf-8'
                        html_context = resp.text
                    except:
                        html_context = ""
                    print(html_context)

                    # # html_context = self.getHtml(detail_url)
                    # # html_context = urllib.request.urlopen(detail_url).read()
                    # print(html_context)
                    # soup = BeautifulSoup(html_context, 'html.parser')
                    # # print(soup.prettify())
                    # # 景点简介
                    # poi_summary = ''
                    # if None != soup.find(class_="summary"):
                    #     poi_summary = soup.find(class_="summary").text.replace(" ", "")
                    # # 景点游览耗时
                    # poi_time = ''
                    # if None != soup.find(class_="item-time"):
                    #     poi_time = soup.find(class_="item-time").text
                    #
                    # # 景点信息
                    # infos = soup.findAll({'dl'})
                    # # 交通
                    # poi_traffic = self.get_dl_info(infos, '交通')
                    # # 门票
                    # poi_ticket = self.get_dl_info(infos, '门票')
                    # # 开放时间
                    # poi_open_time = self.get_dl_info(infos, '开放时间')
                    # print(poi_summary)
            #     for scenic in list:
            #         onesceniclist = {}
            #         name = scenic['name']
            #         fname = ''
            #         des = scenic['description']
            #         rank = scenic['rank']
            #         imgsrc = scenic['img_link']
            #         onesceniclist['fname'] = fname
            #         onesceniclist['description'] = des
            #         onesceniclist['rank'] = rank
                    onesceniclist['imgsrc'] = imgsrc
                    onecitylist[name] = onesceniclist
            self.list[city] = onecitylist
        # for city,url in allCityList.items():
        #     detail = self.getHtml(url)
        #     detail = detail.replace(' ','').replace('\n','')
        #     detail = detail[detail.find('mapponints')+11:detail.find('M.closure(function(require)')-1]
        #     try:
        #         info = json.loads(detail)
        #     except:
        #         continue
        #     onecitylist = {}
        #     for scenic in info:
        #         name = scenic['name'].encode("utf-8").decode("utf-8")
        #         fname = scenic['foreign_name']
        #         des = scenic['description'].encode("utf-8").decode("utf-8")
        #         rank = scenic['rank']
        #         id = scenic['id']
        #         img = 'https://n1-q.mafengwo.net/'+scenic['img'].replace('\\','').replace('mfwStorage','s')
        #         onesceniclist = {}
        #         onesceniclist['fname'] = fname
        #         onesceniclist['description'] = des
        #         onesceniclist['rank'] = rank
        #         onesceniclist['imgsrc'] = img
        #         onecitylist[name] = onesceniclist
        #     self.list[city] = onecitylist
        print(self.list)
        filename = 'allScenic.json'
        with open(filename,'w') as file:
            json.dump(self.list,file)



@require_http_methods(["POST"])
def getInfo(request):
    '''
    获取某个景点的详细信息
    :param city: 景点所在城市
    :param name: 景点名称
    :return:
    '''
    city = request.POST.get('city')
    name = request.POST.get('name')
    list = {}
    try:
        filename = 'allScenic.json'
        with open(filename, 'r') as file:
            list = json.load(file)
            result = process.extractBests(city, list.keys(), score_cutoff=80, limit=1)
            info = list[result[0][0]][name]
        response = {'data': info}
        return JsonResponse(response)
    except:
        response = {'data': {}}
        return JsonResponse(response)


@require_http_methods(["POST"])
def getInfoofCity(request):
    '''

    :param city:
    :return: 该城市所有景点
    '''
    city = request.POST.get('city')
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



def getInfoofCity0(city):
    '''

    :param city:
    :return: 该城市所有景点
    '''

    list = {}
    try:
        filename = 'allScenic.json'
        with open(filename, 'r') as file:
            list = json.load(file)
            result = process.extractBests(city, list.keys(), score_cutoff=80, limit=1)
            info = list[result[0][0]]
        response = {'data': info}
        return info
    except:
        response = {'data': {}}
        return {}


if __name__ == '__main__':
    # print(getInfo('杭州市', '西湖'))
    mat = TupianSpider()
    mat.getAllImg()
    # print(len(getInfoofCity0('杭州')))