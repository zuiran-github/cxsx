# 创新项目实训
# 比价&酒店推荐系统
# 住宿查询
import copy
import numpy as np
#定义一个初始测试数据集——数组
#选择地点后，得到该地区的酒店实时信息

# testdata=[[],   #酒店名称
#           [],   #酒店距离选定地点的距离，单位设置为km
#           [],   #酒店评分
#           [],   #酒店评论数
#           [],   #酒店房间最低价格
#           [],   #类型
#           []    #地点
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
#输入列表为[名称，距离，评分，评论数，价格，类型，地点]
#输出为综合评分矩阵[距离评分，评分，评论，价格，综合评分，排名]
#改进：输出形式为[酒店名称，距离，评分，评论，价格，类型，地点，综合评分]，并且按照综合评分降序排列
def sort_comprehensive_assess(testdata,weight_1,weight_2,weight_3,weight_4):
    score_matrix= [[0 for i in range(6)] for i in range(len(testdata))]   #综合评分矩阵
    out_matrix=copy.deepcopy(testdata)    #输出矩阵初始为输入矩阵的深度拷贝形式
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
        score_matrix[i][1]=weight_2*((testdata[i][2]-min_points)/(5.0-min_points))

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
        #将综合评分加在输出矩阵每一行的最后
        out_matrix[i].append(score_matrix[i][4])

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

    #对输出矩阵进行按照综合评分降序排列
    for i in range(len(out_matrix)-1):
        for j in range(len(out_matrix)-1):
            temp=out_matrix[j]
            #如果后者综合评分大于前者，那么调换顺序
            if(out_matrix[j][7]<out_matrix[j+1][7]):
                out_matrix[j]=out_matrix[j+1]
                out_matrix[j+1]=temp
    # print(out_matrix)
    return out_matrix

