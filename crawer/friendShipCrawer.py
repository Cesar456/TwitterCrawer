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
data = GetData.get_data_from_xls("H:\\TWITTER\\IOT.xls")
# 用户数据存储文件夹
folder_path = "H:\\TWITTER\\friendship\\"


def get_following():
    for screen_name in data:
        print screen_name
        followers = api.GetFriends(screen_name=screen_name)
        print len(followers)
        SaveData.sava_user_to_xml(users=followers, folder_path=folder_path + "followering/" + screen_name + "/")
        time.sleep(60)


def get_following_id_by_name():
    id_ = 1
    for screen_name in data:
        try:
            print "序号：" + str(id_) + "  userName：" + str(screen_name)
            id_ += 1
            followers = api.GetFriendIDs(screen_name=screen_name)
            print "用户数据获取成功正在存储"
            SaveData.sava_user_id_to_txt(users=followers, folder_path=folder_path + str(screen_name) + "/")
            print "用户数据已存储"
            time.sleep(200)
        except Exception, e:
            print e
            print str(screen_name) + "  无法获得"


def get_following_id():
    id_ = 1
    for uid in data:
        try:
            print "序号：" + str(id_) + "  userID：" + str(uid)
            id_ += 1
            followers = api.GetFriendIDs(user_id=uid)
            print "用户数据获取成功正在存储"
            SaveData.sava_user_id_to_txt(users=followers, folder_path=folder_path + str(uid) + "/")
            print "用户数据已存储"
            time.sleep(100)
        except Exception, e:
            print e
            print str(uid) + "  无法获得"


if __name__ == '__main__':
    get_following_id_by_name()
