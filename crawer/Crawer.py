# encoding=utf-8

import getData
import twitter
import saveData
import time

# 初始化Twitter的用户信息
api = twitter.Api(consumer_key='EKEMZjnkpUu7p8CbICyFKnUfD',
                  consumer_secret='lKnVGbM4V8fTwwBjy7uVwo1IyQBpgUBzB0r9R6wAvUmGaNdBwe',
                  access_token_key='720077099688706048-KYyr0iV9aF5vsBl0yQGrjLB8sXBizmr',
                  access_token_secret='D7kbKR9N1rHdYmtnUa6CdPs9qt1gNy8rEsdAIFBoC4Rhu')

# 获取需要爬取的用户数据，元组或列表
data = getData.get_id_from_xls("C:\Users\Cesar\Desktop\data.xls")

# 定义存储路径
folder_path = "F:/twitterData/"


def main():
    for per in data:
        get_status_by_id(per)


def get_status_by_id(user_id):
    print str(user_id) + " start crawler"
    statuses = api.GetUserTimeline(user_id=user_id, count='200')
    saveData.sava_status_to_xml(statuses, str(folder_path + str(user_id) + "/"))
    totle = len(statuses)
    if totle == 0:
        print str(user_id)+'无数据'
        return
    max_id = statuses[totle - 1].id
    while not totle < 10:
        time.sleep(2)
        statuses = api.GetUserTimeline(user_id=user_id, count='200', max_id=max_id)
        saveData.sava_status_to_xml(statuses, str(folder_path + str(user_id) + "/"))
        totle = len(statuses)
        if totle == 0:
            print str(user_id)+'完毕'
            return
        max_id = statuses[totle - 1].id
        print "..."
    print str(user_id) + " complete"


def get_status(screen_name):
    print screen_name + " start crawler"
    statuses = api.GetUserTimeline(screen_name=screen_name, count='200')
    saveData.sava_status_to_xml(statuses, str(folder_path + screen_name + "/"))
    totle = len(statuses)
    if totle == 0:
        return
    max_id = statuses[totle - 1].id
    while not totle < 100:
        statuses = api.GetUserTimeline(screen_name=screen_name, count='200', max_id=max_id)
        saveData.sava_status_to_xml(statuses, str(folder_path + screen_name + "/"))
        totle = len(statuses)
        if totle == 0:
            return
        max_id = statuses[totle - 1].id
        print "..."
        time.sleep(5)
    print screen_name + " complete"


if __name__ == '__main__':
    main()
