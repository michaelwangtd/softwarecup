#!/usr/bin/env python
# -*- coding:utf-8 -*-

from matplotlib import pyplot as plt
import pandas as pd
from utils import inout
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn import svm
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import Lasso, Ridge
from sklearn.model_selection import GridSearchCV

"""
    input file:proxy action记录文件
    1 代理行为记录文件转换格式或重写读取部分代码

    2 计算该文件滞后重要性特征：
        1）算法要改写i/o接口
        2）参数提取出来：滞后周期，重要性特征个数

    3 根据生成的重要性特征列表
"""


if __name__ == '__main__':

    """
        不在pipeline的范围，测试模型预测的准确性
        logistic regression
    """
    pd.set_option('display.width', 300)
    np.set_printoptions(linewidth=300, suppress=True)

    # 这里的滞后特征列表可以由之前的过程得到
    lags_feature_list = ['t-6','t-3','t-2','t-1','t']
    forecast_len = 11

    inFileName = 'lags_features_clean.csv'
    # inFileName = 'lags_features_clean_O1002.csv'
    inFilePath = inout.getDataModelPipelinePath(inFileName)
    data = pd.read_csv(inFilePath,header=0)
    data = data[lags_feature_list].values
    # print data
    # 先把训练集/测试集数据分开
    train_data = data[:70]
    test_data = data[70:]
    # print type(test_data[:,-1])
    # exit(0)
    # print len(train_data)
    # print len(test_data)
    # 初始化预测查询表
    x_train = train_data[:,0:-1]
    y_train = train_data[:,-1]
    # print x_train
    # print type(x_train)
    # print x_train.shape()
    # print y_train
    # print type(y_train)
    # exit(0)

    base_num = len(y_train)
    predict_search_list = list(y_train)

    alpha_can = np.logspace(-3, 2, 10)

    # model = Ridge()
    # lr = GridSearchCV(model, param_grid={'alpha': alpha_can}, cv=5)
    lr = DecisionTreeRegressor(criterion='mse', max_depth=20)
    # lr = LogisticRegression()
    # lr = LinearRegression()
    # lr = svm.SVR(kernel='rbf',gamma=0.2,C=100)
    # x_train = x_train.reshape(-1,1)
    lr.fit(x_train, y_train)

    y_hat_list = []
    # 滚动预测
    for i in range(0,forecast_len):
        curr_index = i + base_num
        predict_queue = []
        predict_queue.append(predict_search_list[curr_index-6])
        predict_queue.append(predict_search_list[curr_index-3])
        predict_queue.append(predict_search_list[curr_index-2])
        predict_queue.append(predict_search_list[curr_index-1])
        predict_queue = np.array(predict_queue)
        print i,predict_queue
        print type(predict_queue)
        # exit(0)

        y_hat = lr.predict(predict_queue)
        print 'result:',y_hat
        y_hat_list.append(y_hat[0])
        predict_search_list.append(y_hat[0])
    print len(y_hat_list),y_hat_list
    print len(test_data[:,-1]),test_data[:,-1]
    # exit(0)
    plt.figure()
    ticks = [i for i in range(len(y_hat_list))]
    y_hat = np.array(y_hat_list)
    plt.subplot(1,1,1)
    plt.plot(ticks,y_hat,'-b')
    plt.plot(ticks,test_data[:,-1],'-r')
    plt.show()
    # pyplot.bar(ticks,fit.ranking_)
    # pyplot.xticks(ticks,names)

    exit(0)




    x = data[lags_feature_list].values
    y = data['t'].values
    # print type(x)
    # print x
    # print type(y)
    # print y

    x_train = x[:70]
    y_train = y[:70]
    x_test = x[70:]
    y_test = y[70:]

    lr = LogisticRegression()
    # lr = svm.SVR(kernel='rbf',gamma=0.2,C=100)
    lr.fit(x_train,y_train)



    y_hat = lr.predict(x_test)

    x_time = [i for i in range(11,len(y)+11)]
    print x_time
    x_test_time = x_time[60:]
    print x_test_time

    plt.figure(facecolor='w')
    plt.plot(x_time,y,'g-')
    plt.plot(x_test_time,y_hat,'r-')
    plt.show()




