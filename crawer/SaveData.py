# encoding=utf-8

import xmltodict
import json
from os import path
from os import mkdir
import time

"""
该类主要是对爬取的数据进行存储
传入的是一个用户状态的列表，每一个列表都包含数条
以json格式存储的数据:但是json格式数据有个问题就是
\"无法存储，必须转化为\\\"才可以存储
"""


def sava_status_to_xml(status=[], folder_path="F:/twitterData/unknow/"):
    """
    :param status: 用户状态
    :type folder_path: str
    传入为该批数据存储的文件夹路径，为绝对路径+twitter用户名的形式
    """

    if len(status) == 0:
        print "no data exception"
        return
    if not folder_path.endswith("/"):
        folder_path += "/"

    dic_re = {}
    for s in status:
        json_str = str(s).replace(r"\"", r"\\\"")
        dic_re[str(s.id)] = json.loads(json_str)
    result = {"status": dic_re}
    xml_re = unicode(xmltodict.unparse(result))

    file_path = folder_path + str(time.time()) + ".xml"
    if not path.exists(folder_path):
        mkdir(folder_path)
    file_re = open(file_path, "w")
    file_re.write(xml_re.encode("utf-8"))
    file_re.close()


def sava_status_to_json(status=[], folder_path="F:/twitterData/unknow/"):
    """
    :param status: 用户状态
    :type folder_path: str
    传入为该批数据存储的文件夹路径，为绝对路径+twitter用户名的形式
    """

    if len(status) == 0:
        print "no data exception"
        return
    if not folder_path.endswith("/"):
        folder_path += "/"

    result = unicode(str(status))
    file_path = folder_path + str(time.time()) + ".txt"

    if not path.exists(folder_path):
        mkdir(folder_path)
    file_re = open(file_path, "w")
    file_re.write(result.encode("utf-8"))
    file_re.close()
