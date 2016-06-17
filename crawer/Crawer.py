# encoding=utf-8

import GetData
import twitter
import SaveData
import time

# 初始化Twitter的用户信息
api = twitter.Api(consumer_key='EKEMZjnkpUu7p8CbICyFKnUfD',
                  consumer_secret='lKnVGbM4V8fTwwBjy7uVwo1IyQBpgUBzB0r9R6wAvUmGaNdBwe',
                  access_token_key='720077099688706048-KYyr0iV9aF5vsBl0yQGrjLB8sXBizmr',
                  access_token_secret='D7kbKR9N1rHdYmtnUa6CdPs9qt1gNy8rEsdAIFBoC4Rhu')

# 获取需要爬取的用户数据，元组或列表
data = GetData.get_data_from_xls("F:\data52.xls")

# 定义存储路径
folder_path = "F:/twitter_52/"

"""
err_log 记载出错的账户名称
right_log记载正确账户名称
id_log 记载截至程序停止为止当前最大ID，启动程序时需要更新
"""
err_log = open("F:/err_log.txt", 'a')
right_log = open("F:/right_log.txt", 'a')
id_log = open("F:/id_log.txt", 'w')

maxID = 999999999999999999


def main():
    for per in data:
        try:
            get_status(per)
            global maxID
            maxID = 999999999999999999
            right_log.writelines(str(per) + '\n')
        except Exception, e:
            err_log.writelines(str(per) + '\n')
            print e


def get_status_by_id(user_id):
    print str(user_id) + " start crawler"
    statuses = api.GetUserTimeline(user_id=user_id, count='200', max_id=maxID)
    SaveData.sava_status_to_xml(statuses, str(folder_path + str(user_id) + "/"))
    totle = len(statuses)
    if totle == 0:
        print str(user_id) + '无数据'
        return
    max_id = statuses[totle - 1].id
    while not totle < 10:
        id_log.writelines(str(max_id) + "\n")
        id_log.flush()
        time.sleep(10)
        statuses = api.GetUserTimeline(user_id=user_id, count='200', max_id=max_id)
        SaveData.sava_status_to_xml(statuses, str(folder_path + str(user_id) + "/"))
        totle = len(statuses)
        if totle == 0:
            print str(user_id) + '完毕'
            return
        max_id = statuses[totle - 1].id
        print "..."
    print str(user_id) + " complete"


def get_status(screen_name):
    print screen_name + " start crawler"
    statuses = api.GetUserTimeline(screen_name=screen_name, count='200', max_id=maxID)
    SaveData.sava_status_to_xml(statuses, str(folder_path + screen_name + "/"))
    totle = len(statuses)
    if totle == 0:
        print str(screen_name) + '无数据'
        return
    max_id = statuses[totle - 1].id
    while not totle < 10:
        id_log.writelines(str(max_id) + "\n")
        id_log.flush()
        time.sleep(10)
        statuses = api.GetUserTimeline(screen_name=screen_name, count='200', max_id=max_id)
        SaveData.sava_status_to_xml(statuses, str(folder_path + screen_name + "/"))
        totle = len(statuses)
        if totle == 0:
            print str(screen_name) + '完毕'
            return
        max_id = statuses[totle - 1].id
        print "..."
    print screen_name + " complete"


if __name__ == '__main__':
    main()
