#/usr/bin/env python
# -*- coding:utf-8 -*-

from utils import inout
import time
from collections import OrderedDict
import codecs

def getProxyDailyBuyAndSaleStatisticInfo(proxyKey,proxyValueDic):
    '''
        返回key为1-91形式的统计信息
    '''
    dic = OrderedDict()
    for i in range(1,92):
        dic[i] = []
    for keyDay,valueList in proxyValueDic.items():
        inDegree,inSumNum,inSumMoney,inAvgMoney,outDegree,outSumNum,outSumMoney,outAvgMoney = getInOutRelatedInfo(proxyKey,valueList)
        dic[int(keyDay)] = [inDegree,inSumNum,inSumMoney,inAvgMoney,outDegree,outSumNum,outSumMoney,outAvgMoney]
    return dic

def getInOutRelatedInfo(proxyKey,valueList):
    '''

    '''
    inDegree = 0
    outDegree = 0
    inSumNum = 0
    inSumMoney = 0
    outSumNum = 0
    outSumMoney = 0
    inAvgMoney = 0.0
    outAvgMoney = 0.0
    for item in valueList:
        # print item
        if proxyKey == item[1]:
            outDegree += 1
            outSumNum += int(item[3])
            outSumMoney += int(float(item[4]))
        if proxyKey == item[2]:
            inDegree += 1
            inSumNum += int(item[3])
            inSumMoney += int(float(item[4]))
    if inSumNum:
        inAvgMoney = inSumMoney / inSumNum
    if outSumNum:
        outAvgMoney = outSumMoney / outSumNum
    return inDegree,inSumNum,inSumMoney,inAvgMoney,outDegree,outSumNum,outSumMoney,outAvgMoney

def intList2strList(item):
    if item:
        tempList = []
        for intItem in item:
            tempList.append(str(intItem))
        return tempList


if __name__ == '__main__':
    inputFileName = 'proxy_json.txt'
    outputFileName = 'proxy_perday_ifno_statistic.txt'

    inputFilePath = inout.getDataPath(inputFileName)
    outputFilePath = inout.getDataPath(outputFileName)

    finalOutputList = []

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
        initDic[proxyKey] = getProxyDailyBuyAndSaleStatisticInfo(proxyKey,proxyValueDic)
        print initDic[proxyKey]
        # 构建输出list列表
        for k in initDic[proxyKey].keys():
            if initDic[proxyKey][k]:
                outputList = [proxyKey,int(k)]
                outputList.extend(initDic[proxyKey][k])
                finalOutputList.append(outputList)
        # if i >= 1:
        #     break
    print '统计字典构建完毕...'
    print '写出到xls'
    print 'finalOutputList length:'
    print len(finalOutputList)
    # inout.writeContent2Excel(finalOutputList,outputFilePath)
    # 因为数据量677677条，写入txt先
    fw = codecs.open(outputFilePath,'wb')
    for item in finalOutputList:
        item = intList2strList(item)
        outputLine = ','.join(item)
        fw.write(outputLine + '\n')
        print outputLine
    fw.close()

