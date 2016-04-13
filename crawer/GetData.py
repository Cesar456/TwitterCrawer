# encoding=utf-8

import xlrd

"""该类主要用于原始任务数据的获取，
方法的返回值必须是一个用户Screen Name的列表或元组
"""


def get_data_from_xls(filepath="data.xls"):
    data = xlrd.open_workbook(filepath)
    sheet = data.sheets()[0]
    re = []
    for s in sheet.col_values(1):
        if s.startswith("@"):
            s = s.replace("@", "")
            re.append(s)
    return re


# get_data_from_xls("C:\Users\Cesar\Desktop\data.xls")
