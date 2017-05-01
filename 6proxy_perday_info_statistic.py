#/usr/bin/env python
# -*- coding:utf-8 -*-

from utils import inout
import time
from collections import OrderedDict

def getProxyDailyBuyAndSaleStatisticInfo(proxyValueDic):
    '''
        返回key为1-91形式的统计信息
    '''


if __name__ == '__main__':
    inputFileName = 'proxy_json.txt'
    outputFileName = 'proxy_perday_ifno_statistic.xls'

    inputFilePath = inout.getDataPath(inputFileName)
    outputFilePath = inout.getDataPath(outputFileName)

    print '开始加载数据...'
    infoList = inout.loadData2Json(inputFilePath)
    print '数据加载完成...'
    # 构建统计字典
    initDic = OrderedDict()
    print '构建统计字典...'
    for i in range(len(infoList)):
        proxyKey = infoList[i].keys()[0]
        proxyValueDic = infoList[i][proxyKey]
        # 获取代理每天买入，卖出统计信息字典
        initDic[proxyKey] = getProxyDailyBuyAndSaleStatisticInfo(proxyValueDic)
        break
    print '统计字典构建完毕...'
