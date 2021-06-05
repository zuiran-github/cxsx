import json
import requests
from json import loads
from math import radians,sin,cos,asin,sqrt
#调用百度API
#调用高德API
myAK='5tHbBCtfbrlAajfBy6iYKfG1RNrvjG6O'
def getapiurl(myaddress):
    url=r"http://api.map.baidu.com/geocoding/v3/?address={}&output=json&ak={}".format(myaddress,myAK)#说明文档里给出的api接口
    return url

def getPosition(url):
    '''返回经纬度信息'''
    res = requests.get(url)
    json_data = json.loads(res.text)

    if json_data['status'] == 0:
        lat = json_data['result']['location']['lat']  # 纬度
        lng = json_data['result']['location']['lng']  # 经度
    else:
        print("Error output!")
        return json_data['status']
    return lat, lng

def getdistance(startlat,startlng,endlat,endlng):
    #{: .6f}保留小数点后六位
    distanceurl=r"http://api.map.baidu.com/directionlite/v1/walking?origin={:.6f},{:.6f}&destination={:.6f},{:.6f}&ak={}".format(startlat,startlng,endlat,endlng,myAK)
    res = requests.get(distanceurl)
    dis_json_data = json.loads(res.text)
    if dis_json_data['status'] == 0:
        distance=dis_json_data['result']['routes'][0]['distance']
        distance=format(distance/1000, '.2f')
        # print(distance)
        return distance

# if __name__=='__main__':
#     myAK = 'G4b4UrDhT23CSbWmyOrcGyxsDi37KPsd'
#     starturl=getapiurl(str('上海市杨浦区长阳路860号'))
#     startlat,startlng=getPosition(starturl)
#     endurl=getapiurl(str('上海市普陀区梅川路1558号'))
#     endlat, endlng = getPosition(endurl)
#     getdistance(startlat, startlng,endlat, endlng)

#调用高德API
KEY = 'cb5071a542abea5c6ab88f2640335d15'
#获得地址的经纬度，即location
def get_geocode(address):
    #用于输出和字符串拼接
    # global flag
    #参数列表key和address
    data = {
        'key':KEY,
        'address':address,
    }
    #向api发送get请求
    url = 'http://restapi.amap.com/v3/geocode/geo'
    res = requests.get(url,data)
    #将json数据加载为子典
    result = loads(res.text)
    return result['geocodes'][0]['location']

#高德地图所提供的API,误差较大,可能是非直线距离
def distance_calc(startloc , endloc):
    url = 'http://restapi.amap.com/v3/distance'
    data = {
        'key':KEY,
        'origins':startloc,
        'destination':endloc,
    }
    res = requests.get(url,data)
    result = loads(res.text)

#计算精确
def distance_calc_two(startloc , endloc):
    # global finally_result
    startloc = startloc + ',' + endloc
    # 将十进制度数转化为弧度
    lon1 , lat1 ,lon2 , lat2 = map(radians,[float(i) for i in startloc.split(',')])
    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    # 地球平均半径，单位为公里
    r = 6371
    return '%.3f'%(r * c)
    # print(finally_result + u'公里')

def gaode(location_1,location_2):
    start=get_geocode(location_1)
    end=get_geocode(location_2)
    return  (distance_calc_two(start,end))


# finally_result = ''
# print(gaode('淀山湖大道风景区 上海市青浦区淀山湖大道与珠湖路交叉口东80米','上海佳美田园酒店'))