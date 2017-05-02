# !/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas
from utils import inout
from utils import util
from collections import OrderedDict
import re
import index
import codecs
import json


start = 0.0
re = int(start)
print re

# name = '家'

# testPath = index.ROOTPATH+'\\test_json.txt'
# testList = [['哈哈'],['嘻嘻'],['呵呵'],name]
# fw = codecs.open(testPath,'wb')
# fw.write(json.dumps(testList,ensure_ascii=False))
# fw.close()
# fr = codecs.open(testPath,'rb')
# line = fr.readline()
# re = json.loads(line)
# print re
# print re[0][0]
# fr.close()



# re = inout.loadData2Json(index.ROOTPATH+'\\data\\proxy_json.txt')
# print re[0]



# testStr = 'O1084'
# if re.search('^O',testStr):
#     print(testStr)

# testList = ['O1001', 'O1007', 'O1011', 'O1039', 'O1043', 'O1050', 'O1069', 'O107', 'O1073', 'O1079']
# print(sorted(testList))

# print index.ROOTPATH


# testPath = index.ROOTPATH+'\\test_code.txt'
# """
#     1 codecs utf8 + unicode编码解决文件读写
# """
# # fw = codecs.open(testPath,'a',encoding='utf-8')
# # content = u'哈哈哈哈，小buffer,code'  # 表示unicode编码
# # fw.write(content)
# # fw.close()
# # fr = codecs.open(testPath,'r',encoding='utf-8')
# # content = fr.readline()
# # print type(content),content #读进来的编码为unicode编码
# # fr.close()
# """
#     2 utf8 byte string + b二进制io
# """
# fw = codecs.open(testPath,'ab')     # 以'ab'二进制追加写
# content = '哈哈啊jkj'  # 类型为“str”
# con2 = u'jsjf贾师傅'.encode('utf-8') # 编码为byte string
# fw.write(content)
# fw.write(con2)
# fw.close()
# fr = codecs.open(testPath,'rb')
# content = fr.readline()
# con2 = fr.readline()
# print type(content),content
# print type(con2),con2
# re1 = content.decode('utf-8')
# print type(re1)


