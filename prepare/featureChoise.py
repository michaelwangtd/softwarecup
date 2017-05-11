#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pandas import Series
from matplotlib import pyplot
from utils import inout
from pandas import DataFrame
from sklearn.ensemble import RandomForestRegressor
from pandas import read_csv
from sklearn.feature_selection import RFE

if __name__ == '__main__':
    # inputFileName = 'car_sales.csv'
    inputFileName = 'O1005_O1005_model_trial.csv'
    inputFilePath = inout.getDataModelPipelinePath(inputFileName)
    out1FileName = 'cycle_adjusted.csv'
    out1FilePath = inout.getDataModelPipelinePath(out1FileName)
    out2FileName = 'lags_features_origin.csv'
    out2FilePath = inout.getDataModelPipelinePath(out2FileName)
    out3FileName = 'lags_features_clean.csv'
    out3FilePath = inout.getDataModelPipelinePath(out3FileName)

    data = Series.from_csv(inputFilePath,header=0)

    ##
    # print type(data)
    # print data
    # print data.head(5)
    # data.plot()
    # pyplot.show()

    ##
    # differenced = data.diff(10)
    # print differenced
    # differenced = differenced[12:]
    # print differenced
    # differenced.to_csv(out1FilePath)
    # differenced.plot()
    # pyplot.show()

    ## autocorrelation

    ## lags
    # print type(data.values)
    # print data.values
    # dataframe = DataFrame()
    # for i in range(10,0,-1):
    #     dataframe['t-'+str(i)] = data.shift(i)
    # dataframe['t'] = data.values
    # print dataframe.head(10)
    # dataframe.to_csv(out2FilePath,index=False)
    # dataframe = dataframe[10:]
    # dataframe.to_csv(out3FilePath,index=False)

    ##
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
    # pyplot.bar(ticks,model.feature_importances_)
    # pyplot.xticks(ticks,names)
    # pyplot.show()

    ##
    dataframe = read_csv(out3FilePath, header=0)
    array = dataframe.values
    x = array[:, 0:-1]
    y = array[:, -1]
    rfe = RFE(RandomForestRegressor(n_estimators=500, random_state=1),4)
    fit = rfe.fit(x, y)
    print fit.support_
    print 'selected features:'
    names = dataframe.columns.values[0:-1]
    for i in range(len(fit.support_)):
        if fit.support_[i]:
            print names[i]
    names = dataframe.columns.values[0:-1]
    ticks = [i for i in range(len(names))]
    pyplot.bar(ticks,fit.ranking_)
    pyplot.xticks(ticks,names)
    pyplot.show()


