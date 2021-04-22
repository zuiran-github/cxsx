import numpy as np
import matplotlib.pyplot as plt
import dataProcessing as load_data

# 前向预测算法
def forward_prediction(x, weights):
   f = np.matmul(x, weights.T)
   return np.divide(1, np.add(1, np.exp(-f)))

# 带正则项的损失函数
def loss(weights, h, y, _lambda):
   count = y.shape[0]
   loss_1 = -np.matmul(y.T, np.log(h))
   loss_0 = -np.matmul(np.add(1, -y).T, np.log(np.add(1, -h)))
   regularization_term = np.multiply(np.matmul(weights, weights.T), _lambda)
   loss_ = np.divide((loss_1 + loss_0 + regularization_term), count)
   return loss_

# 参数梯度
def gradient(x, h, y, alpha):
   count = h.shape[0]
   grad = np.divide(np.multiply(alpha, np.matmul(np.add(-y, h).T, x)), count)
   return grad

def main():
   data = load_data()
   x = data[:, :2]
   y = np.array([data[:, 2]]).T
   weights = np.zeros((1, x.shape[1]))
   _lambda = 0.001
   _alpha = 1
   loss_arr = []
   i = 1000
   for _ in range(i):
       h = forward_prediction(x=x, weights=weights)
       _loss = loss(weights, h, y, _lambda)
       grad = gradient(x, h, y, _alpha)
       weights = weights - np.multiply(grad, _alpha)
       loss_arr.append(_loss[0][0])
   h = forward_prediction(x=x, weights=weights)
   real = np.array([data[:, 2]]).T
   _ = np.append(h, real, axis=1)
   for __ in _:
       print(__)
   x_axis = np.arange(0, i, 1)
   # plt.plot(x_axis, loss_arr)
   # plt.show()
   # plt.draw()

# if __name__ == '__main__':
#    main()
