# encoding=utf-8

import xlrd
import types

"""该类主要用于原始任务数据的获取，
方法的返回值必须是一个用户Screen Name的列表或元组
"""


def get_data_from_xls(file_path="data.xls"):
    data = xlrd.open_workbook(file_path)
    sheet = data.sheets()[0]
    re = []
    for s in sheet.col_values(1):
        if str(s).startswith("@"):
            s = str(s).replace("@", "")
            re.append(float(str(s).strip()))
    return re


def get_id_from_xls(file_path="data.xls"):
    data = xlrd.open_workbook(file_path)
    sheet = data.sheets()[0]
    re = []
    for s in sheet.col_values(1):
        if type(s) is types.FloatType:
            re.append(int(s))
    return re


# get_data_from_xls("C:\Users\Cesar\Desktop\data.xls")
