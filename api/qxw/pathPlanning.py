#路线规划
#在确定酒店位置的前提下，根据酒店所在的位置，利用百度地图API检索周边景点，并根据景点位置以轮图的形式呈现给用户
#以酒店为中心，在酒店与任意景点、任意景点与其相邻景点之间连接路线
#这个任务为我的新增任务
#主要实现方法为：
#以酒店为中心，计算出酒店到其他各个景点的距离，遍历每一个景点，计算这个景点到其他所有景点的距离，找到最近地点
#即为相邻景点
from distance import getPosition,getapiurl
from dataProcessing import distance,get_lng_lat
import json
#输入为酒店和景点
#前端要求传入地点坐标，也就是经纬度，输出形式如下：
# {paths: [
#         [
#           { lng: 121.6292529148, lat: 31.2035397816 },
#           { lng: 121.6282529148, lat: 31.2045397816 },
#         ],
#         [
#           { lng: 121.6292529148, lat: 31.2035397816 },
#           { lng: 121.6302529148, lat: 31.2035397816 },
#         ],
#       ],
#       center: { lng: 121.6292529148, lat: 31.2035397816 }}
def qxw_path(hotel,places):
    #景点之间的距离矩阵
    #初始值均为99999,表示两个点之间没有边
    matrix_1=[[0 for i in range(len(places))] for i in range(len(places))]
    for i in range(len(places)):
        for j in range(len(places)):
            matrix_1[i][j]=99999
            matrix_1[j][i]=99999
    #计算出相邻两个景点之间的距离
    for i in range(len(places)):
        #找到每个景点的相邻景点，即最近点
        #先计算出每个景点到别的地点的距离
        temp_1=9999.9
        nearest=i
        for j in range(len(places)):
            #如果当前点是该景点本身，则跳过
            if(j==i):
                continue
            temp_2=float(distance(places[i],places[j]))
            if(temp_2<temp_1):
                temp_1=temp_2
                nearest=j
        matrix_1[i][nearest]=temp_1
        matrix_1[nearest][i]=temp_1
    result={}
    paths=[]
    #先将景点之间的边加入路径集
    for i in range(len(places)):
        for j in range(len(places)):
            if(j<=i):
                continue
            #两点之间有通路
            if(matrix_1[i][j]<9999):
                temp_31,temp_32=get_lng_lat(places[i])
                position_1={}
                position_1['lng']=temp_31 #经度
                position_1['lat']=temp_32 #纬度
                temp_41,temp_42=get_lng_lat(places[j])
                position_2={}
                position_2['lng']=temp_41
                position_2['lat']=temp_42
                paths.append([position_1,position_2])
    #再将酒店与景点之间的边加入路径集
    #酒店的经纬度
    temp_51,temp_52 = get_lng_lat(hotel)
    temp_6 = {}
    temp_6['lng'] = temp_51
    temp_6['lat'] = temp_52
    for i in range(len(places)):
        temp_71,temp_72=get_lng_lat(places[i])
        temp_8={}
        temp_8['lng']=temp_71
        temp_8['lat']=temp_72
        paths.append([temp_6,temp_8])
    print(len(paths))
    result['paths']=paths
    result['center']=temp_6
    output=json.dumps(result)
    return output

# #test
# hotel='上海V8连锁宾馆'
# places=['上海文庙 文庙路215号','人民公园 上海市黄浦区南京西路231号','黄兴公园 上海市杨浦区营口路639号','白云观 上海市黄浦区大境路239号']
# print(path(hotel,places))