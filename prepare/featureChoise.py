#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pandas import Series
import pandas as pd
from matplotlib import pyplot as plt
from utils import inout
from pandas import DataFrame
from sklearn.ensemble import RandomForestRegressor
from pandas import read_csv
from sklearn.feature_selection import RFE
import numpy as np
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf

if __name__ == '__main__':
    # inputFileName = 'car_sales.csv'
    # inputFileName = 'O1005-O1005_model_trial.csv'
    inputFileName = 'O1002-PAX_model_trial.csv'
    inputFilePath = inout.getDataModelPipelinePath(inputFileName)
    out1FileName = 'O1005_diff_10.csv'
    out1FilePath = inout.getDataModelPipelinePath(out1FileName)
    out2FileName = 'lags_features_origin_O1002.csv'
    out2FilePath = inout.getDataModelPipelinePath(out2FileName)
    out3FileName = 'lags_features_clean_O1002.csv'
    out3FilePath = inout.getDataModelPipelinePath(out3FileName)

    diff_window = 10
    lags_feature_num = 4

    # data = Series.from_csv(inputFilePath,header=0)
    data = pd.read_csv(inputFilePath,header=None)
    ts = data[4]
    ts.index = data[0]
    # ts_log = ts
    ts_log = np.log(ts)

    ##
    # ts.plot()
    # plt.show()

    ##
    # diff_10 = ts_log.diff(diff_window)
    # diff_10.dropna(inplace=True)
    # diff_10.to_csv(out1FilePath)
    # diff_10.plot()
    # plt.show()
    # adftest = adfuller(diff_10)
    # print 'adf p-value:',adftest[1]
    # plot_acf(diff_10,lags=31)
    # plt.show()

    ## lags
    print type(ts_log.values)
    # print ts_log.values
    dataframe = DataFrame()
    for i in range(diff_window,0,-1):
        dataframe['t-'+str(i)] = ts_log.shift(i)
    dataframe['t'] = ts_log.values
    # print dataframe.head(10)
    dataframe.to_csv(out2FilePath,index=False)
    # dataframe = dataframe[10:]
    dataframe.dropna(inplace=True)
    dataframe.to_csv(out3FilePath,index=False)

    ## 根据重要性选择滞后特征
    # dataframe = read_csv(out3FilePath,header=0)
    # array = dataframe.values
    # # print array
    # x = array[:,0:-1]
    # # print x
    # y = array[:,-1]
    # model = RandomForestRegressor(n_estimators=500,random_state=1)
    # model.fit(x,y)
    # print model.feature_importances_
    # names = dataframe.columns.values[0:-1]
    # print names
    # ticks = [i for i in range(len(names))]
    # print ticks
    # plt.bar(ticks,model.feature_importances_)
    # plt.xticks(ticks,names)
    # plt.show()

    ##
    # dataframe = read_csv(out3FilePath, header=0)
    # array = dataframe.values
    # x = array[:, 0:-1]
    # y = array[:, -1]
    # rfe = RFE(RandomForestRegressor(n_estimators=500, random_state=1),lags_feature_num)
    # fit = rfe.fit(x, y)
    # print fit.support_
    # print 'selected features:'
    # names = dataframe.columns.values[0:-1]
    # for i in range(len(fit.support_)):
    #     if fit.support_[i]:
    #         print names[i]
    # names = dataframe.columns.values[0:-1]
    # ticks = [i for i in range(len(names))]
    # plt.bar(ticks,fit.ranking_)
    # plt.xticks(ticks,names)
    # plt.show()


