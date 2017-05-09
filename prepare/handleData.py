#/usr/bin/env python
# -*- coding:utf-8 -*-

from utils import inout
from collections import OrderedDict
import os
import codecs

def getTradeActionDicDayDic(infoList):
    dic = OrderedDict()
    if infoList:
        for actionRecord in infoList:
            actionRecordList = actionRecord.split(',')


def getProxyClassifyDicList(jsonList):
    '''

    '''
    dic = OrderedDict()
    for i in range(len(jsonList)):
        lineProxyJson = jsonList[i]
        proxyKey = lineProxyJson.keys()[0]
        if proxyKey not in dic.keys():
            dic[proxyKey] = []
        for k,vList in lineProxyJson[proxyKey].items():
            dic[proxyKey].extend(vList)
    return dic


def getProxyActionClassifyDicList(proxyInfoList):
    '''

    '''
    # 初始化字典
    initDic = dict()
    resultDic = dict()
    for item in proxyInfoList:
        itemList = item.strip().split(',')
        proxyActionName = itemList[1] + '-' + itemList[2]
        # 增加新的key值
        if proxyActionName not in initDic.keys():
            initDic[proxyActionName] = []
        # 添加元素
        initDic[proxyActionName].append(item)
    # 调整字典列表，使其按照day升序排列
    for k,vList in initDic.items():
        resultDic[k] = sorted(vList,key = lambda itemRecord : itemRecord[0])
    return resultDic



if __name__ == '__main__':

    """
        1 将原始数据按照代理分类处理，生成csv文件
    """
    # ## 第一步的代理分类字典列表
    # proxyClassifyDicList = OrderedDict()
    #
    # # inFileName = 'searchRegular_01.txt'
    # inFileName = 'proxy_json.txt'
    # inFilePath = inout.getDataPreparePath(inFileName)
    # # 加载数据
    # jsonList = inout.loadData2Json(inFilePath)
    #
    # # 获取第一步代理分类字典列表
    # proxyClassifyDicList = getProxyClassifyDicList(jsonList)
    # print type(proxyClassifyDicList)
    # # 将代理分类字典列表中每一个代理对应的记录写入到csv文件
    # for k,vList in proxyClassifyDicList.items():
    #     print k,len(vList),type(vList),vList
    #     outFileName = 'proxy_classify_' + k + '.csv'
    #     outFilePath = inout.getDataRegularProxyClassifyPath(outFileName)
    #     inout.writeList2Txt(outFilePath,vList)


    """
       2 统计所有代理行为纪录的条数
        并将统计信息生成文件
    """
    # # # 获取目录
    # inProxyClassifyDir = inout.getDataRegularProxyClassifyDir()
    # # 获取目录下文件名列表
    # csvNameList = os.listdir(inProxyClassifyDir)
    #
    # # 遍历处理每一个文件
    # i = 0
    # statisticNumList = []
    # for csvName in csvNameList:
    #     itemFilePath = inout.getDataRegularProxyClassifyPath(csvName)
    #     # 获取代理行为分类列表
    #     proxyInfoList = inout.readListFromTxt(itemFilePath)
    #     proxyActionClassifyDicList = getProxyActionClassifyDicList(proxyInfoList)
    #     # 分类列表写出到文件
    #     for k, vList in proxyActionClassifyDicList.items():
    #         statisticNumList.append(len(vList))
    #     i += 1
    #     print i
    # print '开始排序'
    # statisticNumList = sorted(statisticNumList)
    # print '排序完成'
    # print 'statisticNumList length:'
    # print len(statisticNumList)
    # outFilePath = inout.getDataPreparePath('allProxyAction.csv')
    # print '开始写入文件'
    # fw = codecs.open(outFilePath, 'wb')
    # for j in range(len(statisticNumList)):
    #     outLine = str(j + 1) + ',' + str(statisticNumList[j])
    #     fw.write(outLine + '\n')
    # fw.close()
    # print '写入文件完成'


    """
       3 为模型选择做实验（测试模型的可靠性）
        选取代理行为纪录数为90的某个代理的行为纪录，并生成csv文件
    """
    ## 获取目录下文件列表
    # 获取目录
    inProxyClassifyDir = inout.getDataRegularProxyClassifyDir()
    # 获取目录下文件名列表
    csvNameList = os.listdir(inProxyClassifyDir)

    # 遍历处理每一个文件
    i = 0
    outputList= []
    flage = False
    for csvName in csvNameList:
        # proxyName = csvName.split('.')[0].split('_')[-1]
        itemFilePath = inout.getDataRegularProxyClassifyPath(csvName)
        # 获取代理行为分类列表
        proxyInfoList = inout.readListFromTxt(itemFilePath)
        proxyActionClassifyDicList = getProxyActionClassifyDicList(proxyInfoList)
        # 分类列表写出到文件
        for k,vList in proxyActionClassifyDicList.items():
            print k
            vList = list(set(vList))
            if len(vList)>90 and 'O1002' not in k.split('-'):
                outputList = vList
                outputFileName = k+'_model_trial.csv'
                flage = True
                break
        if flage == True:break

    ## 一定要注意这里要去重
    outputList = list(set(outputList))

    outFilePath = inout.getDataPreparePath(outputFileName)
    print '开始写入文件'
    inout.writeList2Txt(outFilePath,outputList)
    print '写入文件完成'

















    # ##
    # inFileName = 'test_proxy_classify_O1014.csv'
    # inFilePath = inout.getDataRegularPath(inFileName)
    # infoList = inout.readListFromTxt(inFilePath)
    #
    # # 交易行为字典天数字典
    # tradeActionDicDayDic = getTradeActionDicDayDic(infoList)


