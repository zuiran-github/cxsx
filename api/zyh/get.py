import requests
import json
import re


def city_id():
    """
    获取城市站台对应代号并保存到本地
    :return: dict
    """
    # 通过抓包可知城市代码信息为请求如下地址
    url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9186"
    response = requests.get(url=url).text

    # 通过正则表达式获取需要数据
    find_city = re.findall(r'@.*?\|(.*?)\|', response)
    find_city_id = re.findall(r'@.*?\|.*?\|(.*?)\|', response)

    city_id_dict = {}
    for c, i in zip(find_city, find_city_id):
        city_id_dict[c] = i

    # print(city_id_dict)
    return city_id_dict


def decrypt(string):
    """
    处理字符串
    :param string:
    :return:
    """
    # 定义正则表达式提取规则
    reg1 = re.compile(
        '.*?\|预订\|.*?\|(.*?)\|(.*?)\|(.*?)\|.*?\|.*?\|(.*?)\|(.*?)\|(.*?)\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|(.*?)\|')
    reg2 = re.compile(
        '.*?\|.*?起售\|.*?\|(.*?)\|(.*?)\|(.*?)\|.*?\|.*?\|(.*?)\|(.*?)\|(.*?)\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|.*?\|.*?\|.*?\|.*')
    reg3 = re.compile(
        '.*?\|.*?停运\|.*?\|(.*?)\|(.*?)\|(.*?)\|.*?\|.*?\|(.*?)\|(.*?)\|(.*?)\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|.*?\|.*?\|.*?\|.*')
    reg4 = re.compile(
        '.*?\|.*?暂停发售\|.*?\|(.*?)\|(.*?)\|(.*?)\|.*?\|.*?\|(.*?)\|(.*?)\|(.*?)\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|.*?\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|.*?\|.*?\|.*?\|.*')
    # 因网站存在三种状态的列车信息，所以使用try语句进行处理。

    try:
        result = re.findall(reg1, string)[0]
    except IndexError as e:
        try:
            result = re.findall(reg2, string)[0]
        except:
            try:
                result = re.findall(reg3, string)[0]
            except:
                result = re.findall(reg4, string)[0]
    return result


def getchepiaoinfo(city_id_dict, start, end, time):
    """
    获取列车信息并保存至本地。
    :param city_id_dict:
    :return:
    """
    # 通过抓包可知车次信息为请求如下地址得到
    fs = start
    ts = end
    date = time
    url = "https://kyfw.12306.cn/otn/leftTicket/query?"

    # 构造form表单
    params = {
        'leftTicketDTO.train_date': date,
        'leftTicketDTO.from_station': city_id_dict[fs],
        'leftTicketDTO.to_station': city_id_dict[ts],
        'purpose_codes': 'ADULT',
    }
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Host': 'kyfw.12306.cn',
        'If-Modified-Since': '0',
        'Pragma': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': '_uab_collina=161493863463826929255067; JSESSIONID=2740020E11DC4CBC1A2AA60B5DD9CEC2;'
    }

    response = requests.get(url=url,params=params,headers=headers)
    print(response.status_code)
    # 请求到的数据使用json来进行处理
    # print(response.text)
    jsdata = json.loads(response.text, strict=False)['data']['result']
    read_id = {}
    for k, v in city_id_dict.items():
        read_id[v] = k
    # 获取车次详情信息，并保存至本地
    dict = []
    # count = 0
    for item in jsdata:
        # break
        result = list(decrypt(item))
        # print("jieguo")
        # print(result)
        result[1] = fs
        result[2] = ts
        # 构建content列表，用于存放列车信息
        content = [result[0], read_id[item.split('|')[6]], read_id[item.split('|')[7]], result[3], result[4], result[5],
                   result[-1], result[-2], result[-3],
                   result[6], result[-10], result[8], result[-5], result[9], result[-4], result[-7], result[-6]]
        # 构建content列表，用于存放列车信息
        print(result[-1])
        if len(result[-1]) == 30:
            top = (result[-1][-9:-4])[:-1]+'.'+(result[-1][-9:-4])[-1]
            no1 = (result[-1][11:16])[:-1]+'.'+(result[-1][11:16])[-1]
            no2 = (result[-1][1:6])[:-1]+'.'+(result[-1][1:6])[-1]
            print(top, no1, no2)
            result[-1] = min(float(top), float(no1), float(no2))
        elif len(result[-1]) ==40:
            noseat = (result[-1][-9:-4])[:-1]+'.'+(result[-1][-9:-4])[-1]
            seat1 = (result[-1][1:6])[:-1]+'.'+(result[-1][1:6])[-1]
            seat2 = (result[-1][11:16])[:-1]+'.'+(result[-1][11:16])[-1]
            seat3 = (result[-1][21:26])[:-1]+'.'+(result[-1][21:26])[-1]
            print(noseat, seat2, seat1, seat3)
            result[-1] = min(float(noseat), float(seat1), float(seat2), float(seat3))
        elif len(result[-1]) == 20:
            noseat = (result[-1][-9:-4])[:-1] + '.' + (result[-1][-9:-4])[-1]
            seat1 = (result[-1][1:6])[:-1] + '.' + (result[-1][1:6])[-1]
            print(noseat, seat1)
            result[-1] = min(float(noseat), float(seat1))

        content = [result[0], read_id[item.split('|')[6]], read_id[item.split('|')[7]], result[3], result[4], result[5],
                   result[-2], result[-3], result[-4],
                   result[6], result[7], result[8], result[-6], result[9], result[-5], result[-8], result[-7],
                   result[-1]]
        print(content)
        # print(type(content))

        tzurl = 'https://kyfw.12306.cn/otn/leftTicket/init?' \
                'linktypeid=dc' \
                '&fs=,' + city_id_dict[fs] + \
                '&ts=,' + city_id_dict[ts] + \
                '&date=' + date + \
                '&flag=N,N,Y'

        price = result[-1]
        # print(tzurl)

        dict.append({
            'trainID': result[0],
            'dStation': read_id[item.split('|')[6]],
            'aStation': read_id[item.split('|')[7]],
            'dtime': result[3],
            'atime': result[4],
            'during': result[5],
            'shangwu': result[-2],
            'yidengzuo': result[-3],
            'erdengzuo': result[-4],
            'gaojiruanwo': result[6],
            'ruanwo': result[-11],
            'dongwo': result[8],
            'yingwo': result[-6],
            'ruanzuo': result[9],
            'yingzuo': result[-5],
            'wuzuo': result[-8],
            'qita': result[-7],
            'tzurl': tzurl,
            'price': price,


        })

        # count += 1
    print(dict)
    # jsdict = json.dumps(dict)
    # f2 = open('train.json', 'w')
    # f2.write(jsdict)
    # f2.close()
    return dict


def spider_main():
    # 主函数，程序运行入口
    start='重庆'#input("出发地")
    end='广州'#input("目的地")
    time='2021-06-10'#input("出发时间(xxxx-xx-xx)")
    str='[车次,出发地,目的地,出发时间,抵达时间,行驶时间,商务座/特等座,一等座,二等座/二等包座,高级软卧,软卧/一等卧,动卧,硬卧/二等卧,软座,硬座,无座,其它]'
    print(str)
    city_id_dict = city_id()

    secretStr = getchepiaoinfo(city_id_dict,start,end,time)
    return secretStr


if __name__ == '__main__':
    dict = spider_main()
    # print(dict)
