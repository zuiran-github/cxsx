from .distance import *
from pypinyin import lazy_pinyin
import re
import time
from .LR import *
import os
import json
import requests
'''
连接数据库
'''
import pymysql

def database_connect():
    db = pymysql.connect(
        host='8.140.178.29',
        port=3306,
        user='cxsx',
        passwd='cxsx123',
        db='cxsx',
        charset='utf8'
    )

    # 使用cursor()方法创建一个游标对象cursor
    cursor = db.cursor()
    return cursor

#获取训练数据
def load_data():
    sql_data='select * from lr_data'
    cursor.execute(sql_data)
    results_data=cursor.fetchall()      #此处数据形式为[id,hotel_name,time,distance,score,comments,price]
    train_data_x=[]
    train_data_y=[]
    for row in results_data:
        train_data_x.append([row[3],row[4],row[5],row[6]])
        train_data_y.append(1)
    sql_unclick='select * from distance where hotel not in(select hotel_name from lr_data)'
    cursor.execute(sql_unclick)
    results_unclick=cursor.fetchall()
    for row in results_unclick:
        i=0
        train_data_x.append([row[2],row[3],row[4],row[5]])
        train_data_y.append(0)
        i=i+1
        if(i>20):
            break
    return train_data_x,train_data_y

#计算逻辑回归模型的权重
#将计算出来的权重存入数据库
def update_weights(weights):
    nowtime=int(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
    values=(weights[0],weights[1],weights[3],weights[4],nowtime)
    sql_lr="update lrweights set weight_1=%s,weight_2=%s,weight_3=%s,weight_4=%s,train_time=%s"
    cursor.execute(sql_lr,values)
    db.commit()

#从数据库中获取逻辑回归模型权重
def get_weights():
    sql_LR="select * from lrweights"
    cursor.execute(sql_LR)
    weights=cursor.fetchone()
    return weights

#将从前端获取的用户点击行为存入数据库
#每点击一次，存储一次，存储的数据为[id,hotel_name,time],time为存储时间
#id每十分钟更新一次，从0开始，递增
def qxw_clicks_saving(hotel_name,distance,score,comments,price):
    try:
        #先搜索出当前id下的最早时间
        sql_temp='select max(id_data),min(time) from lr_data'
        cursor.execute(sql_temp)
        result_data=cursor.fetchone()
        # print(result_data)
        time_early=result_data[1]
        id=result_data[0]
        #获取当前时间前十分钟
        time_1=int(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
        time_2=int(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()-600)))
        #如果当前ID最早时间早于当前时间前十分钟，id+1
        #否则仍然使用当前id
        if(time_early<time_2):
            id=id+1
        values=(id,hotel_name,time_1,distance,score,comments,price)
        sql_click='insert into lr_data (id_data,hotel_name,time,distance,score,comments,price) values (%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql_click,values)
        db.commit()

        #搜索出上次训练时间
        sql_train='select max(train_time) from lrweights'
        cursor.execute(sql_train)
        last_train_time=cursor.fetchone()[0]
        #若距离上次训练时间已经过去了十分钟，则再次训练
        # if(last_train_time<time_2):
        #     x,y=load_data()
        #     LR(x,y)
    except Exception as e:
        print(e)

#去哪儿
def getCityName(city):
    if city =='天津' or city =='上海' or city =='北京' or city =='重庆':
        citypinyin = "".join(lazy_pinyin(city))+'_city'
        #print(citypinyin)
    else:
        citypinyin = "".join(lazy_pinyin(city))
        #print(citypinyin)
    return citypinyin

#飞猪
def getCityId(cityn):
    with open('/Users/zuiran/Documents/大三下/创新实训/proj4/api/qxw/pig.txt','r', encoding='utf-8') as f:
        data = f.read().replace(' ','')  # 读取文件
        data = data.replace('区','').replace('市','').replace('县','')
        find_city = re.findall(r'\"name.*?\"\:\"(.*?)\"', data)
        find_city_code=re.findall(r'code.*?\"\:\"(.*?)\"\,',data)
    city_dict = {}
    for city,code in zip(find_city,find_city_code):
        city_dict[city] = code
    cityc = city_dict[cityn]
    return cityc

#获取酒店链接
def getLink(city_name,id,checkin,checkout,web_name):
    #根据网站名和id返回链接
    if(web_name=='去哪儿'):
        citypinyin=getCityName(city_name)
        link='https://hotel.qunar.com/cn/{}/dt-{}?fromDate={}&toDate={}/'.format(citypinyin, id, checkin, checkout)
        return link
    elif(web_name=='途牛'):
        link='https://hotel.tuniu.com/detail/{}?checkInDate={}&checkOutDate={}'.format(id,checkin,checkout)
        return link
    elif(web_name=='飞猪'):
        citycode=getCityId(city_name)
        link='https://hotel.fliggy.com/hotel_detail2.htm?shid={}&city={}&checkIn={}&checkOut={}&searchId=4811e8b3defc48fe92d7698b9842bbb5&_output_charset=utf8'.format(id, citycode, checkin, checkout)
        return link
    elif(web_name=='携程'):
        link='https://hotels.ctrip.com/hotels/detail/?hotelId={}&checkIn={}&checkOut={}&cityId=2'.format(id,checkin,checkout)
        return link
    elif(web_name=='艺龙'):
        link='http://hotel.elong.com/{}/?indate={}&outdate={}'.format(id,checkin,checkout)
        return link

#计算两个地点之间的直线距离
def distance(location_1,location_2):
    #先使用高德地图，如果失败，再使用百度地图
    try:
        if(float(gaode(location_1,location_2))>300):
            starturl = getapiurl(str(location_1))
            startlat, startlng = getPosition(starturl)
            endurl = getapiurl(str(location_2))
            endlat, endlng = getPosition(endurl)
            return float(getdistance(startlat, startlng, endlat, endlng))
        else:
            return float(gaode(location_1,location_2))
    except:
        starturl=getapiurl(str(location_1))
        startlat,startlng=getPosition(starturl)
        endurl=getapiurl(str(location_2))
        endlat, endlng = getPosition(endurl)
        return float(getdistance(startlat, startlng,endlat, endlng))

#计算某个地点的经纬度
#先输出经度，再输出纬度
def get_lng_lat(address):
    #先使用高德API，因为速度较快
    try:
        lat,lng=getPosition(getapiurl(address))
        return lng,lat
        #先输出经度，再输出纬度
        lng ,lat=get_geocode(address)
        return lng,lat
    #高德出现异常再使用百度地图API
    except:
        #先输出纬度，再输出经度
        lat,lng=getPosition(getapiurl(address))
        return lng,lat

#从数据库中获取景点与与所有酒店之间的距离,并筛选类型
def get_distanceFromDB(position,type,cursor):
    if(type=='全部'):
        temp_sql="select * from distance where position like %s "
        cursor.execute(temp_sql,'%'+position+'%')
        temp_results=cursor.fetchall()
        results=[]
        for row in temp_results:
            results.append([row[1],row[2],row[3],row[4],row[5],row[6]])
        #输出形式为：[酒店名，距离，评分，评论数，价格，类型]
        return results
    else:
        temp_sql="select * from distance where position like %s and type=%s"
        values=('%'+position+'%',type)
        cursor.execute(temp_sql,values)
        temp_results=cursor.fetchall()
        results=[]
        for row in temp_results:
            results.append([row[1],row[2],row[3],row[4],row[5],row[6]])
        #输出形式为：[酒店名，距离，评分，评论数，价格，类型]
        return results

#从数据库中获取景点与与所有酒店之间的距离,并筛选类型,且在最后加上地点
def get_distanceFromDB_1(position,type,cursor):
    # cursor=database_connect()
    if(type=='全部'):
        temp_sql="select * from distance where position like %s "
        cursor.execute(temp_sql,'%'+position+'%')
        temp_results=cursor.fetchall()
        results=[]
        for row in temp_results:
            results.append([row[1],row[2],row[3],row[4],row[5],row[6],position])
        #输出形式为：[酒店名，距离，评分，评论数，价格，类型]
        return results
    else:
        temp_sql="select * from distance where position like %s and type=%s"
        values=('%'+position+'%',type)
        cursor.execute(temp_sql,values)
        temp_results=cursor.fetchall()
        results=[]
        for row in temp_results:
            results.append([row[1],row[2],row[3],row[4],row[5],row[6],position])
        #输出形式为：[酒店名，距离，评分，评论数，价格，类型]
        return results
#综合输出数据
#输入形式为：[酒店名称，距离，评分，评论，价格，类型，地点，综合评分]
#输出形式为：
    #[
    # {name :'美高智选酒店(济南万象城店)',
    # webs:
    #  [{website:'携程',distance:1, score:'4.7', comments:'980', price:'364', type:'舒适型', link:'',position:''},
    #  {website:'去哪儿',distance:1, score:'4.7', comments:'980', price:'364', type:'舒适型', link:'',position:''},
    #  {website:'飞猪',distance:1, score:'4.7', comments:'980', price:'364', type:'舒适型', link:'',position:''},
    #  {website:'途牛', distance:1,score:'4.7', comments:'980', price:'364', type:'舒适型', link:'',position:''},
    #  {website:'爱彼迎', distance:1,score:'4.7', comments:'980', price:'364', type:'舒适型', link:'',position:''}]
#       picture:''},{...}]
#目前我们只需要输出前100名酒店即可
#可以随时改变输出数量
def output(hotels,group,city,checkintime,checkouttime,cursor):
    output_number=20
    if(city=='上海'):
        sql_1 = "select * from hotel_web where Hotel_name=%s group by Web_name"
    elif(city=='济南'):
        sql_1 = "select * from hotel_jinan where Hotel_name=%s group by Web_name"
    else:
        sql_1 = "select * from hotel_beijin where Hotel_name=%s group by Web_name"

    #不分组
    if(group==0):
        results=[0 for i in range(output_number)]
        for i in range(output_number):
            #可能会出现部分酒店在这五个网站中不同时出现，此时判断结果是否为空，若为空，则结果集不为空，但是返回数据均为空
            results[i]=[]
            results[i].append(hotels[i][0])
            # sql_1="select * from hotel_web where Hotel_name=%s and Web_name=%s"
            # values_1=(hotels[i][0],'去哪儿')
            web_1 = ['去哪儿', hotels[i][1], hotels[i][2], hotels[i][3], 0, hotels[i][5],
                     None, hotels[i][6]]
            web_2 = ['飞猪', hotels[i][1], hotels[i][2], hotels[i][3], 0, hotels[i][5],
                     None, hotels[i][6]]
            web_3 = ['途牛', hotels[i][1], hotels[i][2], hotels[i][3], 0, hotels[i][5],
                     None, hotels[i][6]]
            web_4 = ['携程', hotels[i][1], hotels[i][2], hotels[i][3], 0, hotels[i][5],
                     None, hotels[i][6]]
            web_5 = ['艺龙', hotels[i][1], hotels[i][2], hotels[i][3], 0, hotels[i][5],
                     None, hotels[i][6]]
            cursor.execute(sql_1,hotels[i][0])
            results_1=cursor.fetchall()
            for row in results_1:
                if(row[1]=='去哪儿'):
                    web_1 = ['去哪儿', hotels[i][1], row[4],row[5] ,row[3], hotels[i][5],
                             getLink(city, row[6], checkintime, checkouttime, '去哪儿'), hotels[i][6]]
                if(row[1]=='携程'):
                    web_4 = ['携程', hotels[i][1], row[4],row[5] , row[3], hotels[i][5],
                             getLink(city, row[6], checkintime, checkouttime, '携程'), hotels[i][6]]
                if(row[1]=='飞猪'):
                    web_2 = ['飞猪', hotels[i][1], row[4],row[5] , row[3], hotels[i][5],
                             getLink(city, row[6], checkintime, checkouttime, '飞猪'), hotels[i][6]]
                if(row[1]=='途牛'):
                    web_3 = ['途牛', hotels[i][1], row[4],row[5] , row[3], hotels[i][5],
                             getLink(city, row[6], checkintime, checkouttime, '途牛'), hotels[i][6]]
                if(row[1]=='艺龙'):
                    web_5 = ['艺龙', hotels[i][1], row[4],row[5] , row[3], hotels[i][5],
                             getLink(city, row[6], checkintime, checkouttime, '艺龙'), hotels[i][6]]
            results[i].append([web_4,
                                       web_1,
                                       web_2,
                                       web_3,
                                       web_5])
                    # print(results_2)
            results[i].append(results_1[0][7])
        return results
    else:
        results=[0 for i in range(group)]
        for k in range(group):
            results[k]=[0 for i in range(output_number)]
            for i in range(output_number):
                # 可能会出现部分酒店在这五个网站中不同时出现，此时判断结果是否为空，若为空，则结果集不为空，但是返回数据均为空
                results[k][i] = []
                results[k][i].append(hotels[k][i][0])
                cursor.execute(sql_1, hotels[k][i][0])
                results_1 = cursor.fetchall()
                web_1 = ['去哪儿', hotels[k][i][1], hotels[k][i][2], hotels[k][i][3], 0, hotels[k][i][5],
                         None, hotels[k][i][6]]
                web_2 = ['飞猪', hotels[k][i][1], hotels[k][i][2], hotels[k][i][3], 0, hotels[k][i][5],
                         None, hotels[k][i][6]]
                web_3 = ['途牛', hotels[k][i][1], hotels[k][i][2], hotels[k][i][3], 0, hotels[k][i][5],
                         None, hotels[k][i][6]]
                web_4 = ['携程', hotels[k][i][1], hotels[k][i][2], hotels[k][i][3], 0, hotels[k][i][5],
                         None, hotels[k][i][6]]
                web_5 = ['艺龙', hotels[k][i][1], hotels[k][i][2], hotels[k][i][3], 0, hotels[k][i][5],
                         None, hotels[k][i][6]]
                for row in results_1:
                    if (row[1] == '去哪儿'):
                        # print(row[4])
                        web_1 = ['去哪儿', hotels[k][i][1],row[4],row[5] , row[3], hotels[k][i][5],
                             getLink(city, row[6], checkintime, checkouttime, '去哪儿'), hotels[k][i][6]]
                    if (row[1] == '携程'):
                        web_4 = ['携程', hotels[k][i][1], row[4],row[5] ,row[3], hotels[k][i][5],
                                 getLink(city, row[6], checkintime, checkouttime, '携程'), hotels[k][i][6]]
                    if (row[1] == '飞猪'):
                        web_2 = ['飞猪', hotels[k][i][1],row[4],row[5] , row[3], hotels[k][i][5],
                                 getLink(city, row[6], checkintime, checkouttime, '飞猪'), hotels[k][i][6]]
                    if (row[1] == '途牛'):
                        web_3 = ['途牛', hotels[k][i][1],row[4],row[5] , row[3], hotels[k][i][5],
                                 getLink(city, row[6], checkintime, checkouttime, '途牛'), hotels[k][i][6]]
                    if (row[1] == '艺龙'):
                        web_5 = ['艺龙', hotels[k][i][1],row[4],row[5] ,row[3], hotels[k][i][5],
                                 getLink(city, row[6], checkintime, checkouttime, '艺龙'), hotels[k][i][6]]
                results[k][i].append([web_4,
                                   web_1,
                                   web_2,
                                   web_3,
                                   web_5])
                results[k][i].append(results_1[0][7])
        return results

def python_to_json(results,group):
    #"data":{0":[和没分组一样的格式],"1":[]}
    #如果没有分组，输出如下：
    if(group==0):
        outcome={}
        outcome['type']=1
        temp=[]
        for i in range(len(results)):
            d={}
            d_1={}
            d_2={}
            d_3={}
            d_4={}
            d_5={}
            # print(results[i][0])
            d['name']=results[i][0]
            #携程
            d_1['website']=results[i][1][0][0]
            d_1['distance']=results[i][1][0][1]
            d_1['score']=results[i][1][0][2]
            d_1['comments']=results[i][1][0][3]
            d_1['price']=results[i][1][0][4]
            d_1['type']=results[i][1][0][5]
            d_1['link']=results[i][1][0][6]
            d_1['position']=results[i][1][0][7]
            #去哪儿
            d_2['website']=results[i][1][1][0]
            d_2['distance']=results[i][1][1][1]
            d_2['score']=results[i][1][1][2]
            d_2['comments']=results[i][1][1][3]
            d_2['price']=results[i][1][1][4]
            d_2['type']=results[i][1][1][5]
            d_2['link']=results[i][1][1][6]
            d_2['position']=results[i][1][1][7]
            #飞猪
            d_3['website']=results[i][1][2][0]
            d_3['distance']=results[i][1][2][1]
            d_3['score']=results[i][1][2][2]
            d_3['comments']=results[i][1][2][3]
            d_3['price']=results[i][1][2][4]
            d_3['type']=results[i][1][2][5]
            d_3['link']=results[i][1][2][6]
            d_3['position']=results[i][1][2][7]
            #途牛
            d_4['website']=results[i][1][3][0]
            d_4['distance']=results[i][1][3][1]
            d_4['score']=results[i][1][3][2]
            d_4['comments']=results[i][1][3][3]
            d_4['price']=results[i][1][3][4]
            d_4['type']=results[i][1][3][5]
            d_4['link']=results[i][1][3][6]
            d_4['position']=results[i][1][3][7]
            #艺龙
            d_5['website']=results[i][1][4][0]
            d_5['distance']=results[i][1][4][1]
            d_5['score']=results[i][1][4][2]
            d_5['comments']=results[i][1][4][3]
            d_5['price']=results[i][1][4][4]
            d_5['type']=results[i][1][4][5]
            d_5['link']=results[i][1][4][6]
            d_5['position']=results[i][1][4][7]

            d['web']=[d_1,d_2,d_3,d_4,d_5]
            d['picture']=results[i][2]
            temp.append(d)
            # print(d)
            # if(i==len(results)-1):
            #     outcome = outcome + json.dumps(d) + ']'
            # else:
            #     outcome=outcome+json.dumps(d)+','
        outcome['data']=temp
        # print(outcome)
        # final_data=json.dumps(outcome)
        # print(type(outcome))
        # print(outcome)
        return outcome
    #有分组
    #分两组
    elif(group==2):
        outcome={}
        outcome['type']=0
        temp={}
        temp_1=[]
        for i in range(len(results[0])):
            d={}
            d_1={}
            d_2={}
            d_3={}
            d_4={}
            d_5={}
            # print(results[0][i][0])
            d['name']=results[0][i][0]
            #携程
            d_1['website']=results[0][i][1][0][0]
            d_1['distance']=results[0][i][1][0][1]
            d_1['score']=results[0][i][1][0][2]
            d_1['comments']=results[0][i][1][0][3]
            d_1['price']=results[0][i][1][0][4]
            d_1['type']=results[0][i][1][0][5]
            d_1['link']=results[0][i][1][0][6]
            d_1['position']=results[0][i][1][0][7]
            #去哪儿
            d_2['website']=results[0][i][1][1][0]
            d_2['distance']=results[0][i][1][1][1]
            d_2['score']=results[0][i][1][1][2]
            d_2['comments']=results[0][i][1][1][3]
            d_2['price']=results[0][i][1][1][4]
            d_2['type']=results[0][i][1][1][5]
            d_2['link']=results[0][i][1][1][6]
            d_2['position']=results[0][i][1][1][7]
            #飞猪
            d_3['website']=results[0][i][1][2][0]
            d_3['distance']=results[0][i][1][2][1]
            d_3['score']=results[0][i][1][2][2]
            d_3['comments']=results[0][i][1][2][3]
            d_3['price']=results[0][i][1][2][4]
            d_3['type']=results[0][i][1][2][5]
            d_3['link']=results[0][i][1][2][6]
            d_3['position']=results[0][i][1][2][7]
            #途牛
            d_4['website']=results[0][i][1][3][0]
            d_4['distance']=results[0][i][1][3][1]
            d_4['score']=results[0][i][1][3][2]
            d_4['comments']=results[0][i][1][3][3]
            d_4['price']=results[0][i][1][3][4]
            d_4['type']=results[0][i][1][3][5]
            d_4['link']=results[0][i][1][3][6]
            d_4['position']=results[0][i][1][3][7]
            #艺龙
            d_5['website']=results[0][i][1][4][0]
            d_5['distance']=results[0][i][1][4][1]
            d_5['score']=results[0][i][1][4][2]
            d_5['comments']=results[0][i][1][4][3]
            d_5['price']=results[0][i][1][4][4]
            d_5['type']=results[0][i][1][4][5]
            d_5['link']=results[0][i][1][4][6]
            d_5['position']=results[0][i][1][4][7]

            d['web']=[d_1,d_2,d_3,d_4,d_5]
            d['picture']=results[0][i][2]
            temp_1.append(d)
        temp_2=[]
        for i in range(len(results[1])):
            d={}
            d_1={}
            d_2={}
            d_3={}
            d_4={}
            d_5={}
            # print(results[1][i][0])
            d['name']=results[1][i][0]
            #携程
            d_1['website']=results[1][i][1][0][0]
            d_1['distance']=results[1][i][1][0][1]
            d_1['score']=results[1][i][1][0][2]
            d_1['comments']=results[1][i][1][0][3]
            d_1['price']=results[1][i][1][0][4]
            d_1['type']=results[1][i][1][0][5]
            d_1['link']=results[1][i][1][0][6]
            d_1['position']=results[1][i][1][0][7]
            #去哪儿
            d_2['website']=results[1][i][1][1][0]
            d_2['distance']=results[1][i][1][1][1]
            d_2['score']=results[1][i][1][1][2]
            d_2['comments']=results[1][i][1][1][3]
            d_2['price']=results[1][i][1][1][4]
            d_2['type']=results[1][i][1][1][5]
            d_2['link']=results[1][i][1][1][6]
            d_2['position']=results[1][i][1][1][7]
            #飞猪
            d_3['website']=results[1][i][1][2][0]
            d_3['distance']=results[1][i][1][2][1]
            d_3['score']=results[1][i][1][2][2]
            d_3['comments']=results[1][i][1][2][3]
            d_3['price']=results[1][i][1][2][4]
            d_3['type']=results[1][i][1][2][5]
            d_3['link']=results[1][i][1][2][6]
            d_3['position']=results[1][i][1][2][7]
            #途牛
            d_4['website']=results[1][i][1][3][0]
            d_4['distance']=results[1][i][1][3][1]
            d_4['score']=results[1][i][1][3][2]
            d_4['comments']=results[1][i][1][3][3]
            d_4['price']=results[1][i][1][3][4]
            d_4['type']=results[1][i][1][3][5]
            d_4['link']=results[1][i][1][3][6]
            d_4['position']=results[1][i][1][3][7]
            #艺龙
            d_5['website']=results[1][i][1][4][0]
            d_5['distance']=results[1][i][1][4][1]
            d_5['score']=results[1][i][1][4][2]
            d_5['comments']=results[1][i][1][4][3]
            d_5['price']=results[1][i][1][4][4]
            d_5['type']=results[1][i][1][4][5]
            d_5['link']=results[1][i][1][4][6]
            d_5['position']=results[1][i][1][4][7]

            d['web']=[d_1,d_2,d_3,d_4,d_5]
            d['picture']=results[1][i][2]
            temp_2.append(d)
        temp['0']=temp_1
        temp['1']=temp_2
        outcome['data']=temp
        # final_data=json.dumps(outcome)
        return outcome
    #分三组
    elif(group==3):
        outcome={}
        outcome['type']=0
        temp={}
        temp_1=[]
        for i in range(len(results[0])):
            d={}
            d_1={}
            d_2={}
            d_3={}
            d_4={}
            d_5={}
            # print(results[0][i][0])
            d['name']=results[0][i][0]
            #携程
            d_1['website']=results[0][i][1][0][0]
            d_1['distance']=results[0][i][1][0][1]
            d_1['score']=results[0][i][1][0][2]
            d_1['comments']=results[0][i][1][0][3]
            d_1['price']=results[0][i][1][0][4]
            d_1['type']=results[0][i][1][0][5]
            d_1['link']=results[0][i][1][0][6]
            d_1['position']=results[0][i][1][0][7]
            #去哪儿
            d_2['website']=results[0][i][1][1][0]
            d_2['distance']=results[0][i][1][1][1]
            d_2['score']=results[0][i][1][1][2]
            d_2['comments']=results[0][i][1][1][3]
            d_2['price']=results[0][i][1][1][4]
            d_2['type']=results[0][i][1][1][5]
            d_2['link']=results[0][i][1][1][6]
            d_2['position']=results[0][i][1][1][7]
            #飞猪
            d_3['website']=results[0][i][1][2][0]
            d_3['distance']=results[0][i][1][2][1]
            d_3['score']=results[0][i][1][2][2]
            d_3['comments']=results[0][i][1][2][3]
            d_3['price']=results[0][i][1][2][4]
            d_3['type']=results[0][i][1][2][5]
            d_3['link']=results[0][i][1][2][6]
            d_3['position']=results[0][i][1][2][7]
            #途牛
            d_4['website']=results[0][i][1][3][0]
            d_4['distance']=results[0][i][1][3][1]
            d_4['score']=results[0][i][1][3][2]
            d_4['comments']=results[0][i][1][3][3]
            d_4['price']=results[0][i][1][3][4]
            d_4['type']=results[0][i][1][3][5]
            d_4['link']=results[0][i][1][3][6]
            d_4['position']=results[0][i][1][3][7]
            #艺龙
            d_5['website']=results[0][i][1][4][0]
            d_5['distance']=results[0][i][1][4][1]
            d_5['score']=results[0][i][1][4][2]
            d_5['comments']=results[0][i][1][4][3]
            d_5['price']=results[0][i][1][4][4]
            d_5['type']=results[0][i][1][4][5]
            d_5['link']=results[0][i][1][4][6]
            d_5['position']=results[0][i][1][4][7]

            d['web']=[d_1,d_2,d_3,d_4,d_5]
            d['picture']=results[0][i][2]
            temp_1.append(d)
        temp_2=[]
        for i in range(len(results[1])):
            d={}
            d_1={}
            d_2={}
            d_3={}
            d_4={}
            d_5={}
            # print(results[1][i][0])
            d['name']=results[1][i][0]
            #携程
            d_1['website']=results[1][i][1][0][0]
            d_1['distance']=results[1][i][1][0][1]
            d_1['score']=results[1][i][1][0][2]
            d_1['comments']=results[1][i][1][0][3]
            d_1['price']=results[1][i][1][0][4]
            d_1['type']=results[1][i][1][0][5]
            d_1['link']=results[1][i][1][0][6]
            d_1['position']=results[1][i][1][0][7]
            #去哪儿
            d_2['website']=results[1][i][1][1][0]
            d_2['distance']=results[1][i][1][1][1]
            d_2['score']=results[1][i][1][1][2]
            d_2['comments']=results[1][i][1][1][3]
            d_2['price']=results[1][i][1][1][4]
            d_2['type']=results[1][i][1][1][5]
            d_2['link']=results[1][i][1][1][6]
            d_2['position']=results[1][i][1][1][7]
            #飞猪
            d_3['website']=results[1][i][1][2][0]
            d_3['distance']=results[1][i][1][2][1]
            d_3['score']=results[1][i][1][2][2]
            d_3['comments']=results[1][i][1][2][3]
            d_3['price']=results[1][i][1][2][4]
            d_3['type']=results[1][i][1][2][5]
            d_3['link']=results[1][i][1][2][6]
            d_3['position']=results[1][i][1][2][7]
            #途牛
            d_4['website']=results[1][i][1][3][0]
            d_4['distance']=results[1][i][1][3][1]
            d_4['score']=results[1][i][1][3][2]
            d_4['comments']=results[1][i][1][3][3]
            d_4['price']=results[1][i][1][3][4]
            d_4['type']=results[1][i][1][3][5]
            d_4['link']=results[1][i][1][3][6]
            d_4['position']=results[1][i][1][3][7]
            #艺龙
            d_5['website']=results[1][i][1][4][0]
            d_5['distance']=results[1][i][1][4][1]
            d_5['score']=results[1][i][1][4][2]
            d_5['comments']=results[1][i][1][4][3]
            d_5['price']=results[1][i][1][4][4]
            d_5['type']=results[1][i][1][4][5]
            d_5['link']=results[1][i][1][4][6]
            d_5['position']=results[1][i][1][4][7]

            d['web']=[d_1,d_2,d_3,d_4,d_5]
            d['picture']=results[1][i][2]
            temp_2.append(d)
        temp_3=[]
        for i in range(len(results[2])):
            d={}
            d_1={}
            d_2={}
            d_3={}
            d_4={}
            d_5={}
            # print(results[1][i][0])
            d['name']=results[2][i][0]
            #携程
            d_1['website']=results[2][i][1][0][0]
            d_1['distance']=results[2][i][1][0][1]
            d_1['score']=results[2][i][1][0][2]
            d_1['comments']=results[2][i][1][0][3]
            d_1['price']=results[2][i][1][0][4]
            d_1['type']=results[2][i][1][0][5]
            d_1['link']=results[2][i][1][0][6]
            d_1['position']=results[2][i][1][0][7]
            #去哪儿
            d_2['website']=results[2][i][1][1][0]
            d_2['distance']=results[2][i][1][1][1]
            d_2['score']=results[2][i][1][1][2]
            d_2['comments']=results[2][i][1][1][3]
            d_2['price']=results[2][i][1][1][4]
            d_2['type']=results[2][i][1][1][5]
            d_2['link']=results[2][i][1][1][6]
            d_2['position']=results[2][i][1][1][7]
            #飞猪
            d_3['website']=results[2][i][1][2][0]
            d_3['distance']=results[2][i][1][2][1]
            d_3['score']=results[2][i][1][2][2]
            d_3['comments']=results[2][i][1][2][3]
            d_3['price']=results[2][i][1][2][4]
            d_3['type']=results[2][i][1][2][5]
            d_3['link']=results[2][i][1][2][6]
            d_3['position']=results[2][i][1][2][7]
            #途牛
            d_4['website']=results[2][i][1][3][0]
            d_4['distance']=results[2][i][1][3][1]
            d_4['score']=results[2][i][1][3][2]
            d_4['comments']=results[2][i][1][3][3]
            d_4['price']=results[2][i][1][3][4]
            d_4['type']=results[2][i][1][3][5]
            d_4['link']=results[2][i][1][3][6]
            d_4['position']=results[2][i][1][3][7]
            #艺龙
            d_5['website']=results[2][i][1][4][0]
            d_5['distance']=results[2][i][1][4][1]
            d_5['score']=results[2][i][1][4][2]
            d_5['comments']=results[2][i][1][4][3]
            d_5['price']=results[2][i][1][4][4]
            d_5['type']=results[2][i][1][4][5]
            d_5['link']=results[2][i][1][4][6]
            d_5['position']=results[2][i][1][4][7]

            d['web']=[d_1,d_2,d_3,d_4,d_5]
            d['picture']=results[2][i][2]
            temp_3.append(d)
        temp['0']=temp_1
        temp['1']=temp_2
        temp['2']=temp_3
        outcome['data'] = temp
        # final_data=json.dumps(outcome)
        return outcome
    #分四组
    elif(group==4):
        outcome={}
        outcome['type']=0
        temp={}
        temp_1=[]
        for i in range(len(results[0])):
            d={}
            d_1={}
            d_2={}
            d_3={}
            d_4={}
            d_5={}
            # print(results[0][i][0])
            d['name']=results[0][i][0]
            #携程
            d_1['website']=results[0][i][1][0][0]
            d_1['distance']=results[0][i][1][0][1]
            d_1['score']=results[0][i][1][0][2]
            d_1['comments']=results[0][i][1][0][3]
            d_1['price']=results[0][i][1][0][4]
            d_1['type']=results[0][i][1][0][5]
            d_1['link']=results[0][i][1][0][6]
            d_1['position']=results[0][i][1][0][7]
            #去哪儿
            d_2['website']=results[0][i][1][1][0]
            d_2['distance']=results[0][i][1][1][1]
            d_2['score']=results[0][i][1][1][2]
            d_2['comments']=results[0][i][1][1][3]
            d_2['price']=results[0][i][1][1][4]
            d_2['type']=results[0][i][1][1][5]
            d_2['link']=results[0][i][1][1][6]
            d_2['position']=results[0][i][1][1][7]
            #飞猪
            d_3['website']=results[0][i][1][2][0]
            d_3['distance']=results[0][i][1][2][1]
            d_3['score']=results[0][i][1][2][2]
            d_3['comments']=results[0][i][1][2][3]
            d_3['price']=results[0][i][1][2][4]
            d_3['type']=results[0][i][1][2][5]
            d_3['link']=results[0][i][1][2][6]
            d_3['position']=results[0][i][1][2][7]
            #途牛
            d_4['website']=results[0][i][1][3][0]
            d_4['distance']=results[0][i][1][3][1]
            d_4['score']=results[0][i][1][3][2]
            d_4['comments']=results[0][i][1][3][3]
            d_4['price']=results[0][i][1][3][4]
            d_4['type']=results[0][i][1][3][5]
            d_4['link']=results[0][i][1][3][6]
            d_4['position']=results[0][i][1][3][7]
            #艺龙
            d_5['website']=results[0][i][1][4][0]
            d_5['distance']=results[0][i][1][4][1]
            d_5['score']=results[0][i][1][4][2]
            d_5['comments']=results[0][i][1][4][3]
            d_5['price']=results[0][i][1][4][4]
            d_5['type']=results[0][i][1][4][5]
            d_5['link']=results[0][i][1][4][6]
            d_5['position']=results[0][i][1][4][7]

            d['web']=[d_1,d_2,d_3,d_4,d_5]
            d['picture']=results[0][i][2]
            temp_1.append(d)
        temp_2=[]
        for i in range(len(results[1])):
            d={}
            d_1={}
            d_2={}
            d_3={}
            d_4={}
            d_5={}
            # print(results[1][i][0])
            d['name']=results[1][i][0]
            #携程
            d_1['website']=results[1][i][1][0][0]
            d_1['distance']=results[1][i][1][0][1]
            d_1['score']=results[1][i][1][0][2]
            d_1['comments']=results[1][i][1][0][3]
            d_1['price']=results[1][i][1][0][4]
            d_1['type']=results[1][i][1][0][5]
            d_1['link']=results[1][i][1][0][6]
            d_1['position']=results[1][i][1][0][7]
            #去哪儿
            d_2['website']=results[1][i][1][1][0]
            d_2['distance']=results[1][i][1][1][1]
            d_2['score']=results[1][i][1][1][2]
            d_2['comments']=results[1][i][1][1][3]
            d_2['price']=results[1][i][1][1][4]
            d_2['type']=results[1][i][1][1][5]
            d_2['link']=results[1][i][1][1][6]
            d_2['position']=results[1][i][1][1][7]
            #飞猪
            d_3['website']=results[1][i][1][2][0]
            d_3['distance']=results[1][i][1][2][1]
            d_3['score']=results[1][i][1][2][2]
            d_3['comments']=results[1][i][1][2][3]
            d_3['price']=results[1][i][1][2][4]
            d_3['type']=results[1][i][1][2][5]
            d_3['link']=results[1][i][1][2][6]
            d_3['position']=results[1][i][1][2][7]
            #途牛
            d_4['website']=results[1][i][1][3][0]
            d_4['distance']=results[1][i][1][3][1]
            d_4['score']=results[1][i][1][3][2]
            d_4['comments']=results[1][i][1][3][3]
            d_4['price']=results[1][i][1][3][4]
            d_4['type']=results[1][i][1][3][5]
            d_4['link']=results[1][i][1][3][6]
            d_4['position']=results[1][i][1][3][7]
            #艺龙
            d_5['website']=results[1][i][1][4][0]
            d_5['distance']=results[1][i][1][4][1]
            d_5['score']=results[1][i][1][4][2]
            d_5['comments']=results[1][i][1][4][3]
            d_5['price']=results[1][i][1][4][4]
            d_5['type']=results[1][i][1][4][5]
            d_5['link']=results[1][i][1][4][6]
            d_5['position']=results[1][i][1][4][7]

            d['web']=[d_1,d_2,d_3,d_4,d_5]
            d['picture']=results[1][i][2]
            temp_2.append(d)
        temp_3=[]
        for i in range(len(results[2])):
            d={}
            d_1={}
            d_2={}
            d_3={}
            d_4={}
            d_5={}
            # print(results[1][i][0])
            d['name']=results[2][i][0]
            #携程
            d_1['website']=results[2][i][1][0][0]
            d_1['distance']=results[2][i][1][0][1]
            d_1['score']=results[2][i][1][0][2]
            d_1['comments']=results[2][i][1][0][3]
            d_1['price']=results[2][i][1][0][4]
            d_1['type']=results[2][i][1][0][5]
            d_1['link']=results[2][i][1][0][6]
            d_1['position']=results[2][i][1][0][7]
            #去哪儿
            d_2['website']=results[2][i][1][1][0]
            d_2['distance']=results[2][i][1][1][1]
            d_2['score']=results[2][i][1][1][2]
            d_2['comments']=results[2][i][1][1][3]
            d_2['price']=results[2][i][1][1][4]
            d_2['type']=results[2][i][1][1][5]
            d_2['link']=results[2][i][1][1][6]
            d_2['position']=results[2][i][1][1][7]
            #飞猪
            d_3['website']=results[2][i][1][2][0]
            d_3['distance']=results[2][i][1][2][1]
            d_3['score']=results[2][i][1][2][2]
            d_3['comments']=results[2][i][1][2][3]
            d_3['price']=results[2][i][1][2][4]
            d_3['type']=results[2][i][1][2][5]
            d_3['link']=results[2][i][1][2][6]
            d_3['position']=results[2][i][1][2][7]
            #途牛
            d_4['website']=results[2][i][1][3][0]
            d_4['distance']=results[2][i][1][3][1]
            d_4['score']=results[2][i][1][3][2]
            d_4['comments']=results[2][i][1][3][3]
            d_4['price']=results[2][i][1][3][4]
            d_4['type']=results[2][i][1][3][5]
            d_4['link']=results[2][i][1][3][6]
            d_4['position']=results[2][i][1][3][7]
            #艺龙
            d_5['website']=results[2][i][1][4][0]
            d_5['distance']=results[2][i][1][4][1]
            d_5['score']=results[2][i][1][4][2]
            d_5['comments']=results[2][i][1][4][3]
            d_5['price']=results[2][i][1][4][4]
            d_5['type']=results[2][i][1][4][5]
            d_5['link']=results[2][i][1][4][6]
            d_5['position']=results[2][i][1][4][7]

            d['web']=[d_1,d_2,d_3,d_4,d_5]
            d['picture']=results[2][i][2]
            temp_3.append(d)
        temp_4=[]
        for i in range(len(results[3])):
            d={}
            d_1={}
            d_2={}
            d_3={}
            d_4={}
            d_5={}
            # print(results[1][i][0])
            d['name']=results[3][i][0]
            #携程
            d_1['website']=results[3][i][1][0][0]
            d_1['distance']=results[3][i][1][0][1]
            d_1['score']=results[3][i][1][0][2]
            d_1['comments']=results[3][i][1][0][3]
            d_1['price']=results[3][i][1][0][4]
            d_1['type']=results[3][i][1][0][5]
            d_1['link']=results[3][i][1][0][6]
            d_1['position']=results[3][i][1][0][7]
            #去哪儿
            d_2['website']=results[3][i][1][1][0]
            d_2['distance']=results[3][i][1][1][1]
            d_2['score']=results[3][i][1][1][2]
            d_2['comments']=results[3][i][1][1][3]
            d_2['price']=results[3][i][1][1][4]
            d_2['type']=results[3][i][1][1][5]
            d_2['link']=results[3][i][1][1][6]
            d_2['position']=results[3][i][1][1][7]
            #飞猪
            d_3['website']=results[3][i][1][2][0]
            d_3['distance']=results[3][i][1][2][1]
            d_3['score']=results[3][i][1][2][2]
            d_3['comments']=results[3][i][1][2][3]
            d_3['price']=results[3][i][1][2][4]
            d_3['type']=results[3][i][1][2][5]
            d_3['link']=results[3][i][1][2][6]
            d_3['position']=results[3][i][1][2][7]
            #途牛
            d_4['website']=results[3][i][1][3][0]
            d_4['distance']=results[3][i][1][3][1]
            d_4['score']=results[3][i][1][3][2]
            d_4['comments']=results[3][i][1][3][3]
            d_4['price']=results[3][i][1][3][4]
            d_4['type']=results[3][i][1][3][5]
            d_4['link']=results[3][i][1][3][6]
            d_4['position']=results[3][i][1][3][7]
            #艺龙
            d_5['website']=results[3][i][1][4][0]
            d_5['distance']=results[3][i][1][4][1]
            d_5['score']=results[3][i][1][4][2]
            d_5['comments']=results[3][i][1][4][3]
            d_5['price']=results[3][i][1][4][4]
            d_5['type']=results[3][i][1][4][5]
            d_5['link']=results[3][i][1][4][6]
            d_5['position']=results[3][i][1][4][7]

            d['web']=[d_1,d_2,d_3,d_4,d_5]
            d['picture']=results[3][i][2]
            temp_4.append(d)
        temp['0']=temp_1
        temp['1']=temp_2
        temp['2']=temp_3
        temp['3']=temp_4
        outcome['data']=temp
        # final_data=json.dumps(outcome)
        return outcome

# citypinyin=getCityName('上海')
# print(getLink('上海',50997,'2021-06-07','2021-06-08','途牛'))
    #建立数据库连接
# db = pymysql.connect(
#         host='8.140.178.29',
#         port=3306,
#         user='cxsx',
#         passwd='cxsx123',
#         db='cxsx',
#         charset='utf8'
# )

# 使用cursor()方法创建一个游标对象cursor
# cursor = db.cursor()
# sql1="select * from hotel_web where Web_name='去哪儿'"
#
# test_hotels=[[0 for i in range(7)] for j in range(20)]
# try:
#     # 执行SQL语句
#     cursor.execute(sql1)
#     # 获取所有记录列表
#     #先查询出去哪儿网站中的所有酒店，然后根据酒店名，找到该酒店在飞猪和途牛对应的信息
#     results_1 = cursor.fetchall()
#     i = 0
#     for row in results_1:
#         #查询同一酒店在飞猪中的信息
#         sql2 = "select * from hotel_web where Web_name='飞猪' and Hotel_name=%s"
#         #查询同一酒店在途牛中的信息
#         sql3 = "select * from hotel_web where Web_name='途牛' and Hotel_name=%s"
#         cursor.execute(sql2,row[0])
#         results_2=cursor.fetchone()
#         if(results_2==None):
#             continue
#         cursor.execute(sql3,row[0])
#         results_3=cursor.fetchone()
#         if(results_3==None):
#             continue
#         test_hotels[i][3]=['飞猪',0,row[4],row[5],results_2[3],row[2],getLink('上海',results_2[6],'2021-06-28','2021-06-29','飞猪'),'']
#         cursor.execute(sql3,row[0])
#         test_hotels[i][0]=row[0]#酒店名称
#         test_hotels[i][4]=['途牛',0,row[4],row[5],results_3[3],row[2],getLink('上海',results_3[6],'2021-06-28','2021-06-29','途牛'),'']
#         test_hotels[i][1]=['携程',0,row[4],row[5],row[3],row[2],getLink('上海',row[6],'2021-06-28','2021-06-29','去哪儿'),'']
#         test_hotels[i][2]=['去哪儿',0,row[4],row[5],row[3],row[2],getLink('上海',row[6],'2021-06-28','2021-06-29','去哪儿'),'']
#         test_hotels[i][5]=['爱彼迎',0,row[4],row[5],row[3],row[2],getLink('上海',row[6],'2021-06-28','2021-06-29','去哪儿'),'']
#         test_hotels[i][6]=row[7]
#         i=i+1
#         if(i==20):
#             break
#     for i in range(20):
#         print("{name:'"+test_hotels[i][0]+"',webs:[",end='')
#         print("{website:'携程',distance:0,score:",end='')
#         print(test_hotels[i][1][2],end='')
#         print(",comments:",end='')
#         print(test_hotels[i][1][3],end='')
#         print(",price:",end='')
#         print(test_hotels[i][1][4],end='')
#         print(",type:'"+test_hotels[i][1][5]+"',link:'"+test_hotels[i][1][6]+"',position:''},",end='')
#         print("{website:'去哪儿',distance:0,score:",end='')
#         print(test_hotels[i][2][2],end='')
#         print(",comments:",end='')
#         print(test_hotels[i][2][3],end='')
#         print(",price:",end='')
#         print(test_hotels[i][2][4],end='')
#         print(",type:'"+test_hotels[i][2][5]+"',link:'"+test_hotels[i][2][6]+"',position:''},",end='')
#         print("{website:'飞猪',distance:0,score:",end='')
#         print(test_hotels[i][3][2],end='')
#         print(",comments:",end='')
#         print(test_hotels[i][3][3],end='')
#         print(",price:",end='')
#         print(test_hotels[i][3][4],end='')
#         print(",type:'"+test_hotels[i][3][5]+"',link:'"+test_hotels[i][3][6]+"',position:''},",end='')
#         print("{website:'途牛',distance:0,score:",end='')
#         print(test_hotels[i][4][2],end='')
#         print(",comments:",end='')
#         print(test_hotels[i][4][3],end='')
#         print(",price:",end='')
#         print(test_hotels[i][4][4],end='')
#         print(",type:'"+test_hotels[i][4][5]+"',link:'"+test_hotels[i][4][6]+"',position:''},",end='')
#         print("{website:'爱彼迎',distance:0,score:",end='')
#         print(test_hotels[i][1][2],end='')
#         print(",comments:",end='')
#         print(test_hotels[i][1][3],end='')
#         print(",price:",end='')
#         print(test_hotels[i][1][4],end='')
#         print(",type:'"+test_hotels[i][1][5]+"',link:'"+test_hotels[i][1][6]+"',position:''}],",end='')
#         print("picture:'"+test_hotels[i][6]+"'},")
#         # print(test_hotels[i])
#
# except:
#     print("Error: unable to fetch data")

# 查询景点到酒店距离，并将它存入数据库
db = pymysql.connect(
        host='8.140.178.29',
        port=3306,
        user='cxsx',
        passwd='cxsx123',
        db='cxsx',
        charset='utf8'
)

# 使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()
#济南
# sql="select Hotel_name from hotel_jinan"#查询所有酒店
# cursor.execute(sql)
# hotels=cursor.fetchall()
# positions=[]#查询所有地点
# f = open("positions.txt",encoding='UTF-8')  # 返回一个文件对象
# line = f.readline()  # 调用文件的 readline()方法
# while line:
#     positions.append(line)
#     line = f.readline()
# f.close()
# #计算距离
# for i in range(len(positions)):
#     #计算每个地点到各个酒店的距离
#     k=0
#     try:
#         for j in range(len(hotels)):
#             print(positions[i])
#             print(hotels[j])
#             try:
#                 # starturl=getapiurl(str(positions[i]))
#                 # startlat,startlng=getPosition(starturl)
#                 # endurl=getapiurl(str(hotels[j]))
#                 # endlat, endlng = getPosition(endurl)
#                 # dist=getdistance(startlat, startlng,endlat, endlng)
#                 # dist=gaode(positions[i],hotels[j])
#                 dist=distance(positions[i],hotels[j])
#                 k=k+1
#                 print(k)
#             except:
#                 k=k+1
#                 print(k)
#                 continue
#             print(dist)
#             if(dist==None):
#                 continue
#             sql4="insert into distance (position,hotel,distance,score, comments,price,type) values (%s,%s,%s,0,0,0,'')"
#             cursor.execute(sql4,(positions[i],hotels[j],dist))
#             db.commit()  # 提交到数据库执行
#     except:
#         time.sleep(3)
#         continue
#查询出所有酒店，酒店在各大网站上均存在
# sql="select * from hotel_web where Web_name='去哪儿'"
# hotels=[]
# try:
#     sql_0="select * from distance where comments=0"
#     print('successful_1')
#     cursor.execute(sql_0)
#     results_1=cursor.fetchall()
#     print(len(results_1))
#     i=0
#     for row in results_1:
#         print(i)
#         print(row[1])
#         sql_1="select * from hotel_web where Web_name='艺龙' and Hotel_name=%s "
#         cursor.execute(sql_1,row[1])
#         print('successful_2')
#         results_2=cursor.fetchone()
#         values=(results_2[4],results_2[5],results_2[3],results_2[2],row[1])
#         print(values)
#         sql_2="update distance set score=%s,comments=%s,price=%s,type=%s where hotel=%s and comments=0"
#         cursor.execute(sql_2,values)
#         print('successful_3')
#         db.commit()
#         i=i+1
# except:
#     print("Error: unable to fetch data")

#算出景点与酒店的距离
#     sql="select * from same_hotel"
#     cursor.execute(sql)
#     results=cursor.fetchall()
#     # i=0
#     for row in results:
#         # #查询同一酒店在飞猪中的信息
#         # sql2 = "select * from hotel_web where Web_name='飞猪' and Hotel_name=%s"
#         # #查询同一酒店在途牛中的信息
#         # sql3 = "select * from hotel_web where Web_name='途牛' and Hotel_name=%s"
#         # # sql4 = "select * from hotel_web where Web_name='途牛' and Hotel_name=%s"
#         # # sql5 = "select * from hotel_web where Web_name='途牛' and Hotel_name=%s"
#         #
#         # cursor.execute(sql2,row[0])
#         # results_2=cursor.fetchone()
#         # if(results_2==None):
#         #     continue
#         # cursor.execute(sql3, row[0])
#         # results_3=cursor.fetchone()
#         # if(results_3==None):
#         #     continue
#         # print("succeed")
#         #
#         # sql5="insert into same_hotel(same_hotel_name) values (%s)"
#         # cursor.execute(sql5,row[0])
#         # db.commit()  # 提交到数据库执行
#         # print(row[0])
#         hotels.append(row[0])
#         # i=i+1
#         # if(i==20):
#         #     break
#
# except:
#     print("Error: unable to fetch data")
#
# positions=[]
# f = open("positions.txt",encoding='UTF-8')  # 返回一个文件对象
# line = f.readline()  # 调用文件的 readline()方法
# while line:
#     positions.append(line)
#     line = f.readline()
# f.close()
# for i in range(len(positions)):
#     #计算每个地点到各个酒店的距离
#     k=0
#     try:
#         for j in range(len(hotels)):
#             print(positions[i])
#             print(hotels[j])
#             try:
#                 starturl=getapiurl(str(positions[i]))
#                 startlat,startlng=getPosition(starturl)
#                 endurl=getapiurl(str(hotels[j]))
#                 endlat, endlng = getPosition(endurl)
#                 dist=getdistance(startlat, startlng,endlat, endlng)
#                 # dist=gaode(positions[i],hotels[j])
#                 k=k+1
#                 print(k)
#             except:
#                 k=k+1
#                 print(k)
#                 continue
#             #为了防止百度API不工作，所以每执行100次睡眠一段时间
#             if(k==100):
#                 time.sleep(1)
#             print(dist)
#             if(dist==None):
#                 continue
#             sql4="insert into distance (position,hotel,distance,score, comments,price,type) values (%s,%s,%s,0,0,0,'')"
#             cursor.execute(sql4,(positions[i],hotels[j],dist))
#             db.commit()  # 提交到数据库执行
#     except:
#         time.sleep(1)
#         continue

# get_lng_lat('上海城隍庙 上海市黄浦区方浜中路249号')

