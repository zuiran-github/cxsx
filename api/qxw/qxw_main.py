from .basicSort import sort_distance,sort_points,sort_comment,sort_price_descend,sort_price_ascend
from .recommend import basic_recommend,multiple_locations,multiple_locations_days
import requests
from .dataProcessing import distance,get_weights,output,python_to_json,get_distanceFromDB,get_distanceFromDB_1,database_connect
import json
'''
用户输入搜索信息后，默认出来的是综合排序后的结果，即按照综合评分的结果
事实上，我只需要输出一个带有酒店名称的列表就可，因为其他基础信息可以通过查询数据库得到（类型，评分，评论数，价格）
输出酒店列表之后，查询数据库得到一个具体的列表，页面一次显示十家酒店，爬虫爬取这十家酒店的实时价格，点击下一页再爬取下十家

情况一：若用户只输入了一个地点，那么根据这个地点先搜索出全城的酒店信息（按照计划，全部酒店的基本信息被预先存放到了数据库里）
计算出这个地点到所有酒店的距离，有了距离，评分，评论数和价格信息之后，根据已经设计好的模型得出酒店推荐顺序
综合评分模型有两种，一种是对距离，评分，评论数和价格这四个特征赋以固定的权重，得到一个综合评分，根据综合评分降序推荐
另一种是逻辑回归模型，根据用户的点击情况，对用户的点击行为进行拟合，进而根据那四个特征预测用户的点击行为，根据概率降序推荐

情况二：若用户输入了不止一个地点，并且这几个点相隔较近，那么先对每一个地点做出第一种的情况的推荐，然后得到若干组的推荐结果，
对这些推荐列表逐个比较，并且15（主观设定，可以随时更改，考虑是否有更好的更新方法，比如考虑用户的点击习惯？）名以后的酒店不予比较，
得到一个新的列表，列表里是这几个酒店推荐列表的全集，信息包括酒店的基本参数和重叠度，重叠度为出现在这几个推荐列表的次数，
根据重叠度大小优先推荐，否则根据综合评分降序推荐。

情况三：若用户输入了不止一个地点，且住的时间超过一晚，并且至少有两个地点相隔较远（判断标准：15km，主观设定，可以随时更改，
考虑是否有更好的更新方法？），那么先将这些地点分组，对每一组地点按照第二种情况进行推荐
'''
"""
    #我的输出应该是一个包含酒店名称的列表，只要有了酒店名称，其他可以通过数据库查询到其他信息，我的工作重点是酒店顺序
    #为了减少调用百度API的次数，返回列表还应该有距离
    #但是在多地点推荐中，距离应该具体到某个地点，最优形式是显示这个地点到所有地点的距离，
    #考虑到页面实际显示情况，显示所有距离不符合实际情况，所以我考虑显示最近的地点的距离，这样我的结果中应该有地点
    #因为有这么多复杂的输出情况，所以最后用统一的方法输出数据
    
    #前端最后获得的数据由我输出，输出的形式为：
    #[
    # {name :'美高智选酒店(济南万象城店)',
    # webs:
    #  [{website:'携程',kind:1, score:'4.7', comments:'980', price:'364', type:'舒适型', link:''},
    #  {website:'去哪儿',kind:1, score:'4.7', comments:'980', price:'364', type:'舒适型', link:''},
    #  {website:'飞猪',kind:1, score:'4.7', comments:'980', price:'364', type:'舒适型', link:''},
    #  {website:'途牛', kind:1,score:'4.7', comments:'980', price:'364', type:'舒适型', link:''},
    #  {website:'爱彼迎', kind:1,score:'4.7', comments:'980', price:'364', type:'舒适型', link:''}]},{...}]
    #目前考虑单独编写一个方法传出数据
    #这个方法传出的数据为前端可用的数据
    #无论是综合排序还是其他排序方法，最后传出数据的时候，都应该调用这个方法
    #由于用户还可以通过筛选酒店的类型，所以再编写一个筛选酒店类型的方法，该方法为酒店排序方法的前置方法，将酒店筛选过后再传出
"""
#默认调用方法
def qxw_jiudian(city,places,checkin_time,checkout_time,type):
    # try:
        #逻辑回归模型参数经过迭代计算，参数权重大小已经存放在数据库中
        # weights=get_weights()
        weights=[0.5,0.3,0.15,0.15]
        cursor = database_connect()
        #去的地方只有一个，使用基础推荐算法，并传出json数据
        if(len(places)==1):
            place=places[0]
            #返回结果形式为：[酒店名称，距离，评分，评论，价格，类型，地点，综合评分]
            # return basic_recommend(city,places,checkin_time,checkout_time,weights)
            # print(type(python_to_json(output(basic_recommend(city,place,checkin_time,checkout_time,weights,type),
            #                 0,city,checkin_time,checkout_time),0)))
            # dict = {}
            dict = python_to_json(output(basic_recommend(city,place,checkin_time,checkout_time,weights,type,cursor),
                           0,city,checkin_time,checkout_time,cursor),0)
            # dict = json.dumps(dict)
            # print(type(dict))
            print(dict)
            return dict#python_to_json(output(basic_recommend(city,place,checkin_time,checkout_time,weights,type),
                           # 0,city,checkin_time,checkout_time),0)

        #否则采用多地点推荐法，并传出json形式数据
        else:
            # 返回形式为：[酒店名称，距离，评分，评论，价格，类型，地点，综合评分]
            # return multiple_locations_days(city,places,checkin_time,checkout_time,weights)
            temp=multiple_locations_days(city,places,checkin_time,checkout_time,weights,type,cursor)
            group=0
            if(len(temp)<5):
                group=len(temp)
            print(output(temp,group,city,checkin_time,checkout_time,cursor),group)
            return python_to_json(output(temp,group,city,checkin_time,checkout_time,cursor),group)
    # except Exception as e:
    #     print(e)
    #     error_result={}
    #     error_result['type']=2
    #     error_result['data']=[]
    #     return error_result

#距离升序调用方法
#该方法只适用于景点数为1的情况
def qxw_distance_output(city,places,checkin_time,checkout_time,type):
    place=places[0]
    cursor = database_connect()
    #测试
    # city='上海'
    # places='上海城隍庙 上海市黄浦区方浜中路249号'
    # checkin_time='2021-06-21'
    # checkout_time='2021-06-22'
    # type='全部'
    #先得到所有酒店
    #先从距离表中获取该地点到所有酒店的距离
    #形式为[酒店名称，距离，评分，评论数，价格，类型,地点]
    try:
        all_hotels=get_distanceFromDB_1(place,type,cursor)
        hotels=sort_distance(all_hotels)
        results=output(hotels,0,city,checkin_time,checkout_time,cursor)
        # print(python_to_json(results,0))
        return python_to_json(results,0)
    except Exception as e:
        print(e)
        error_result={}
        error_result['type']=2
        error_result['data']=[]
        return error_result

#评分降序调用方法
#该方法只适用于景点数为1的情况
def qxw_score_output(city,places,checkin_time,checkout_time,type):
    place=places[0]
    cursor = database_connect()
    #先得到所有酒店
    #先从距离表中获取该地点到所有酒店的距离
    #形式为[酒店名称，距离，评分，评论数，价格，类型，地点]
    try:
        all_hotels=get_distanceFromDB_1(place,type,cursor)
        hotels=sort_points(all_hotels)
        results=output(hotels,0,city,checkin_time,checkout_time,cursor)
        return python_to_json(results,0)
    except Exception as e:
        print(e)
        error_result={}
        error_result['type']=2
        error_result['data']=[]
        return error_result

#评论数降序调用方法
#该方法只适用于景点数为1的情况
def qxw_commends_output(city,places,checkin_time,checkout_time,type):
    place=places[0]
    cursor = database_connect()
    #先得到所有酒店
    #先从距离表中获取该地点到所有酒店的距离
    #形式为[酒店名称，距离，评分，评论数，价格，类型，地点]
    try:
        all_hotels=get_distanceFromDB_1(place,type,cursor)
        hotels=sort_comment(all_hotels)
        results=output(hotels,0,city,checkin_time,checkout_time,cursor)
        return python_to_json(results,0)
    except Exception as e:
        print(e)
        error_result={}
        error_result['type']=2
        error_result['data']=[]
        return error_result

#价格降序调用方法
#该方法只适用于景点数为1的情况
def qxw_price_descend_output(city,places,checkin_time,checkout_time,type):
    place=places[0]
    cursor = database_connect()
    #先得到所有酒店
    #先从距离表中获取该地点到所有酒店的距离
    #形式为[酒店名称，距离，评分，评论数，价格，类型，地点]
    try:
        all_hotels=get_distanceFromDB_1(place,type,cursor)
        hotels=sort_price_descend(all_hotels)
        results=output(hotels,0,city,checkin_time,checkout_time,cursor)
        return python_to_json(results,0)
    except Exception as e:
        print(e)
        error_result={}
        error_result['type']=2
        error_result['data']=[]
        return error_result

#评分升序调用方法
#该方法只适用于景点数为1的情况
def qxw_price_ascend_output(city,places,checkin_time,checkout_time,type):
    place=places[0]
    cursor = database_connect()
    #先得到所有酒店
    #先从距离表中获取该地点到所有酒店的距离
    #形式为[酒店名称，距离，评分，评论数，价格，类型，地点]
    try:
        all_hotels=get_distanceFromDB_1(place,type,cursor)
        # print(all_hotels)
        hotels=sort_price_ascend(all_hotels)
        results=output(hotels,0,city,checkin_time,checkout_time,cursor)
        return python_to_json(results,0)
    except Exception as e:
        print(e)
        error_result={}
        error_result['type']=2
        error_result['data']=[]
        return error_result

#测试
# city='上海'
# places=['上海城隍庙 上海市黄浦区方浜中路249号']
# checkin_time='2021-06-21'
# checkout_time='2021-06-22'
# type='全部'