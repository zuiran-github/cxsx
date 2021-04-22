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
import qunar
#定义一个初始测试数据集——数组
#选择地点后，得到该地区的酒店实时信息

# testdata=[[],   #酒店名称
#           [],   #酒店距离选定地点的距离，单位设置为km
#           [],   #酒店评分
#           [],   #酒店评论数
#           [],   #酒店房间最低价格（根据人数推荐，如果是一个人，优先推荐单间，两个人及以上优先推荐标准双人间
#           [],   #类型
#           []    #位置
#           ]
#将testdata进行转置

#定义排序算法，根据评分，价格，评论数，距离远近排序
#根据酒店距离选定地点的远近进行排序，按照距离升序排序
def sort_distance(testdata):
    copydata=copy.deepcopy(testdata)    #深度拷贝测试数组,对拷贝数组进行操作
    for i in range(len(copydata)-1):
        for i in range(len(copydata)-1):
            temp=copydata[i];
            if(copydata[i][1]>copydata[i+1][1]):
                copydata[i]=copydata[i+1]
                copydata[i+1]=temp
    return copydata

#根据评分高低进行排序
def sort_points(testdata):
    copydata=copy.deepcopy(testdata)    #深度拷贝测试数组,对拷贝数组进行操作
    for i in range(len(copydata)-1):
        for i in range(len(copydata)-1):
            temp=copydata[i];
            if(copydata[i][2]<copydata[i+1][2]):
                copydata[i]=copydata[i+1]
                copydata[i+1]=temp
    return copydata

#根据评论数进行降序排列
def sort_comment(testdata):
    copydata=copy.deepcopy(testdata)    #深度拷贝测试数组,对拷贝数组进行操作
    for i in range(len(copydata)-1):
        for i in range(len(copydata)-1):
            temp=copydata[i];
            if(copydata[i][3]<copydata[i+1][3]):
                copydata[i]=copydata[i+1]
                copydata[i+1]=temp
    return copydata

#根据价格高低进行降序排列
def sort_price_descend(testdata):
    copydata=copy.deepcopy(testdata)    #深度拷贝测试数组,对拷贝数组进行操作
    for i in range(len(copydata)-1):
        for i in range(len(copydata)-1):
            temp=copydata[i];
            if(copydata[i][4]<copydata[i+1][4]):
                copydata[i]=copydata[i+1]
                copydata[i+1]=temp
    return copydata

#根据价格高低进行升排列
def sort_price_ascend(testdata):
    copydata=copy.deepcopy(testdata)    #深度拷贝测试数组,对拷贝数组进行操作
    for i in range(len(copydata)-1):
        for i in range(len(copydata)-1):
            temp=copydata[i];
            if(copydata[i][4]>copydata[i+1][4]):
                copydata[i]=copydata[i+1]
                copydata[i+1]=temp
    return copydata

#综合评价法，初始权重：0.5（距离），0.3（评分），0.05（评论数），价格（0.15）
def sort_comprehensive_assess(testdata,weight_1,weight_2,weight_3,weight_4):
    score_matrix= [[0 for i in range(6)] for i in range(len(testdata))]   #综合评分矩阵
    #计算综合评分

    #计算距离
    #计算出最大距离
    max_distance=sort_distance(testdata)[len(testdata)-1][1]
    for i in range(len(testdata)):
        score_matrix[i][0]=weight_1*max_distance/testdata[i][1]

    #计算酒店评分
    #计算最小评分
    min_points=sort_points(testdata)[len(testdata)-1][2]
    for i in range(len(testdata)):
        score_matrix[i][1]=weight_2*((testdata[i][2]-min_points))/(5.0-min_points)

    #计算评论数
    #计算最多评论和最少评论
    max_comment=sort_comment(testdata)[0][3]
    min_comment=sort_comment(testdata)[len(testdata)-1][3]
    for i in range(len(testdata)):
        score_matrix[i][2]=weight_3*(testdata[i][3]-min_comment)/(max_comment-min_comment)

    #计算价格
    #计算最高价格和最低价格
    max_price=sort_price_descend(testdata)[0][4]
    min_price=sort_price_ascend(testdata)[0][4]
    for i in range(len(testdata)):
        score_matrix[i][3]=weight_4*(testdata[i][4]-min_price)/(max_price-min_price)

    #计算综合评分
    for i in range(len(testdata)):
        score_matrix[i][4]=score_matrix[i][0]+score_matrix[i][1]+score_matrix[i][2]+score_matrix[i][3]

    #根据评分高低得到排名
    #先将排名归零
    for i in range(len(testdata)):
        score_matrix[i][5]=0
    for i in range(len(testdata)-1):
        for j in range(i+1):
            if(score_matrix[j]<=score_matrix[i+1]):
                score_matrix[i+1][5]=score_matrix[i+1][5]+1
            else :
                score_matrix[j][5]=score_matrix[j][5]+1
    for i in range(len(testdata)):
        score_matrix[i][5]=len(testdata)-score_matrix[i][5]
    return score_matrix


#测试程序
#测试数据
#将地点定为上海
#获取上海所有酒店的实时数据
testlist0= qunar.getList('济南', '2021-04-23', '2021-04-25')[0]
testlist=[[0 for i in range(7)] for i in range(len(testlist0[0]))]
for i in range(len(testlist0[0])):
    for j in range(7):
        testlist[i][j]=testlist0[j][i]
# print(np.transpose(testlist))
# for i in range(len(testlist)):
#     for j in range(7):
#         print(testlist[i][j])
#     print()
# testdata_1=sort_distance(testlist)
testdata_2=sort_points(testlist)
# testdata_3=sort_comment(testlist)
# testdata_4=sort_price_descend(testlist)
# testdata_5=sort_price_ascend(testlist)
# testdata_6=sort_comprehensive_assess(testlist,0.5,0.3,0.05,0.15)
# for i in range(len(testlist)):
#     print(testdata_1[i])
# print()
for i in range(len(testlist)):
    print(testdata_2[i])
print()
# for i in range(len(testlist)):
#     print(testdata_3[i])
# print()
# for i in range(len(testlist)):
#     print(testdata_4[i])
# print()
# for i in range(len(testlist)):
#     print(testdata_5[i])
# for i in range(len(testlist)):
#     print(testdata_6[i])