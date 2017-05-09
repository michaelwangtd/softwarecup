#!/usr/bin/env python
# -*- coding:utf-8 -*-

from matplotlib import pyplot
import pandas as pd
from utils import inout
from sklearn.linear_model import LogisticRegression
from sklearn import svm

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
    inFileName = 'lags_features_clean_model_choise.csv'
    inFilePath = inout.getDataModelPipelinePath(inFileName)
    data = pd.read_csv(inFilePath)
    x = data[['t-6','t-3','t-2','t-1']].values
    y = data['t'].values
    # print type(x.values)
    # print x
    # print type(y.values)
    # print y
    x_train = x[:60]
    y_train = y[:60]
    x_test = x[60:]
    y_test = y[60:]

    lr = LogisticRegression()
    # lr = svm.SVR(kernel='rbf',gamma=0.2,C=100)
    lr.fit(x_train,y_train)
    y_hat = lr.predict(x_test)

    x_time = [i for i in range(11,len(y)+11)]
    print x_time
    x_test_time = x_time[60:]
    print x_test_time

    pyplot.figure(facecolor='w')
    pyplot.plot(x_time,y,'g-')
    pyplot.plot(x_test_time,y_hat,'r-')
    pyplot.show()




