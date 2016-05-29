# encoding=utf-8
import twitter, SaveData
import time

# 初始化Twitter的用户信息
api = twitter.Api(consumer_key='EKEMZjnkpUu7p8CbICyFKnUfD',
                  consumer_secret='lKnVGbM4V8fTwwBjy7uVwo1IyQBpgUBzB0r9R6wAvUmGaNdBwe',
                  access_token_key='720077099688706048-KYyr0iV9aF5vsBl0yQGrjLB8sXBizmr',
                  access_token_secret='D7kbKR9N1rHdYmtnUa6CdPs9qt1gNy8rEsdAIFBoC4Rhu')

# 定义存储路径
folder_path = "F:/twitter_mine/"

status = []


def get_time_line():
    print "start"
    statuses = api.GetHomeTimeline(count=200)
    SaveData.sava_status_to_xml(statuses, str(folder_path + "/"))
    totle = len(statuses)
    if (totle > 0):
        since_id = statuses[0].id
    else:
        print "你没有关注任何用户或没有任何用户发表微博"
    statuses = []
    i = 0
    try:
        while True:
            time.sleep(10)
            print str(i) + " 次刷新..."
            i += 1
            # 刷出新的微博
            new_statues = api.GetHomeTimeline(count=200, since_id=since_id)
            print "本次共刷出" + str(len(new_statues)) + "条微博"
            if len(new_statues) < 30:
                print "刷出微博过少，休息十分钟"
                time.sleep(600)
            if not len(new_statues) > 0:
                continue
            since_id = new_statues[0].id
            statuses.extend(new_statues)
            if len(statuses) > 200:
                SaveData.sava_status_to_xml(statuses, str(folder_path + "/"))
                statuses = []
    except Exception, e:
        print e
        SaveData.sava_status_to_xml(statuses, str(folder_path + "/"))


if __name__ == '__main__':
    get_time_line()
