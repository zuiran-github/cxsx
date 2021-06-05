# data = [{'MU5100': '54'}, {'MU5183': '98'}]
# for i in data:
#     print(i.keys())
#     print(type(i.keys()))


# import random
# print(random.randint(1,3))
#
# for i in range(100):
#     print(random.randint(1, 3))

# dict = {'type': 1,
#         'data': [
#             {'name': '上海峰裕宾馆',
#              'web': [{'website': '携程', 'distance': 0.44, 'score': 4.4, 'comments': 106, 'price': 0, 'type': '经济型', 'link': None, 'position': '上海朱家角古镇旅游区 新风路与美周路交界处'}, {'website': '去哪儿', 'distance': 0.44, 'score': 4.4, 'comments': 106, 'price': 242.0, 'type': '经济型', 'link': 'https://hotel.qunar.com/cn/shanghai_city/dt-82909?fromDate=2021-06-10&toDate=2021-06-12/', 'position': '上海朱家角古镇旅游区 新风路与美周路交界处'}, {'website': '飞猪', 'distance': 0.44, 'score': 4.4, 'comments': 106, 'price': 154.0, 'type': '经济型', 'link': 'https://hotel.fliggy.com/hotel_detail2.htm?shid=61501009&city=310100&checkIn=2021-06-10&checkOut=2021-06-12&searchId=4811e8b3defc48fe92d7698b9842bbb5&_output_charset=utf8', 'position': '上海朱家角古镇旅游区 新风路与美周路交界处'}, {'website': '途牛', 'distance': 0.44, 'score': 4.4, 'comments': 106, 'price': 216.0, 'type': '经济型', 'link': 'https://hotel.tuniu.com/detail/2051654775?checkInDate=2021-06-10&checkOutDate=2021-06-12', 'position': '上海朱家角古镇旅游区 新风路与美周路交界处'}, {'website': '艺龙', 'distance': 0.44, 'score': 4.4, 'comments': 106, 'price': 0, 'type': '经济型', 'link': None, 'position': '上海朱家角古镇旅游区 新风路与美周路交界处'}],
#              'picture': 'https://userimg.qunarzz.com/imgs/202005/01/C.tpQEczB2whjZJdWlz480.webp'
#             }]
#         }
#
# print(type(dict))


# import datetime
# # print (datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
#
# date = '2021-06-21'
# print(date+datetime.timedelta(days=1))
#
#
# import datetime
# in_date = '2021-08-31'
# dt = datetime.datetime.strptime(in_date, "%Y-%m-%d")
# out_date = (dt + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
# # str(out_date)
# a = out_date + 'ddd'
# print(a)
# print(out_date)

def getCityName(citycode):
    '''
    根据大写城市代码返回城市中文名称
    :param citycode: 大写城市代码
    :return:
    '''
    try:
        dict = {'安庆': 'AQG', '阿克苏': 'AKU', '北海': 'BHY', '毕节': 'BFJ', '包头': 'BAV', '北京': 'PKX', '北京': 'PEK', '北京': 'BJS',
                '常州': 'CZX', '常德': 'CGD', '成都': 'CTU', '池州': 'JUH', '长春': 'CGQ', '重庆': 'CKG', '长沙': 'CSX', '承德': 'CDE',
                '大同': 'DAT', '大连': 'DLC', '敦煌': 'DNH', '大庆': 'DQA', '大理': 'DLU', '恩施': 'ENH', '福州': 'FOC', '贵阳': 'KWE',
                '广州': 'CAN', '固原': 'GYU', '赣州': 'KOW', '桂林': 'KWL', '杭州': 'HGH', '海拉尔': 'HLD', '呼和浩特': 'HET',
                '衡阳': 'HNY', '海口': 'HAK', '汉中': 'HZG', '哈尔滨': 'HRB', '黄山': 'TXN', '邯郸': 'HDG', '合肥': 'HFE', '淮安': 'HIA',
                '九寨': 'JZH', '嘉峪关': 'JGN', '景德镇': 'JDZ', '济宁': 'JNG', '揭阳': 'SWA', '井冈山': 'JGS', '金昌': 'JIC',
                '济南': 'TNA', '昆明': 'KMG', '库尔勒': 'KRL', '喀什': 'KHG', '拉萨': 'LXA', '柳州': 'LZH', '泸州': 'LZO', '陇南': 'LNL',
                '临沂': 'LYI', '连云港': 'LYG', '兰州': 'LHW', '连城': 'LCX', '洛阳': 'LYA', '丽江': 'LJG', '牡丹江': 'MDG',
                '满洲里': 'NZH', '梅州': 'MXZ', '绵阳': 'MIG', '南昌': 'KHN', '南充': 'NAO', '宁波': 'NGB', '南阳': 'NNY', '南京': 'NKG',
                '南通': 'NTG', '南宁': 'NNG', '鄂尔多斯': 'DSN', '攀枝花': 'PZI', '秦皇岛': 'BPE', '衢州': 'JUZ', '琼海': 'BAR',
                '青岛': 'TAO', '泉州': 'JJN', '日照': 'RIZ', '石家庄': 'SJW', '三亚': 'SYX', '三清山': 'SQD', '深圳': 'SZX',
                '沈阳': 'SHE', '上海': 'PVG', '三明': 'SQJ', '松原': 'YSQ', '上海': 'SHA', '十堰': 'WDS', '唐山': 'TVS',
                '铜仁': 'TEN', '太原': 'TYN', '腾冲': 'TCZ', '台州': 'HYN', '吐鲁番': 'TLQ', '天津': 'TSN', '温州': 'WNZ',
                '武夷山': 'WUS', '无锡': 'WUX', '乌鲁木齐': 'URC', '乌海': 'WUA', '万州': 'WXN', '武汉': 'WUH', '威海': 'WEH',
                '忻州': 'WUT', '西双版纳': 'JHG', '襄阳': 'XFN', '西安': 'XIY', '西昌': 'XIC', '厦门': 'XMN', '兴义': 'ACX',
                '徐州': 'XUZ', '西宁': 'XNN', '伊宁': 'YIN', '义乌': 'YIW', '宜昌': 'YIH', '宜春': 'YIC', '盐城': 'YNZ', '宜宾': 'YBP',
                '银川': 'INC', '扬州': 'YTY', '烟台': 'YNT', '岳阳': 'YYA', '榆林': 'UYN', '运城': 'YCU', '延吉': 'YNJ', '中卫': 'ZHY',
                '湛江': 'ZHA', '张家口': 'ZQZ', '张家界': 'DYG', '遵义新舟': 'ZYI', '遵义茅台': 'WMT', '临汾': 'LFQ', '珠海': 'ZUH',
                '郑州': 'CGO', '扎兰屯': 'NZL', '舟山': 'HSN'}
        for key, value in dict.items():
            if value == citycode:
                return key
    except:
        print("获取城市名字出错")


print(getCityName('PKX'))

