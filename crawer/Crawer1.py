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
data = GetData.get_data_from_xls("F:\\6000\\6000\\6000.xls")

# 定义存储路径
folder_path = "F:\\6000\\6000\\6000-0901\\"


def main():
    for per in data:
        try:
            get_status_by_id(per)
        except Exception, e:
            print e


def get_status(screen_name):
    print screen_name + " start crawler"
    statuses = api.GetUserTimeline(screen_name=screen_name, count=200)
    SaveData.sava_status_to_xml(statuses, str(folder_path + screen_name + "/"))
    totle = len(statuses)
    if totle < 100:
        pass
    else:
        print "..."
        max_id = statuses[totle - 1].id
        statuses = api.GetUserTimeline(screen_name=screen_name, count=200, max_id=max_id)
        SaveData.sava_status_to_xml(statuses, str(folder_path + screen_name + "/"))
    time.sleep(10)
    print screen_name + " complete"


def get_status_by_id(id_):
    print str(id_) + " start crawler"
    statuses = api.GetUserTimeline(user_id=id_, count=200)
    SaveData.sava_status_to_xml(statuses, str(folder_path + str(id_) + "/"))
    totle = len(statuses)
    if totle < 100:
        pass
    else:
        print "..."
        max_id = statuses[totle - 1].id
        statuses = api.GetUserTimeline(user_id=id_, count=200, max_id=max_id)
        SaveData.sava_status_to_xml(statuses, str(folder_path + str(id_) + "/"))
    time.sleep(10)
    print str(id_) + " complete"


if __name__ == '__main__':
    main()
