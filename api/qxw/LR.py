import numpy as np
import matplotlib.pyplot as plt
from .dataProcessing import *
import math
'''
由于初始数据量较少，故使用逻辑回归模型对用户的点击情况进行反馈从而拟合用户的喜好
逻辑回归中y为定性变量，故y=0或1
1为点击，0为未点击
训练矩阵为：
x[ x1 x2 x3 x4],分别代表距离，评分，评论，价格，共m行
y[ y1 y2 y3 y3]
theta[ theta1 theta2 theta3 theta4]
构造预测函数为h(xi)=g(theta xi)=1/(1+e(-theta xi))
损失函数为J(theta)=-(1/m)l(theta)
模型的训练可以设置为1h进行一次（主观设置，后续考虑改进），训练结束之后将权重矩阵存储起来，以供查询时使用
'''

#预测函数
#输入下一次搜索得到的的数据矩阵x和已经训练出的权重矩阵，计算出可能被用户点击的概率
#矩阵x的形式为[酒店名称，距离，评分，评论，价格，类型，链接]
def prediction(x,theta):
   #输出矩阵形式：[酒店名称，距离，评分，评论，价格，类型，链接，综合评分]
   #构造输出矩阵
   outlist = [[0 for i in range(8)] for i in range(len(x))]
   for i in range(len(x)):
      for j in range(7):
         outlist[i][j]=x[i][j]
      #计算出theta*xi
      temp1=x[i][1]*theta[0]+x[i][2]*theta[1]+x[i][3]*theta[2]+x[i][4]*theta[3]
      temp2=1+math.exp(-temp1)
      outlist[i][7]=1/temp2
   return outlist

#不带正则项的损失函数
def loss(theta,h,y):
   m=len(h)
   temp1=0
   for i in range(m):
      temp1=temp1+y[i]*np.log(h[i])
   temp2=0
   for i in range(m):
      temp2=temp2+(1-y[i])*np.log(1-h[i])
   loss=-(temp1+temp2)/m
   return loss

#参数梯度
def gradient(x,h,y):
   m=len(h)
   temp=[]
   for j in range(4):
      temp[j]=0
      for i in range(m):
         temp[j]=temp[j]+(h[i]-y[i])*x[i][j]
      temp[j]=temp[j]/m
   return temp

def LR(x,y):
   # #先加载反馈来的数据
   # testdata_x,testdata_y=load_data
   #初始theta矩阵为零矩阵
   theta=[0,0,0,0]
   alpha=1
   i=1000   #迭代次数
   loss_array=[]
   for _ in range(i):
      h=prediction(x,theta)
      loss=loss(theta,h,y)
      gradient=gradient(x,h,y)
      theta=theta-np.multiply(gradient,alpha)
      loss_array.append(loss)
   #将得到的权重矩阵传出
   #同时将权重存入数据库
   update_weights(theta)
   return theta
   #对下一组酒店数据进行前向预测

def logistic_regression(testdata,weights):
   # #先加载反馈来的数据
   # testdata_x,testdata_y=load_data
   # weights=LR(testdata_x,testdata_y)
   #对下一组酒店数据进行前向预测
   # testdata=load_data
   results=prediction(testdata,weights)
   #将得到的前向预测矩阵按照被点击概率大小进行降序排序
   for i in range(len(results)-1):
      for i in range(len(results)-1):
         temp=results[i]
         if(results[i][7]<results[i+1][7]):
            results[i]=results[i+1]
            results[i+1]=temp
   #排序后的矩阵即为输出矩阵
