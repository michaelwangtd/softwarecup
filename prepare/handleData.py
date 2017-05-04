#/usr/bin/env python
# -*- coding:utf-8 -*-

from utils import inout
from collections import OrderedDict

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


if __name__ == '__main__':

    """
        将原始数据按照代理分类处理，生成csv文件
    """
    ## 第一步的代理分类字典列表
    # proxyClassifyDicList = OrderedDict()
    #
    # inFileName = 'searchRegular_01.txt'
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
    #     outFilePath = inout.getDataRegularPath(outFileName)
    #     inout.writeList2Txt(outFilePath,vList)



    """
        对于确定的某一个代理对象，读取代理对象对应的csv文件；
        按照代理交易行为记录分类；
        在交易行为记录下按照存在的天数进行统计并分类
    """
    # 这里到时候可以设计成借口
    inFileName = 'proxy_classify_O1014.csv'
    inFilePath = inout.getDataRegularPath(inFileName)
    infoList = inout.readListFromTxt(inFilePath)

    # 交易行为字典天数字典
    tradeActionDicDayDic = getTradeActionDicDayDic(infoList)


