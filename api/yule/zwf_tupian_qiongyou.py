import csv
import requests
import parsel
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import json
import threading
import my_fake_useragent as mfu
from bs4 import BeautifulSoup
import time
from concurrent.futures import as_completed
from concurrent.futures import wait,ALL_COMPLETED,FIRST_COMPLETED
from yule import zwf_writefile

allList = {}
# count = 0

def send_request(url):
    try:
        headers = {}
        headers['User-Agent'] = mfu.UserAgent().random()
        headers[
            'Cookie'] = '_qyeruid=CgIBAWC4PHp2qkJVmSkPAg==; new_uv=1; new_session=1; _guid=Rc6e04dd-9db6-cafc-afa0-e9515fac0d3f; ql_guid=QL5c19c9-1f38-4377-82a6-18242efa0235; source_url=https://www.qyer.com/; isnew=1622686857075; __utma=253397513.1025643824.1622686844.1622825628.1622888267.5; __utmc=253397513; __utmz=253397513.1622888267.5.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; PHPSESSID=23bf82872f55096d2a8720eb8dfeb705; city_browse=a:2:{i:0;i:50;i:1;i:51;}; ql_created_session=1; ql_stt=1622892667772; ql_vts=7; __utmt=1; __utmb=253397513.27.10.1622888267; ql_seq=27'
        # self.headers['Host'] = 'www.tuniu.com'
        headers['Referer'] = 'https://place.qyer.com/china/sight/'
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        resp.encoding = 'utf-8'
        return resp.text
    except:
        return ""


def parse_data(html_data):
    global allList
    # print(allList)
    selector = parsel.Selector(html_data)
    lis = selector.xpath('//ul[@class="plcCitylist"]/li')
    if len(lis)<15:
        print(str(len(lis)),html_data)
    for li in lis:
        travel_place = li.xpath('.//h3/a/text()').get()  # 目的地
        travel_place = travel_place.replace('\xa0','')
        onecitylist={}
        pid = li.xpath('.//p[@class="addPlanBtn"]/@data-pid').get()
        # print(travel_place, travel_people, travel_hot, travel_url, travel_imgUrl,pid, sep=' | ')
        page = 1
        while page < 500:
            headers = {
                'authority': 'place.qyer.com',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'x-requested-with': 'XMLHttpRequest',
                'sec-ch-ua-mobile': '?0',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://place.qyer.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://place.qyer.com/hong-kong/sight/',
                'accept-language': 'zh-CN,zh;q=0.9',
                'cookie': '_qyeruid=CgIBAWC4PHp2qkJVmSkPAg==; new_uv=1; new_session=1; _guid=Rc6e04dd-9db6-cafc-afa0-e9515fac0d3f; ql_guid=QL5c19c9-1f38-4377-82a6-18242efa0235; source_url=https%3A//www.qyer.com/; isnew=1622686857075; __utma=253397513.1025643824.1622686844.1622825628.1622888267.5; __utmc=253397513; __utmz=253397513.1622888267.5.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; ql_created_session=1; ql_stt=1622888267070; ql_vts=5; frombaidu=1; PHPSESSID=23bf82872f55096d2a8720eb8dfeb705; __utmb=253397513.10.10.1622888267; ql_seq=10',
            }

            params = (
                ('action', 'list_json'),
            )

            data = {
                'page': page,
                'type': 'city',
                'pid': pid,
                'sort': '32',
                'subsort': 'all',
                'isnominate': '-1',
                'haslastm': 'false',
                'rank': '6'
            }
            print(page)
            page = page+1
            response = requests.post('https://place.qyer.com/poi.php', headers=headers, params=params, data=data)

            # NB. Original query string below. It seems impossible to parse and
            # reproduce query strings 100% accurately so the one below is given
            # in case the reproduced version is not "correct".
            # response = requests.post('https://place.qyer.com/poi.php?action=list_json', headers=headers, data=data)
            try:
                result = json.loads(response.text)
            except Exception as e:
                # page = page-1
                print('error'+response.text)
                time.sleep(3)
                page = page-1
                continue
            data = result['data']['list']
            # print(data)
            if len(data)==0:
                break
            for dat in data:
                name = dat['cnname']
                enname = dat['enname']
                score = dat['grade']
                imgsrc = dat['photo']
                rank = dat['rank']
                try:
                    dis=dat['comments'][0]['text']
                except:
                    dis=''
                # detail_url = 'https:'+dat['url']
                # detail_html = send_request(detail_url)
                # soup = BeautifulSoup(detail_html, "html.parser")
                # try:
                #     dis = soup.find('div',{'class':'compo-detail-info'}).text.replace(' ','')
                # except:
                #     dis = ''
                onesceniclist = {}
                onesceniclist['fname'] = enname
                onesceniclist['description'] = dis
                onesceniclist['rank'] = rank
                onesceniclist['imgsrc'] = imgsrc
                onesceniclist['score'] = score
                onecitylist[name] = onesceniclist
                # print(onecitylist)
        allList[travel_place] = onecitylist
        # print(allList)
        # count = count+1
        print('城市：'+travel_place)
        time.sleep(3)
    return allList


def parse_data_for_city(pid, page):
    global allList
    # print(allList)
    headers = {
                'authority': 'place.qyer.com',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'x-requested-with': 'XMLHttpRequest',
                'sec-ch-ua-mobile': '?0',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://place.qyer.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://place.qyer.com/hong-kong/sight/',
                'accept-language': 'zh-CN,zh;q=0.9',
                'cookie': '_qyeruid=CgIBAWC4PHp2qkJVmSkPAg==; new_uv=1; new_session=1; _guid=Rc6e04dd-9db6-cafc-afa0-e9515fac0d3f; ql_guid=QL5c19c9-1f38-4377-82a6-18242efa0235; source_url=https%3A//www.qyer.com/; isnew=1622686857075; __utma=253397513.1025643824.1622686844.1622825628.1622888267.5; __utmc=253397513; __utmz=253397513.1622888267.5.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; ql_created_session=1; ql_stt=1622888267070; ql_vts=5; frombaidu=1; PHPSESSID=23bf82872f55096d2a8720eb8dfeb705; __utmb=253397513.10.10.1622888267; ql_seq=10',
    }

    params = (
            ('action', 'list_json'),
    )

    data = {
                'page': page,
                'type': 'city',
                'pid': pid,
                'sort': '32',
                'subsort': 'all',
                'isnominate': '-1',
                'haslastm': 'false',
                'rank': '6'
    }
    print(page)
    response = requests.post('https://place.qyer.com/poi.php', headers=headers, params=params, data=data)

            # NB. Original query string below. It seems impossible to parse and
            # reproduce query strings 100% accurately so the one below is given
            # in case the reproduced version is not "correct".
            # response = requests.post('https://place.qyer.com/poi.php?action=list_json', headers=headers, data=data)
    try:
        result = json.loads(response.text)
    except Exception as e:
        # page = page-1
        print('error'+response.text)
        time.sleep(3)
        newlist = parse_data_for_city(pid,page)
        return newlist
    data = result['data']['list']
    if len(data)==0:
        return {}
    for dat in data:
        name = dat['cnname']
        enname = dat['enname']
        score = dat['grade']
        imgsrc = dat['photo']
        rank = dat['rank']
        try:
            dis=dat['comments'][0]['text']
        except:
            dis=''
        onesceniclist = {}
        onesceniclist['fname'] = enname
        onesceniclist['description'] = dis
        onesceniclist['rank'] = rank
        onesceniclist['imgsrc'] = imgsrc
        onesceniclist['score'] = score
        allList[name] = onesceniclist
    return allList



def save_data(data_generator):
    global lock
    with open('穷游网.csv', mode='a', encoding='utf-8', newline='') as f:
        csv_write = csv.writer(f)
        for data in data_generator:

            lock.acquire()  # 加锁
            csv_write.writerow(data)
            lock.release()  # 释放锁


def main(url):
    html_data = send_request(url)
    list0 = {}
    try:
        list0 = parse_data(html_data)
    except Exception as e:
        print(repr(e))
    return list0
    # save_data(parse_result)


if __name__ == '__main__':
    # main('https://place.qyer.com/china/citylist-0-0-1')
    all_task = []
    with ProcessPoolExecutor(max_workers=13) as executor:
        for page in range(1, 4): #172
            # print(page)
            url = f'https://place.qyer.com/china/citylist-0-0-{page}/'
            all_task.append(executor.submit(main, url))
            time.sleep(1)
    # for value in as_completed(all_task):
    #     l = value.result()
    #     allList = dict(**allList, **l)
    #     filename = 'allScenic.json'
    #     with open(filename, 'w') as file:
    #         json.dump(allList, file)西安、大连成都青岛广州南京
    wait(all_task, return_when=ALL_COMPLETED)
    for value in all_task:
        l = value.result()
        try:
            allList = dict(**allList, **l)
        except:
            for key, value in l.items():
                allList[key] = value
    # filename = 'allScenic.json'
    # with open(filename, 'w') as file:
    #     json.dump(allList, file)
    zwf_writefile.writeNewCity(allList)
    print(allList)

