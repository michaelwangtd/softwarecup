# !/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
import index
import codecs
import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso, Ridge
from sklearn.model_selection import GridSearchCV


if __name__ == '__main__':
    path = index.ROOTPATH + '\\data\\svr_test_O1014-O1014.xls'

    data = pd.read_excel(path)
    x = data['day']
    y = data['avg']

    # x_pre = range(91,121)

    x = np.array(x)
    x_train = x[:80].reshape(-1,1)
    x_test = x[80:].reshape(-1,1)
    y = np.array(y)
    y_train = y[:80]
    y_test = y[80:]

    # x_pre = np.array(x_pre)
    # x_pre = x_pre.reshape(-1,1)

    # SVR
    svr = svm.SVR(kernel='rbf',gamma=0.2,C=100)
    svr.fit(x_train,y_train)
    y_hat = svr.predict(x_test)
    plt.figure(facecolor='w')
    plt.plot(x, y, 'g.')
    plt.plot(x_test, y_hat, 'r.')
    plt.title(u'SVR')
    plt.grid(True)
    plt.show()

    # # Line Regression
    # linreg = LinearRegression()
    # linreg.fit(x_train,y_train)
    # y_lr_hat = linreg.predict(x_test)
    # plt.figure(facecolor='w')
    # plt.plot(x, y, 'g.')
    # plt.plot(x_test, y_lr_hat, 'r.')
    # plt.plot(u'Line Regression')
    # plt.grid(True)
    # plt.show()
    #
    # # Lasso
    # model = Lasso()
    # alpha_can = np.logspace(-3,2,10)
    # lasso_model = GridSearchCV(model,param_grid={'alpha':alpha_can},cv=5)
    # lasso_model.fit(x_train,y_train)
    # y_ls_hat = lasso_model.predict(x_test)
    # plt.figure(facecolor='w')
    # plt.plot(x,y,'g.')
    # plt.plot(x_test,y_ls_hat,'r.')
    # plt.title(u'Lasso')
    # plt.grid(True)
    # plt.show()
    #
    # # Ridge
    # model = Ridge()
    # alpha_can = np.logspace(-3, 2, 10)
    # ridge_model = GridSearchCV(model, param_grid={'alpha': alpha_can}, cv=5)
    # ridge_model.fit(x_train, y_train)
    # y_ls_hat = ridge_model.predict(x_test)
    # plt.figure(facecolor='w')
    # plt.plot(x, y, 'g.')
    # plt.plot(x_test, y_ls_hat, 'r.')
    # plt.title(u'Ridge')
    # plt.grid(True)
    # plt.show()

