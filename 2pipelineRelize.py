#! /usr/bin/env python
# -*- coding:utf-8 -*-

import index
import codecs
from utils import inout
import re
from collections import OrderedDict
import math

def getThreeSample(originPath):
    resultList = []
    fr = codecs.open(originPath,'rb')
    while(True):
        line = fr.readline().strip()
        if line:
            lineList = line.split(',')
            if str(lineList[0]) in ['1','31','61']:
                resultList.append(lineList)
        else:
            break
    return resultList


def getClassifiedSampleDic(sampleList):
    dic = dict()
    for item in sampleList:
        key = item[1]+'-'+item[2]
        if key not in dic.keys():
            # print key
            dic[key] = []
        dic[key].append(item)
    return dic


def getOSetList(sampleList):
    resultList = []
    for item in sampleList:
        if re.search('^O',item[1]):
            resultList.append(item[1])
        if re.search('^O',item[2]):
            resultList.append(item[2])
    return sorted(list(set(resultList)))


def classifySampleList2OSetDic(sampleList,OSetList):
    dic = OrderedDict()
    for item in OSetList:
        dic[item] = []
    for itemList in sampleList:
        if re.search('^O',itemList[1]):
            dic[itemList[1]].append(itemList)
        if re.search('^O',itemList[2]):
            dic[itemList[2]].append(itemList)
    return dic


def write2Json(threeSampleClassifiedPath,OSetDic):
    fw = open(threeSampleClassifiedPath,'wb')
    for k,v in OSetDic.items():
        outputLine = str(k)+','+str(len(v))+','+str(v).replace(',','-')
        fw.write(outputLine+'\n')
    fw.close()


def getOneSample(originPath,dayNum):
    resultList = []
    fr = codecs.open(originPath,'rb')
    while(True):
        line = fr.readline().strip()
        if line:
            lineList = line.split(',')
            if str(lineList[0]) in [str(dayNum)]:
                resultList.append(lineList)
        else:
            break
    return resultList


def getOSetDicValueLengthList(OSetDic):
    reList = []
    for k,v in OSetDic.items():
        reList.append(len(v))
    reList = sorted(reList)
    return reList


if __name__ == '__main__':
    originPath = index.ROOTPATH+'\\data\\sales_sample_20170310.csv'
    threeSamplePath = index.ROOTPATH+'\\data\\threeSample.txt'
    threeSampleClassifiedPath = index.ROOTPATH+'\\data\\threeSampleClassified.txt'

    # 1 筛选出three sample
    # threeSampleSetList = getThreeSample(originPath)
    # inout.writeList2Txt(threeSamplePath,threeSampleSetList)

    '''对样本按照“A-B关系”进行分类
        总共有17万，分类结果为11万，分的类太小，不适合统计，换一种方式
    '''
    # sampleList = inout.readListFromTxt(threeSamplePath)
    # sampleList = inout.liststr2listlist(sampleList)
    # print len(sampleList)
    # print '数据已加载...'
    # classifiedDic = getClassifiedSampleDic(sampleList)
    # print len(classifiedDic.keys())
    # print classifiedDic.keys()

    # 2 找出three sample中出现的过的“O”，并排序形成列表
    sampleList = inout.readListFromTxt(threeSamplePath)
    sampleList = inout.liststr2listlist(sampleList)
    OSetList = getOSetList(sampleList)
    print len(OSetList)
    # # 将sampleList分类到OSetList对应的数据
    OSetDic = classifySampleList2OSetDic(sampleList,OSetList)
    print len(OSetDic.keys())
    # write2Json(threeSampleClassifiedPath,OSetDic)
    # 获得OSetDic里面v长度排序的列表
    vlenList = getOSetDicValueLengthList(OSetDic)
    print len(vlenList)
    print vlenList[int(math.floor(len(vlenList)*0.88))]

    # 找出91天的数据
    # oneSampleList = getOneSample(originPath,91)
    # print len(oneSampleList)
    # day91_OSetList=  getOSetList(oneSampleList)
    # print len(day91_OSetList)




