# encoding=utf-8

import twitter, GetData
import time

# 初始化Twitter的用户信息
api = twitter.Api(consumer_key='EKEMZjnkpUu7p8CbICyFKnUfD',
                  consumer_secret='lKnVGbM4V8fTwwBjy7uVwo1IyQBpgUBzB0r9R6wAvUmGaNdBwe',
                  access_token_key='720077099688706048-KYyr0iV9aF5vsBl0yQGrjLB8sXBizmr',
                  access_token_secret='D7kbKR9N1rHdYmtnUa6CdPs9qt1gNy8rEsdAIFBoC4Rhu')

# 获取需要爬取的用户数据，元组或列表
data = GetData.get_id_from_xls("F:\\0722\\twitter-52-following-id.xls")

# 定义存储路径
folder_path = ""


def follow_by_id():
    i = 0
    for a in data:
        try:
            api.CreateFriendship(user_id=a, follow=True)
            print str(i) + "  " + str(a) + "已经关注"
            time.sleep(5)
        except Exception, e:
            print e
            print str(i) + "  " + str(a) + "关注失败"
        # for ti in xrange(5):
        #     try:
        #         api.CreateFriendship(user_id=a, follow=True)
        #         print str(i) + "  " + str(a) + "已经关注"
        #         time.sleep(10)
        #         break
        #     except Exception, e:
        #         print e
        #         print str(i) + "  " + str(a) + "关注失败"
        #         time.sleep(10)
        i += 1


# 根据配置文件中的内容
# 找出screenname
# 然后使用该账号去关注这个screnname
def follow():
    i = 0
    for a in data:
        try:
            api.CreateFriendship(screen_name=a, follow=True)
            print str(i) + "  " + a + "已经关注"
            time.sleep(5)
        except Exception, e:
            print e
            print str(i) + "  " + a + "关注失败"
        i += 1


if __name__ == '__main__':
    follow_by_id()
    pass
