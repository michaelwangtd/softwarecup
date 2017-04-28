#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt
import warnings
from sklearn.exceptions import ConvergenceWarning



if __name__ == "__main__":
    # warnings.filterwarnings(action='ignore', category=ConvergenceWarning)
    N = 50
    np.random.seed(0)
    x = np.sort(np.random.uniform(0,6,N),axis=0)
    y = 2 * np.sin(x) + 0.1 * np.random.randn(N)
    x = x.reshape(-1,1)     # x为什么要写成列向量的形式，如果x为向量，则一行表示一个变量

    svr_rbf = svm.SVR(kernel='rbf',gamma=0.2,C=100)
    svr_rbf.fit(x,y)

    x_test = np.linspace(5,2.0*x.max(),100).reshape(-1,1)
    y_hat = svr_rbf.predict(x_test)

    plt.figure(figsize=(11,9),facecolor='w')
    plt.plot(x,y,'ro')
    plt.plot(x_test,y_hat,'b*')
    plt.grid(True)
    plt.show()


