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
data = getData.get_data_from_xls("C:\Users\Cesar\Desktop\data.xls")
# 用户数据存储文件夹
folder_path = "F:/user/"


def get_following():
    for screen_name in data:
        print screen_name
        followers = api.GetFriends(screen_name=screen_name)
        print len(followers)
        saveData.sava_user_to_xml(users=followers, folder_path=folder_path + "followering/" + screen_name + "/")
        time.sleep(120)


def get_following_id():
    id = 1
    for screen_name in data:
        print str(id) + screen_name
        id += 1
        followers = api.GetFriendIDs(screen_name=screen_name)
        saveData.sava_user_id_to_txt(users=followers, folder_path=folder_path + "followering_id/" + screen_name + "/")
        time.sleep(60)

get_following_id()
