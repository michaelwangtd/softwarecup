# !/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas
from utils import inout
from utils import util
from collections import OrderedDict
import re

def getTradeNumSum(dayRecordList):
    tradeNumSum = 0
    for itemList in dayRecordList:
        tradeNumSum += int(itemList[3])
    return tradeNumSum

def getTradeMoneySum(dayRecordList):
    tradeMoneySum = 0
    for itemList in dayRecordList:
        tradeMoneySum += float(itemList[4])
    return tradeMoneySum


if __name__ == '__main__':

    outputPath = 'F:\\repositories\\softcup_back\\data\\'

    # 原始数据
    infoList = inout.readListFromTxt('F:\\repositories\\softcup_back\\data\\sales_sample_20170310.csv')
    print('total num: ' , len(infoList))

    splitInfoList = []
    # 生成splitInfoList列表
    for item in infoList:
        splitInfoList.append(item.strip().split(','))
    print('len splitInfoList: ' , len(splitInfoList))

    # # 按照天数分开的数据
    # dayDic = OrderedDict()
    # # 转化成excel格式数据
    # dayOutExcelList = []
    # for item in infoList:
    #     itemList = item.strip().split(',')
    #     if itemList[0] not in dayDic.keys():
    #         dayDic[itemList[0]] = []
    #     dayDic[itemList[0]].append(itemList)
    #     # 总的列表
    #     splitInfoList.append(itemList)
    # print('len day list:' , len(dayDic.keys()))
    # for k,v in dayDic.items():
    #     tradeNumSum = getTradeNumSum(v)
    #     avgTradeNumSum = tradeNumSum / len(v)
    #     tradeMoneySum = getTradeMoneySum(v)
    #     avgTradeMoneySum = tradeMoneySum / len(v)
    #     print(k,len(v),tradeNumSum,avgTradeNumSum,tradeMoneySum,avgTradeMoneySum)
    #     dayOutExcelList.append([k,len(v),tradeNumSum,avgTradeNumSum,tradeMoneySum,avgTradeMoneySum])
    #
    # inout.writeContent2Excel(dayOutExcelList,outputPath + 'day_and_count_num.xls')
    '''
    下面的主要任务是生成一个按照“O”的类别分好类的json文件
    '''
    # # 统计“O”个数，生成升序列表
    # OList = []
    # for itemList in splitInfoList:
    #     if re.search('^O',itemList[1]):
    #         OList.append(itemList[1])
    #     if re.search('^O',itemList[2]):
    #         OList.append(itemList[2])
    # OList = sorted(list(set(OList)))
    # print('O list len:',len(OList))
    # print(OList[:10])
    # # inout.writeContent2Excel(OList, outputPath + 'proxy_list.xls')
    # inout.writeList2Txt(outputPath + 'proxy_list.txt',OList)
    print()
    # 初始化整体分类字典
    fullClassifyDic = OrderedDict()
    OList = inout.readListFromTxt(outputPath + 'proxy_list.txt')
    for Oitem in OList:
        fullClassifyDic[Oitem] = OrderedDict()
        for i in range(1,92):
            fullClassifyDic[Oitem][str(i)] = []
    # 对数据进行分类处理
    for itemList in splitInfoList:
        if re.search('^O',itemList[1]):
            fullClassifyDic[itemList[1]][itemList[0]].append(itemList)
        if re.search('^O',itemList[2]):
            fullClassifyDic[itemList[2]][itemList[0]].append(itemList)
    print('fullClassifyDic key-O len: ',len(fullClassifyDic.keys()))
    print('fullClassifyDic key-day len: ',len(fullClassifyDic['O1001'].keys()))
    print('fullClassifyDic O1001 day1 len: ',len(fullClassifyDic['O1001']['1']))
    print('fullClassifyDic O1001 day1 content: ',fullClassifyDic['O1001']['1'])



