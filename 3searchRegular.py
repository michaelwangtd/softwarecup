#!/usr/bin/env python
# -*- coding:utf-8 -*-

from utils import inout
import index
from collections import OrderedDict
import re



"""
这里所做的工作是探索已有数据之间的规律
"""

def getDicKey(filePath):
    dic = OrderedDict()
    lineList = inout.readListFromTxt(filePath)
    for itemLine in lineList:
        # itemLineList = re.findall('\s+',itemLine)
        itemLineList = itemLine.strip().split('\t')
        if len(itemLineList) == 5:
            tempKey = itemLineList[1] + '_' + itemLineList[2]
            dic[tempKey] = []
    return dic

def relaizeInitDic(initDic,recordList):
    for line in recordList:
        tempKey = line[1] + '_' + line[2]
        if tempKey in initDic.keys():
            initDic[tempKey].append(line)
    return initDic

def getThreeClassList(intList):
    intList = sorted(intList)
    list1 = []
    list2 = []
    list3 = []
    for item in intList:
        if item <31:
            list1.append(str(item))
        elif item < 61:
            list2.append(str(item))
        elif item <91:
            list3.append(str(item))
    return list1,list2,list3


def getCaulList(keyName,keyList):
    indexList = []
    for itemList in keyList:
        indexList.append(int(itemList[0]))
        list1,list2,list3 = getThreeClassList(list(set(indexList)))
    return [keyName,len(keyList),' '.join(list1),' '.join(list2),' '.join(list3)]

def getInitOrderedDic():
    dic = OrderedDict()
    for i in range(1,91):
        dic[i] = []
    return dic


if __name__ == '__main__':

    ## 1 找出O1014代理，将所有信息输出到csv中观察
    # inputFilePath = index.ROOTPATH+'\\data\\searchRegular_01.txt'
    # outputFilePath = index.ROOTPATH+'\\data\\searchRegular_01_result_O1014.xls'
    # resultList = []
    # dic = inout.loadData2Json(inputFilePath)
    # for i in range(1,92):
    #     resultList.extend(dic[0]['O1014'][str(i)])
    # # for i in range(1,92):
    # #     resultList.extend(dic[0]['O6090'][i])
    # print len(resultList)
    # inout.writeContent2Excel(resultList,outputFilePath)

    ## 2 将O1014所有记录按照91天出现过的记录挑选出来
    inputFilePath1 = index.ROOTPATH + '\\data\\searchRegular_01_result_O1014.xls'
    inputFilePath2 = index.ROOTPATH + '\\data\\O1014_record.txt'
    outputFilePath = index.ROOTPATH + '\\data\\classify_all_record_in_day_91_O1014.xls'

    initDic = getDicKey(inputFilePath2)
    recordList = inout.getListFromExcel(inputFilePath1)
    resultDic = relaizeInitDic(initDic,recordList)
    finalList = []
    for k,v in resultDic.items():
        # print k,': ',len(v),'--',v
        print k,': ',len(v)
        for item in v:
            item.append(int(item[4])/int(item[3]))
            finalList.append(item)
    # 将所有记录输出到csv
    # inout.writeContent2Excel(finalList,outputFilePath)


    # ## 3 将O1014所有出现的记录归档到字典中
    # inputFilePath1 = index.ROOTPATH + '\\data\\searchRegular_01_result_O1014.xls'
    # outputFilePath = index.ROOTPATH + '\\data\\classify_all_record_in_O1014_record_len.xls'
    #
    # dic = dict()
    # outputList = []
    # infoList =  inout.getListFromExcel(inputFilePath1)
    # # 按照key类别进行分类处理
    # for lineList in infoList:
    #     tempKey = lineList[1] + '_' + lineList[2]
    #     if tempKey not in dic.keys():
    #         dic[tempKey] = []
    #     dic[tempKey].append(lineList)
    # print len(dic.keys())
    # for k,v in dic.items():
    #     # print k,len(v),'---',v
    #     caulList = getCaulList(k,v)
    #     outputList.append(caulList)
    # inout.writeContent2Excel(outputList,outputFilePath)


    # ## 在每一个代理下，按照天数分类，找出每天交易记录的长度
    # inputFilePath1 = index.ROOTPATH + '\\data\\searchRegular_01_result_O1014.xls'
    # outputFilePath = index.ROOTPATH + '\\data\\classify_all_record_in_O1014_record_len_by_day.xls'
    #
    # infoList = inout.getListFromExcel(inputFilePath1)
    # initDic = getInitOrderedDic()
    # for lineList in infoList:
    #     if int(lineList[0]) in initDic.keys():
    #         initDic[lineList[0]].append(lineList)
    # outputList = []
    # for k,v in initDic.items():
    #     outputList.append([k,len(v)])
    # inout.writeContent2Excel(outputList,outputFilePath)


