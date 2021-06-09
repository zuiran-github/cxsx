from .getCityname import *

def getTZURL(dep, arr, acity, dcity, day, airlineCode):
    '''
    获取跳转URL
    :param dep: 大写城市代码
    :param arr: 大写城市代码
    :param acity: 到达机场名称
    :param dcity: 出发机场名称
    :param day: 2021-05-26
    :param airlineCode: 航班编号
    :return: 字符串跳转链接
    '''

    try:

        # print(arr, dep)

        # 山东航空日期210504
        daySD = day[2:4] + day[5:7] + day[8:10]

        # 厦门航空 一地多机场分别查询
        arrXM = arr
        depXM = dep


        # 河北航空
        arrHB = arr
        depHB = dep
        # print(arrHB, depHB)

        # 联航 上海的搜索为CitCnSHANGHA364  北京为BJS
        arrLH = 'CITY_' + arr + '_CN'
        depLH = 'CITY_' + dep + '_CN'

        # 西部航空 上海为PVG
        arrXB = arr
        depXB = dep

        if arr == 'SHA':
            arrLH = 'CitCnSHANGHA364'
            arrXM = getCityID('上海' + acity[:2])
            arrHB = 'PVG'
            arrXB = 'PVG'
        if dep == 'SHA':
            depLH = 'CitCnSHANGHA364'
            depXM = getCityID('上海' + dcity[:2])
            depHB = 'PVG'
            depXB = 'PVG'

        # 吉祥 上海SHA 北京PEK
        arrJX = arr
        depJX = dep

        # 山东 上海SHA 北京PEK
        arrSD = arr
        depSD = dep

        if arr == 'BJS':
            arrJX = 'PEK'
            arrXM = getCityID(acity[:4])
            arrHB = 'PKX'
            arrSD = 'pek'
            # arrLH = 'PKX'

        if dep == 'BJS':
            depJX = 'PEK'
            depXM = getCityID(dcity[:4])
            depHB = 'PKX'
            depSD = 'pek'
            # depLH = 'PKX'

        acityname = getCityName(arr)
        dcityname = getCityName(dep)

        acitynameHB = getCityName(arrHB)
        dcitynameHB = getCityName(depHB)

        if arrHB == 'PKX':
            acitynameHB = '北京大兴'
        if arrHB == 'PVG':
            acitynameHB = '上海浦东'
        if depHB == 'PKX':
            dcitynameHB = '北京大兴'
        if depHB == 'PVG':
            dcitynameHB = '上海浦东'

        # print(acitynameHB, dcitynameHB)

        # print(acityname)
        # print(dcityname)

        tzurlMap = {

            # 厦门
            'MF': 'https://www.xiamenair.com/zh-cn/nticket.html?tripType=OW&orgCodeArr%5B0%5D=' + depXM + \
                  '&dstCodeArr%5B0%5D=' + arrXM + \
                  '&orgDateArr%5B0%5D=' + day + \
                  '&dstDate=&isInter=false&adtNum=1&chdNum=0&JFCabinFirst=false&acntCd=&mode=Money&partner=false&jcgm=false',

            # 山东https://flights.sda.cn/flight/search/TNA-SHA-210623-1
            'SC': 'https://flights.sda.cn/flight/search/' + depSD + '-' + arrSD + '-' + daySD + '-1',

            # 深圳
            'ZH': 'http://www.shenzhenair.com/szair_B2C/flightsearch.action?'
                  'hcType=DC&constId=&type=%E5%8D%95%E7%A8%8B'
                  '&orgCity=%E4%B8%8A%E6%B5%B7%E8%99%B9%E6%A1%A5'
                  '&orgCityCode=' + dep +
                  '&dstCity=%E6%B5%8E%E5%8D%97'
                  '&dstCityCode=' + arr +
                  '&orgDate=' + day +
                  '&dstDate=' + day +
                  '&quiz=Y&quiz=1',

            # 吉祥
            'HO': 'http://www.juneyaoair.com/pages/Flight/flight.aspx?' \
                  'flightType=OW' \
                  '&sendCity=%E4%B8%8A%E6%B5%B7' \
                  '&sendCode=' + depJX + \
                  '&arrCity=%E8%A5%BF%E5%AE%89' \
                  '&arrCode=' + arrJX + \
                  '&directType=N' \
                  '&tripType=D' \
                  '&departureDate=' + day + \
                  '&returnDate=',

            # 东航 日期格式'210420'
            'MU': 'http://www.ceair.com/booking/' + dep +
                  '-' + arr + '-' + daySD +
                  '_CNY.html?seriesid=ec53ec609db011ebbf7dbff53ea62a3b',

            # 春秋
            '9C': 'https://flights.ch.com/' + dep + '-' + arr + '.html?' \
                                                                'Departure=%E6%98%86%E6%98%8E' \
                                                                '&Arrival=%E4%B8%8A%E6%B5%B7' \
                                                                '&FDate=' + day + \
                  '&RetDate=2021-07-22' \
                  '&DepartCityCode=' \
                  '&ArriveCityCode=' \
                  '&IsSearchDepAirport=false' \
                  '&IsSearchArrAirport=false' \
                  '&isOnlyZf=false' \
                  '&ANum=1' \
                  '&CNum=0' \
                  '&INum=0' \
                  '&MType=0' \
                  '&IfRet=false' \
                  '&SType=012' \
                  '&isBg=false' \
                  '&IsJC=false' \
                  '&IsNew=1',

            # 国航 待修改(没有固定的参数，依据上次搜所得到数据）
            'CA': 'http://et.airchina.com.cn',

            # 海航 待修改(一串数字）
            'HU': 'https://www.hnair.com',
            # 'https://new.hnair.com/hainanair/ibe/air/searchResults.do?'
            #   'telassa-id=IbeNotLogin%7E5C5F2CF573E7BF9359FFBA26F7B2592A%7Ehu-dev-PRD-0a08e4c4-450301-173456'
            #   '&_catRootMessageId=hu-dev-PRD-0a08e4c4-450301-173456'
            #   '&_catParentMessageId=hu-dev-PRD-0a08e4c4-450301-173456'
            #   '&_catChildMessageId=hu-dev-PRD-0a08e4c4-450301-173731',

            # 联航 到搜索界面但不能填好参数
            'KN': 'http://www.flycua.com/booking/search.html?'
                  'flightType=oneway'
                  '&Origin=' + depLH +
                  '&Destination=' + arrLH +
                  '&departDate=' + day +
                  '&adults=1&children=0&militaryDisability=0&policeRemnants=0',

            # 奥凯 待修改，不显示参数
            'BK': 'https://www.okair.net/#/',

            # 川航 同海航
            '3U': 'https://www.sichuanair.com',

            # 天津航空 不显示参数
            'GS': 'http://www.tianjin-air.com/flight/select.html',

            # 首航
            'JD': 'https://www.jdair.net/b2c-flight/searchflight.action?'
                  '&tripType=OW'
                  '&orgCity=' + dep +
                  '&dstCity=' + arr +
                  '&flightDate=' + day +
                  '&returnDate='
                  '&blackBox=eyJ2Ijoid0RlNDlBL3daMXR0eHl5OHNQck9xZWNDdGo0R0hUMWsrY0lGaFNBaGYxcjdLdEpEUFFHZlUwLzRoWDdFRXZ0SyIsIm9zIjoid2ViIiwiaXQiOjc0OCwidCI6Im1udU9WVzJwb1lyVXFHQUtXakNqd3hJdGpuVFVGUTJwOHN3Z1lUM1FYUzh3WmlIMzg1N2hYQTBQMG5UM3dwRDZSMTBYWmpqd2VyNVlEYlFRRkxQSEVnPT0ifQ==',

            # 西藏航空 不显示参数
            'TV': 'https://www.tibetairlines.com.cn/stdair/searchResults/searchResultsOnewayTSDF',

            # 上航 同东航
            'FM': 'http://www.ceair.com/booking/' + dep +
                  '-' + arr + '-' + daySD +
                  '_CNY.html?seriesid=ec53ec609db011ebbf7dbff53ea62a3b',

            # 华夏航空 无参数
            'G5': 'https://www.chinaexpressair.com/yss/flight-search/bookingOneTrip#',

            # 九元 无参数
            'AQ': 'http://www.9air.com/zh-CN/book/booking',

            # 成都航空 无参数
            'EU': 'https://www.cdal.com.cn/stdair/searchResults/searchResultsOnewayTSDF',

            # 长安航空  无参数
            '9H': 'http://www.airchangan.com/mainprocess/select',

            # 长龙航空  无参数
            'GJ': 'https://www.loongair.cn/#/web/ticket/search',

            # 东海航空
            'DZ': 'https://www.donghaiair.com/html/booking-manage/choose-flight-two.html?'
                  'flightType=1'
                  '&orgCode=' + dep +
                  '&destCode=' + arr +
                  '&starCity=' + dcityname +
                  '&arrviceCity=' + acityname +
                  '&departureDateStr=' + day +
                  '&returnDateStr=' + day +
                  '&adult=1&child=0&infant=0&airCode=DZ&direct=true&noneStop=true',

            # 金鹏航空  主页
            'Y8': 'https://www.yzr.com.cn/flight/searchflight.action?'
                  'tripType=ONEWAY'
                  '&orgCity1=' + dep +
                  '&dstCity1=' + arr +
                  '&flightdate1=' + day +
                  '&flightdate2=',

            # 昆明航空  主页
            'KY': 'https://www.airkunming.com/#/',

            # 新华航空 主页 加入海南航空
            'X2': 'http://www.juneyaoair.com/pages/Flight/flight.aspx?' \
                  'flightType=OW' \
                  '&sendCity=%E4%B8%8A%E6%B5%B7' \
                  '&sendCode=' + depJX + \
                  '&arrCity=%E8%A5%BF%E5%AE%89' \
                  '&arrCode=' + arrJX + \
                  '&directType=N' \
                  '&tripType=D' \
                  '&departureDate=' + day + \
                  '&returnDate=',

            # 幸福航空 主页
            'JR': 'http://www.joy-air.com/b2c/static/searchFlight.html?'
                  'orgCityCode=' + dep +
                  '&dstCityCode=' + arr +
                  '&orgDate=' + day +
                  '&dstDate=&adult=1&child=0&infant=0&trip=ONEWAY',

            # 云南航空 主页 加入东航
            '3Q': 'http://www.ceair.com/booking/' + dep +
                  '-' + arr + '-' + daySD +
                  '_CNY.html?seriesid=ec53ec609db011ebbf7dbff53ea62a3b',

            # 新疆乌鲁木齐航空
            'UQ': 'http://www.urumqi-air.com',

            # 中原航空 加入南航改为南航代码
            # 'Z2': '',

            # 武汉航空 加入东航
            'WU': 'http://www.ceair.com/booking/' + dep +
                  '-' + arr + '-' + daySD +
                  '_CNY.html?seriesid=ec53ec609db011ebbf7dbff53ea62a3b',

            # 贵州航空
            'GY': 'https://www.cgzair.com',

            # 通用航空 货运
            # 'GP': '',

            # 南京航空 货运
            '3W': '',

            # 浙江航空 东航管理
            'ZJ': '',

            # 祥鹏航空
            '8L': 'https://www.luckyair.net/flight/search.html',

            # 福州航空
            'FU': 'https://www.fuzhou-air.cn/b2c/search/searchflight.jsp?'
                  'type=TKT'
                  '&orgCityCode=' + dep +
                  '&dstCityCode=' + arr +
                  '&orgDate=' +day +
                  '&dstDate=&adult=1&child=0&infant=0&trip=ONEWAY',

            # 西部航空
            'PN': 'https://new.westair.cn/flights/results/'
                  '' + depXB +
                  '-'
                  '' + arrXB +
                  '-'
                  '' + daySD +
                  '-100-0',

            # 河北航空
            'NS': 'https://www.hbhk.com.cn/queryFlight?'
                  'departureCiry=' + depHB +
                  '&depsName=' + dcitynameHB +
                  '&startInter=0'
                  '&endInter=0'
                  '&arrivalCity=' + arrHB +
                  '&arrName=' + acitynameHB +
                  '&adtNum=1&chdNum=0&infNum=0&type=buyticket'
                  '&takeOffDate=' + day,
        }

        return tzurlMap[airlineCode]

    except:
        print("获取跳转链接出错")


def getCityID(cityname):
    '''
    :param cityname: 北京大兴
    :return: 大写城市代码
    '''

    try:
        dict = {'安庆': 'AQG', '阿克苏': 'AKU', '北海': 'BHY', '毕节': 'BFJ', '包头': 'BAV', '北京大兴': 'PKX', '北京首都': 'PEK',
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
                '沈阳': 'SHE', '上海浦东': 'PVG', '三明': 'SQJ', '松原': 'YSQ', '上海虹桥': 'SHA', '十堰': 'WDS', '唐山': 'TVS',
                '铜仁': 'TEN', '太原': 'TYN', '腾冲': 'TCZ', '台州': 'HYN', '吐鲁番': 'TLQ', '天津': 'TSN', '温州': 'WNZ',
                '武夷山': 'WUS', '无锡': 'WUX', '乌鲁木齐': 'URC', '乌海': 'WUA', '万州': 'WXN', '武汉': 'WUH', '威海': 'WEH',
                '忻州': 'WUT', '西双版纳': 'JHG', '襄阳': 'XFN', '西安': 'XIY', '西昌': 'XIC', '厦门': 'XMN', '兴义': 'ACX',
                '徐州': 'XUZ', '西宁': 'XNN', '伊宁': 'YIN', '义乌': 'YIW', '宜昌': 'YIH', '宜春': 'YIC', '盐城': 'YNZ', '宜宾': 'YBP',
                '银川': 'INC', '扬州': 'YTY', '烟台': 'YNT', '岳阳': 'YYA', '榆林': 'UYN', '运城': 'YCU', '延吉': 'YNJ', '中卫': 'ZHY',
                '湛江': 'ZHA', '张家口': 'ZQZ', '张家界': 'DYG', '遵义新舟': 'ZYI', '遵义茅台': 'WMT', '临汾': 'LFQ', '珠海': 'ZUH',
                '郑州': 'CGO', '扎兰屯': 'NZL', '舟山': 'HSN', '北京': 'BJS', '上海': 'SHA'}
        cityID = dict[cityname]

    except:
        print('输入城市名称有误')
    return cityID


dcity = '北京大兴国际机场'
acity = '上海浦东机场'

day = '2021-06-21'
arr = 'BJS'
dep = 'SHA'


# 山东航空日期210504
daySD = day[2:4] + day[5:7] + day[8:10]


# 厦门航空 一地多机场分别查询
arrXM = arr
depXM = dep


# 联航 上海的搜索为CitCnSHANGHA364  北京为BJS
arrLH = 'CITY_' + arr + '_CN'
depLH = 'CITY_' + dep + '_CN'
if arr == 'SHA':
    arrLH = 'CitCnSHANGHA364'
    arrXM = getCityID(acity[:4])
if dep == 'SHA':
    depLH = 'CitCnSHANGHA364'
    depXM = getCityID(dcity[:4])


# 吉祥 上海SHA 北京PEK
arrJX = arr
depJX = dep
if arr == 'BJS':
    arrJX = 'PEK'
    arrXM = getCityID(acity[:4])
if dep == 'BJS':
    depJX == 'PEK'
    depXM = getCityID(dcity[:4])








tzurlMap = {

        # 厦门
        'MF': 'https://www.xiamenair.com/zh-cn/nticket.html?tripType=OW&orgCodeArr%5B0%5D=' + dep + \
              '&dstCodeArr%5B0%5D=' + arr + \
              '&orgDateArr%5B0%5D=' + day + \
              '&dstDate=&isInter=false&adtNum=1&chdNum=0&JFCabinFirst=false&acntCd=&mode=Money&partner=false&jcgm=false',

        # 山东https://flights.sda.cn/flight/search/TNA-SHA-210623-1
        'SC': 'https://flights.sda.cn/flight/search/' + dep + '-' + arr + '-' + daySD + '-1',

        # 深圳
        # 'ZH': 'http://www.shenzhenair.com/szair_B2C/flightsearch.action?' \
        #       'orgCityCode=' + dep + \
        #       '&dstCityCode=' + arr + \
        #       '&hcType=DC&orgCity=%E4%B8%8A%E6%B5%B7%E8%99%B9%E6%A1%A5&dstCity=%E6%B7%B1%E5%9C%B3' \
        #       '&orgDate=' + day + \
        #       '&dstDate=' + day + \
        #       '&quiz=Y&quiz=1',
        'ZH': 'http://www.shenzhenair.com/szair_B2C/flightsearch.action?'
              'hcType=DC&constId=&type=%E5%8D%95%E7%A8%8B'
              '&orgCity=%E4%B8%8A%E6%B5%B7%E8%99%B9%E6%A1%A5'
              '&orgCityCode=' + dep +
              '&dstCity=%E6%B5%8E%E5%8D%97'
              '&dstCityCode=' + arr +
              '&orgDate=' + day +
              '&dstDate=' + day +
              '&quiz=Y&quiz=1',

        # 吉祥
        'HO': 'http://www.juneyaoair.com/pages/Flight/flight.aspx?' \
              'flightType=OW' \
              '&sendCity=%E4%B8%8A%E6%B5%B7' \
              '&sendCode=' + depJX + \
              '&arrCity=%E8%A5%BF%E5%AE%89' \
              '&arrCode=' + arrJX + \
              '&directType=N' \
              '&tripType=D' \
              '&departureDate=' + day + \
              '&returnDate=',

        # 东航 日期格式'210420'
        'MU': 'http://www.ceair.com/booking/' + dep +
              '-' + arr + '-' + daySD +
              '_CNY.html?seriesid=ec53ec609db011ebbf7dbff53ea62a3b',

        # 春秋
        '9C': 'https://flights.ch.com/' + dep + '-' + arr + '.html?' \
                                                            'Departure=%E6%98%86%E6%98%8E' \
                                                            '&Arrival=%E4%B8%8A%E6%B5%B7' \
                                                            '&FDate=' + day + \
              '&RetDate=2021-07-22' \
              '&DepartCityCode=' \
              '&ArriveCityCode=' \
              '&IsSearchDepAirport=false' \
              '&IsSearchArrAirport=false' \
              '&isOnlyZf=false' \
              '&ANum=1' \
              '&CNum=0' \
              '&INum=0' \
              '&MType=0' \
              '&IfRet=false' \
              '&SType=012' \
              '&isBg=false' \
              '&IsJC=false' \
              '&IsNew=1',

        # 国航 待修改(没有固定的参数，依据上次搜所得到数据）
        'CA': 'http://et.airchina.com.cn',

        # 海航 待修改(一串数字）
        'HU': 'https://www.hnair.com',
            # 'https://new.hnair.com/hainanair/ibe/air/searchResults.do?'
            #   'telassa-id=IbeNotLogin%7E5C5F2CF573E7BF9359FFBA26F7B2592A%7Ehu-dev-PRD-0a08e4c4-450301-173456'
            #   '&_catRootMessageId=hu-dev-PRD-0a08e4c4-450301-173456'
            #   '&_catParentMessageId=hu-dev-PRD-0a08e4c4-450301-173456'
            #   '&_catChildMessageId=hu-dev-PRD-0a08e4c4-450301-173731',

        # 联航 到搜索界面但不能填好参数
        'KN': 'http://www.flycua.com/booking/search.html?'
              'flightType=oneway'
              '&Origin=' + depLH +
            '&Destination=' + arrLH +
            '&departDate=' + day +
              '&adults=1&children=0&militaryDisability=0&policeRemnants=0',

        # 奥凯 待修改，不显示参数
        'BK': 'https://www.okair.net/#/',

        # 川航 同海航
        '3U': 'https://www.sichuanair.com',

        # 天津航空 不显示参数
        'GS': 'http://www.tianjin-air.com/flight/select.html',

        # 首航
        'JD': 'https://www.jdair.net/b2c-flight/searchflight.action?'
              '&tripType=OW'
              '&orgCity=' + dep +
              '&dstCity=' + arr +
              '&flightDate=' + day +
              '&returnDate='
              '&blackBox=eyJ2Ijoid0RlNDlBL3daMXR0eHl5OHNQck9xZWNDdGo0R0hUMWsrY0lGaFNBaGYxcjdLdEpEUFFHZlUwLzRoWDdFRXZ0SyIsIm9zIjoid2ViIiwiaXQiOjc0OCwidCI6Im1udU9WVzJwb1lyVXFHQUtXakNqd3hJdGpuVFVGUTJwOHN3Z1lUM1FYUzh3WmlIMzg1N2hYQTBQMG5UM3dwRDZSMTBYWmpqd2VyNVlEYlFRRkxQSEVnPT0ifQ==',

        # 西藏航空 不显示参数
        'TV': 'https://www.tibetairlines.com.cn/stdair/searchResults/searchResultsOnewayTSDF',

        # 上航 同东航
        'FM': 'http://www.ceair.com/booking/' + dep +
              '-' + arr + '-' + daySD +
              '_CNY.html?seriesid=ec53ec609db011ebbf7dbff53ea62a3b',

        # 华夏航空 无参数
        'G5': 'https://www.chinaexpressair.com/yss/flight-search/bookingOneTrip#',

        # 九元 无参数
        'AQ': 'http://www.9air.com/zh-CN/book/booking',

        # 成都航空 无参数
        'EU': 'https://www.cdal.com.cn/stdair/searchResults/searchResultsOnewayTSDF',

        # 长安航空  无参数
        '9H': 'http://www.airchangan.com/mainprocess/select',
    }

print(tzurlMap)