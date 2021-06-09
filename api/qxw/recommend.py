# 创新项目实训
# 比价&酒店推荐系统
# 住宿查询

# 用户选定住宿时间（入住时间和离开时间），入住人数（具体人数），酒店的星级或者民宿，
# 选定要去的景点或者商圈，然后根据这些信息推荐酒店，默认按照综合评分排序，
# 用户也可以按照酒店到景点的距离远近、酒店的评分高低、点评数多少、价格高低来对这些酒店进行筛选，
# 而综合评分是根据这些特征对酒店的综合评价。
# 推荐酒店时会比较多家酒店订购网站上的价格，显示最低价格，
# 点击进入详情页面，可以查看到各大酒店订购网站的具体价格，
# 用户可以在该页面直接进入选中的酒店订购网站进行预订。
import copy
import numpy as np
from .basicSort import sort_comprehensive_assess,sort_comment,sort_points,sort_distance,sort_price_ascend,sort_price_descend
import math
from .dataProcessing import distance,get_weights,get_distanceFromDB,get_distanceFromDB_1,database_connect
from .LR import logistic_regression,LR

"""
    先获取全部酒店的信息（从数据库中获取）:[酒店名称，类型，价格，评分，评论数]
    数据库中有酒店名称，评分（各大网站评分的平均数），评论数（各大网站评论数的平均数），
    价格（每个网站过去十分钟价格的平均数，注意：数据库中应该存放了五个网站的价格：携程，去哪儿，途牛，飞猪，爱彼迎，
    但是计算综合评分只需要使用一个价格）
"""

#要去的地点只有一个，综合排序
def basic_recommend(city,place,checkin_time,checkout_time,weights,type,cursor):
    # cursor=database_connect()
    #先从距离表中获取该地点到所有酒店的距离
    #形式为[酒店名称，距离，评分，评论数，价格，类型，地点]
    hotels=get_distanceFromDB_1(place,type,cursor)

    #如何判断是采用初始综合评价方法，还是逻辑回归模型
    #可以手动设定
    if_first=True
    if(if_first):
        #初始综合排序
        weight_1 = 0.5
        weight_2 = 0.3
        weight_3 = 0.05
        weight_4 = 0.15
        #输出形式为[酒店名称，距离，评分，评论，价格，类型，地点，综合评分]
        return sort_comprehensive_assess(hotels,weight_1,weight_2,weight_3,weight_4)
    else:
        #逻辑回归
        # 输出矩阵形式：[酒店名称，距离，评分，评论，价格，类型，地点，综合评分]
        #此处排名为0
        return logistic_regression(hotels,weights)


#要去的地点多于一个，但是酒店入住日期只有一天
#注意，输出结果中的距离应该具体到该酒店到那个地点的距离
def multiple_locations(city,place,checkin_time,checkout_time,weights,type,cursor):
    cursor=database_connect()
    #可以设定输出酒店数量
    output_number=100
    print(place)
    #先获取全部酒店的信息（从数据库中获取）:[酒店名称，类型，价格，评分，评论数]
    # all_hotels=get_all_hotels(city)
    #根据每一个地点进行推荐，得到一个推荐顺序
    hotels=[0 for i in range(len(place))]
    for i in range(len(place)):
        # # 计算出每家酒店到这个地点的距离
        # for j in range(len(all_hotels)):
        #     all_hotels[j].append(distance(all_hotels[i][0], place[i]))
        #     all_hotels[j].append(place[i])
        # # 此处的得到的矩阵形式为[酒店名称，类型，价格，评分，评论数，距离，地点]

        # 先从距离表中获取该地点到所有酒店的距离
        # 形式为[酒店名称，距离，评分，评论数，价格，类型]
        # print(place[i])
        all_hotels = get_distanceFromDB(place[i],type,cursor)
        # print('succcessful')
        # print(all_hotels)
        # 处理矩阵，使其成为我想要的形式[名称，距离，评分，评论数，价格，类型，地点]
        for j in range(len(all_hotels)):
            all_hotels[j].append(place[i])
        # print(all_hotels)
        #对这些酒店按照综合评分法进行排序
        #后期应该用逻辑回归模型
        #此处暂定为人工设定
        if_first=True
        if(if_first):
            weight_1=0.5
            weight_2=0.3
            weight_3=0.05
            weight_4=0.15
            #hotels[i]大小为8，形式为[酒店名称，距离，评分，评论，价格，类型，地点，综合评分]，
            #按照综合评分降序排列
            hotels[i]=sort_comprehensive_assess(all_hotels,weight_1,weight_2,weight_3,weight_4)
        else:
            # 输出矩阵形式：[酒店名称，距离，评分，评论，价格，类型，地点，综合评分]
            hotels[i]=logistic_regression(all_hotels,weights)
    #获取这些酒店前15名的全集，共9列，形式为[酒店名称，距离，评分，评论，价格，类型，地点，综合评分,重叠度]
    overlap_hotels=[]
    for i in range(15):
        overlap_hotels.append(hotels[0][i])
        #设置初始重叠度为0
        overlap_hotels[i].append(0)
    for i in range(len(hotels)-1):
        for j in range(15):
            exist=False
            #先判断该元素是否已经存在
            for k in range(len(overlap_hotels)):
                if(hotels[i+1][j][0]==overlap_hotels[k][0]):
                    if(hotels[i+1][j][1]<overlap_hotels[k][1]):
                        overlap_hotels[k][1]=hotels[i+1][j][1]
                        overlap_hotels[k][6]=hotels[i+1][j][6]
                    #若已经存在，重叠度+1，用距离更小的一个替换
                    # 退出循环
                    overlap_hotels[k][8]=overlap_hotels[k][8]+1
                    break
                #若不存在，则k值等于数组长度-1
                if(k==(len(overlap_hotels))-1):
                    exist=True
            #如果该元素不存在，那么将这条酒店信息加入全集数组，并设施初始重叠度为0
            if(exist):
                overlap_hotels.append(hotels[i+1][j])
                overlap_hotels[len(overlap_hotels)-1].append(0)
    #对全集按照重叠度降序排列
    for i in range(len(overlap_hotels)-1):
        for j in range(len(overlap_hotels)-1):
            temp_2=overlap_hotels[j]
            if(overlap_hotels[j][8]<overlap_hotels[j+1][8]):
                overlap_hotels[j]=overlap_hotels[j+1]
                overlap_hotels[j+1]=temp_2
    #最终推荐列表，根据重叠度大小优先推荐，否则根据综合评分降序交替推荐。
    #先得到所有重叠度不为0的酒店，加入结果矩阵
    result=[]
    temp_3=0
    for i in range(len(overlap_hotels)):
        #若重叠度不为0，那么优先加入结果矩阵，否则终止循环，并得到重叠度不为0的酒店数
        if(overlap_hotels[i][8]!=0):
            result.append(overlap_hotels[i])
            temp_3=temp_3+1
        else:
            break
    #对剩下的重叠度为0的数据进行处理，按照综合评分降序交替推荐
    temp_4=[]
    for temp_3 in range(len(overlap_hotels)):
        temp_4.append(overlap_hotels[temp_3])

    for i in range(len(temp_4)-1):
        for j in range(len(temp_4)-1):
            temp_5=temp_4[j]
            if(temp_4[j][7]<temp_4[j+1][7]):
                temp_4[j]=temp_4[j+1]
                temp_4[j+1]=temp_5

    #将排序后的结果加入到结果集中
    for i in range(len(temp_4)):
        result.append(temp_4[i])

    #再将15名以后的酒店信息交替加入结果集
    #由于我们不需要这么多数据，所以我们可以设定只获取前100个酒店
    for i in range(output_number):
        for j in range(len(place)):
            # print(hotels[j][i+15])
            result.append(hotels[j][i+15])

    #输出形式为：[酒店名称，距离，评分，评论，价格，类型，地点，综合评分,重叠度]
    #考虑输出一致性，删除结果集中的重叠度，使输出形式为[酒店名称，距离，评分，评论，价格，类型，地点，综合评分]
    outcome=[0 for i in range(len(result))]
    for i in range(len(result)):
        outcome[i]=[result[i][0],result[i][1],result[i][2],result[i][3],result[i][4],
                    result[i][5],result[i][6],result[i][7]]

    return outcome

#要去的地点多于一个，酒店入住日期多于一天
#这个时候可以同时推荐多家酒店
def multiple_locations_days(city,place,checkin_time,checkout_time,weights,type,cursor):
    #计算出入住总晚数
    nights=night(checkin_time,checkout_time)
    #只入住一天，则调用multiple_locations方法
    if(nights==1):
        #返回形式为：[酒店名称，距离，评分，评论，价格，类型，地点，综合评分]
        return multiple_locations(city,place,checkin_time,checkout_time,weights,type,cursor)
    else:
        #计算每个地点之间的相互距离，得到距离矩阵
        #判断是否有两个地点相隔较远，目前以12km为界限，后续考虑更新方法
        maximum=25
        divide=False
        far=[]
        place_distance=[[0 for k in range(len(place))] for k in range(len(place))]
        for i in range(len(place)):
            for j in range(len(place)):
                if(j<i):
                    continue
                place_distance[i][j]=distance(place[i],place[j])
                #对称矩阵
                place_distance[j][i]=place_distance[i][j]
                if(float(place_distance[i][j])>=maximum):
                    far.append([i,j])
                    divide=True
            place_distance[i][i]=0
        #若不需要分组，那么推荐方法同multiple_locations，是否需要分组用是否相隔较远判断
        #否则先将地点分组，每组地点距离较近，且每组地点数量不超过4
        results=[]
        #若分组，则输出矩阵为多组酒店集合，至少一组，至多四组，那么我们在前端应该并列显示这多组酒店
        #每一组中的距离为到该分组某一地点的距离，实际中我们应该显示距离它最近地点的距离
        #这样我们应该改进我们的输出形式
        #每一组酒店的原输出形式为[酒店名称，距离，评分，评论，价格，类型，链接，综合评分]
        #改进后为[酒店名称，距离，评分，评论，价格，类型，地点，综合评分]
        #因为综合评分是前端所不需要的，所以可以删去，改为距离该酒店最近的地点
        if(divide):
            #得到分组矩阵，用下标表示
            group=divide_group(place_distance,far,maximum)
            #分别对每一组地点进行推荐
            #得到第一组地点
            place_group_1=[]
            for i in range(4):
                if(group[0][i]!=999):
                    place_group_1.append(place[group[0][i]])
            #计算出第一组的推荐列表
            hotels_1=multiple_locations(city,place_group_1,checkin_time,checkout_time,weights,type,cursor)
            results.append(hotels_1)
            #得到第二组地点
            place_group_2=[]
            for i in range(4):
                if(group[1][i]!=999):
                    place_group_2.append(place[group[1][i]])
            #计算出第二组的推荐列表
            hotels_2=multiple_locations(city,place_group_2,checkin_time,checkout_time,weights,type,cursor)
            results.append(hotels_2)
            #判断是否存在第三组
            if(group[2][0]!=999):
                # 得到第三组地点
                place_group_3 = []
                for i in range(4):
                    if (group[2][i] != 999):
                        place_group_3.append(place[group[2][i]])
                # 计算出第三组的推荐列表
                hotels_3 = multiple_locations(city, place_group_3, checkin_time, checkout_time,weights,type,cursor)
                results.append(hotels_3)
            #判断是否存在第四组
            if(group[3][0]!=999):
                # 得到第四组地点
                place_group_4 = []
                for i in range(4):
                    if (group[3][i] != 999):
                        place_group_4.append(place[group[3][i]])
                # 计算出第四组的推荐列表
                hotels_4 = multiple_locations(city, place_group_4, checkin_time, checkout_time,weights,type,cursor)
                results.append(hotels_4)
        else:
            #返回形式为：[酒店名称，距离，评分，评论，价格，类型，地点，综合评分]
            results=multiple_locations(city,place,checkin_time,checkout_time,weights,type,cursor)
        return results

#将地点按相互间的距离分组，最多四组，最少两组，每组地点数量不超过4个
#这样限制的原因是：在用户实际使用过程中，输入过多地点或者显示多组酒店会引起用户体验感下降
#将相互距离大于12km的下标矩阵也作为输入，会减少很多计算量
#输入判断两个地点是否相隔较远的距离值
#最多允许四对不同的地点，它们相互距离大于12km
#返回结果为分组矩阵
def divide_group(distance,far,maximum):
    #至少有一组地点相隔较远，将其分别放入结果集的前两组，寻找各自最近的点，每组最多有四个点
    #若分完两组，还有地点没有被分组，从剩下的地点中选出一个作为第三组的第一个点，然后继续寻找最近点
    #以此类推
    #初始矩阵，最多有十二个地点，最多四个组，用99这样的大数表示非地点
    temp=[[999,999,999,999],
          [999,999,999,999],
          [999,999,999,999],
          [999,999,999,999]]
    temp[0][0]=far[0][0]
    temp[1][0]=far[0][1]
    number_1=1      #第一组元素个数
    temp1=0         #虽然不是重复出现，但是距离较远的地点的数量
    for j in range(3):
        # 判断是否所有点都已经加入到分组中
        if((number_1+temp1)==len(distance)):
            break
        temp_1 = maximum
        for i in range(len(distance)):
            # 寻找离第j点最近的点，并加入点集
            # 即在第一个点附近找到离它最近的点并加入点集，然后在最新加入的点附近找到最近的点加入点集，以此类推
            # 注意不能重复加入
            exist = False
            #判断这个下标是否已经存在
            for k in range(4):
                if (i == temp[0][k]):
                    exist = True
            for k in range(4):
                if(i==temp[1][k]):
                    exist=True
            if (exist):
                continue
            if (distance[i][temp[0][j]] < temp_1):
                temp_1 = distance[i][temp[0][j]]
                temp[0][j + 1] = i
            else:
                temp1=temp1+1
        if (temp[0][j + 1] != 999):
            number_1 = number_1 + 1

    number_2=1      #第二组元素个数
    temp2=0         #虽然不是重复出现，但是距离较远的地点的数量
    for j in range(3):
        # 判断是否所有点都已经加入到分组中
        if((number_1+number_2+temp2)>=len(distance)):
            break
        temp_1 = maximum
        for i in range(len(distance)):
            # 寻找离第j点最近的点，并加入点集
            # 即在第一个点附近找到离它最近的点并加入点集，然后在最新加入的点附近找到最近的点加入点集，以此类推
            # 注意不能重复加入
            exist = False
            #判断这个下标是否已经存在
            for k in range(4):
                if (i == temp[0][k]):
                    exist = True
            for k in range(4):
                if(i==temp[1][k]):
                    exist=True
            if (exist):
                continue
            if (distance[i][temp[1][j]] < temp_1):
                temp_1 = distance[i][temp[1][j]]
                temp[1][j + 1] = i
            else:
                temp2=temp2+1
        if (temp[1][j + 1] != 999):
            number_2 = number_2 + 1

    number_3=0      #第三组元素个数
    temp3=0         #虽然不是重复出现，但是距离较远的地点的数量
    #如果还有未被分组的地点，那么继续进行第三组的分组
    if((number_1+number_2)<len(distance)):
        #选出一个点作为第三组的第一个点
        #遍历原距离矩阵的所有点，找到第一个在原距离矩阵但是不在一二组中的下标，将其作为第三组的第一个点
        for i in range(len(distance)):
            inexist=True
            for j in range(4):
                if(i==temp[0][j]):
                    inexist=False
                    break
            for j in range(4):
                if(i==temp[1][j]):
                    inexist=False
                    break
            if(inexist):
                temp[2][0]=i
                number_3=1
                break
        for j in range(3):
            # 判断是否所有点都已经加入到分组中
            if ((number_1+number_2+number_3+temp3) == len(distance)):
                break
            temp_1 = maximum
            for i in range(len(distance)):
                # 寻找离第j点最近的点，并加入点集
                # 即在第一个点附近找到离它最近的点并加入点集，然后在最新加入的点附近找到最近的点加入点集，以此类推
                # 注意不能重复加入
                exist = False
                # 判断这个下标是否已经存在
                for k in range(4):
                    if (i == temp[0][k]):
                        exist = True
                for k in range(4):
                    if (i == temp[1][k]):
                        exist = True
                for k in range(4):
                    if(i==temp[2][k]):
                        exist=True
                if (exist):
                    continue
                if (distance[i][temp[2][j]] < temp_1):
                    temp_1 = distance[i][temp[2][j]]
                    temp[2][j + 1] = i
                else:
                    temp3=temp3+1
            if (temp[2][j + 1] != 999):
                number_3 = number_3 + 1

    number_4=0      #第四组元素个数
    temp4=0         #虽然不是重复出现，但是距离较远的地点的数量
    #如果还有未被分组的地点，那么继续进行第四组的分组
    if((number_1+number_2+number_3)<len(distance)):
        #选出一个点作为第三组的第一个点
        #遍历原距离矩阵的所有点，找到第一个在原距离矩阵但是不在一二组中的下标，将其作为第三组的第一个点
        for i in range(len(distance)):
            inexist=True
            for j in range(4):
                if(i==temp[0][j]):
                    inexist=False
                    break
            for j in range(4):
                if(i==temp[1][j]):
                    inexist=False
                    break
            for j in range(4):
                if(i==temp[2][j]):
                    inexist=False
            if(inexist):
                temp[3][0]=i
                number_4=1
                break
        for j in range(3):
            # 判断是否所有点都已经加入到分组中
            if ((number_1+number_2+number_3+number_4+temp4) == len(distance)):
                break
            temp_1 = maximum
            for i in range(len(distance)):
                # 寻找离第j点最近的点，并加入点集
                # 即在第一个点附近找到离它最近的点并加入点集，然后在最新加入的点附近找到最近的点加入点集，以此类推
                # 注意不能重复加入
                exist = False
                # 判断这个下标是否已经存在
                for k in range(4):
                    if (i == temp[0][k]):
                        exist = True
                for k in range(4):
                    if (i == temp[1][k]):
                        exist = True
                for k in range(4):
                    if(i==temp[2][k]):
                        exist=True
                for k in range(4):
                    if(i==temp[3][k]):
                        exist=True
                if (exist):
                    continue
                if (distance[i][temp[3][j]] < temp_1):
                    temp_1 = distance[i][temp[3][j]]
                    temp[3][j + 1] = i
                else:
                    temp4=temp4+1
            if (temp[3][j + 1] != 999):
                number_3 = number_3 + 1

    return temp

#入住晚数，用离开时间减去入住时间
def night(checkin_time,checkout_time):
    nights=0
    #先提取出入住和离开的年，月，日
    checkin_year=int(checkin_time[0:4])
    checkout_year=int(checkout_time[0:4])
    checkin_month=int(checkin_time[5:7])
    checkout_month=int(checkout_time[5:7])
    checkin_day=int(checkin_time[8:])
    checkout_day=int(checkout_time[8:])
    #先判断入住年是否为闰年
    if((checkin_year%4)==0):
        runnian=True
    else:
        runnian=False
    #判断离开年是否为闰年
    if((checkout_year)%4==0):
        out_runnian=True
    else:
        out_runnian=False
    #在同一年
    if(checkin_year==checkout_year):
        #在同一个月
        if(checkin_month==checkout_month):
            nights=checkout_day-checkin_day
        #不在同一月，那么晚数等于（入住月总天数-入住日期+1）+（离开月日期-1）+（中间月总天数）
        else:
            temp2 = checkout_day - 1
            temp3 = 0
            #根据入住月计算，共十三种情况（2月有两种情况）
            if(checkin_month==1):
                temp1=31-checkin_day+1
                if(checkout_month==3):
                    temp3=28
                elif(checkout_month==4):
                    temp3=28+31
                elif(checkout_month==5):
                    temp3=28+31+30
                elif(checkout_month==6):
                    temp3=28+31+30+31
                elif(checkout_month==7):
                    temp3=28+31+30+31+30
                elif(checkout_month==8):
                    temp3=28+31+30+31+30+31
                elif(checkout_month==9):
                    temp3=28+31+30+31+30+31+31
                elif(checkout_month==10):
                    temp3=28+31+30+31+30+31+31+30
                elif(checkout_month==11):
                    temp3=28+31+30+31+30+31+31+30+31
                elif(checkout_month==12):
                    temp3=28+31+30+31+30+31+31+30+31+30
                if(checkout_month==2):
                    nights=temp1+temp2+temp3
                else:
                    if(runnian):
                        nights=temp1+temp2+temp3+1
                    else:
                        nights=temp1+temp2+temp3
            if(checkin_month==2):
                if(runnian):
                    temp1=29-checkin_day+1
                else:
                    temp1=28-checkin_day+1
                if (checkout_month == 4):
                    temp3 = 31
                elif (checkout_month == 5):
                    temp3 = 31 + 30
                elif (checkout_month == 6):
                    temp3 = 31 + 30 + 31
                elif (checkout_month == 7):
                    temp3 = 31 + 30 + 31 + 30
                elif(checkout_month==8):
                    temp3=  31+30+31+30+31
                nights=temp1+temp2+temp3
            if(checkin_month==3):
                temp1=31-checkin_day+1
                if (checkout_month == 5):
                    temp3 =30
                elif (checkout_month == 6):
                    temp3 =30 + 31
                elif (checkout_month == 7):
                    temp3 =30 + 31 + 30
                elif (checkout_month == 8):
                    temp3 =30 + 31 + 30 + 31
                elif (checkout_month == 9):
                    temp3 =30 + 31 + 30 + 31 + 31
                nights=temp1+temp2+temp3
            if(checkin_month==4):
                temp1=30-checkin_day+1
                if (checkout_month == 6):
                    temp3 =31
                elif (checkout_month == 7):
                    temp3 =31 + 30
                elif (checkout_month == 8):
                    temp3 =31 + 30 + 31
                elif (checkout_month == 9):
                    temp3 =31 + 30 + 31 + 31
                elif (checkout_month == 10):
                    temp3 =31 + 30 + 31 + 31 + 30
                nights=temp1+temp2+temp3
            if(checkin_month==5):
                temp1=31-checkin_day+1
                if (checkout_month == 7):
                    temp3 =30
                elif (checkout_month == 8):
                    temp3 =30 + 31
                elif (checkout_month == 9):
                    temp3 =30 + 31 + 31
                elif (checkout_month == 10):
                    temp3 =30 + 31 + 31 + 30
                elif (checkout_month == 11):
                    temp3 =30 + 31 + 31 + 30 + 31
                nights=temp1+temp2+temp3
            if(checkin_month==6):
                temp1=30-checkin_day+1
                if (checkout_month == 8):
                    temp3 = 31
                elif (checkout_month == 9):
                    temp3 = 31 + 31
                elif (checkout_month == 10):
                    temp3 = 31 + 31 + 30
                elif (checkout_month == 11):
                    temp3 = 31 + 31 + 30 + 31
                elif (checkout_month == 12):
                    temp3 = 31 + 31 + 30 + 31 + 30
                nights=temp1+temp2+temp3
            if(checkin_month==7):
                temp1=31-checkin_day+1
                if (checkout_month == 9):
                    temp3 = 31
                elif (checkout_month == 10):
                    temp3 = 31 + 30
                elif (checkout_month == 11):
                    temp3 = 31 + 30 + 31
                elif (checkout_month == 12):
                    temp3 = 31 + 30 + 31 + 30
                nights=temp1+temp2+temp3
            if(checkin_month==8):
                temp1=31-checkin_day+1
                if (checkout_month == 10):
                    temp3 = 30
                elif (checkout_month == 11):
                    temp3 = 30 + 31
                elif (checkout_month == 12):
                    temp3 = 30 + 31 + 30
                nights = temp1 + temp2 + temp3
            if(checkin_month==9):
                temp1=30-checkin_day+1
                if (checkout_month == 11):
                    temp3 = 31
                elif (checkout_month == 12):
                    temp3 = 31 + 30
                nights = temp1 + temp2 + temp3
            if(checkin_month==10):
                temp1=31-checkin_day+1
                if (checkout_month == 12):
                    temp3 = 31 + 30
                nights = temp1 + temp2 + temp3
            if(checkin_month==11):
                temp1=30-checkin_day+1
                nights = temp1 + temp2 + temp3
    #不在同一年，那么即使月份相同，也应该另作处理
    #由于最多只能处理五个月，所以前一年的月份最早应该从8月份开始，下一年的月份最迟为5月
    else:
        temp2 = checkout_day - 1
        temp3 = 0
        if(checkin_month==8):
            temp1=31-checkin_day+1
            temp3=30+31+30+31
            nights=temp1+temp2+temp3
        if(checkin_month==9):
            temp1=30-checkin_day+1
            if(checkout_month==2):
                temp3=31+30+31+31
            else:
                temp3=31+30+31
            nights=temp1+temp2+temp3
        if(checkin_month==10):
            temp1=31-checkin_day+1
            if(checkout_month==2):
                temp3=30+31+31
            elif(checkout_month==3):
                if(out_runnian):
                    temp3=30+31+31+29
                else:
                    temp3=30+31+31+28
            nights=temp1+temp2+temp3
        if(checkin_month==11):
            temp1=30-checkin_day+1
            if(checkout_month==2):
                temp3=31+31
            elif(checkout_month==3):
                if(out_runnian):
                    temp3=31+31+29
                else:
                    temp3=31+31+28
            elif(checkout_month==4):
                if(out_runnian):
                    temp3=31+31+29+31
                else:
                    temp3=31+31+28+31
            nights = temp1 + temp2 + temp3
        if(checkin_month==12):
            temp1 = 31 - checkin_day + 1
            if (checkout_month == 2):
                temp3 = 31
            elif (checkout_month == 3):
                if (out_runnian):
                    temp3 = 31 + 29
                else:
                    temp3 = 31 + 28
            elif (checkout_month == 4):
                if (out_runnian):
                    temp3 = 31 + 29 + 31
                else:
                    temp3 = 31 + 28 + 31
            elif(checkout_month==5):
                if (out_runnian):
                    temp3 = 31 + 29 + 31 + 30
                else:
                    temp3 = 31 + 28 + 31 + 30
        nights = temp1 + temp2 + temp3
    return nights

# temp_1="2021-06-31"
# temp_2="2021-07-02"
# print(night(temp_1,temp_2))
