# encoding=utf-8

import getData
import twitter
import saveData

# 初始化Twitter的用户信息
api = twitter.Api(consumer_key='EKEMZjnkpUu7p8CbICyFKnUfD',
                  consumer_secret='lKnVGbM4V8fTwwBjy7uVwo1IyQBpgUBzB0r9R6wAvUmGaNdBwe',
                  access_token_key='720077099688706048-KYyr0iV9aF5vsBl0yQGrjLB8sXBizmr',
                  access_token_secret='D7kbKR9N1rHdYmtnUa6CdPs9qt1gNy8rEsdAIFBoC4Rhu')

# 获取需要爬取的用户数据，元组或列表
data = getData.get_data_from_xls("C:\Users\Cesar\Desktop\data.xls")

# 定义存储路径
folder_path = "F:/twitterData/"


def main():
    for per in data:
        get_statu(per)


def get_statu(screen_name):
    print screen_name + " start crawler"
    statuses = api.GetUserTimeline(screen_name=screen_name, count='200')
    saveData.sava_status_to_xml(statuses, str(folder_path+screen_name+"/"))
    totle = len(statuses)
    max_id = statuses[totle-1].id
    while not totle < 200:
        statuses = api.GetUserTimeline(screen_name=screen_name, count='200', max_id=max_id)
        saveData.sava_status_to_xml(statuses, str(folder_path+screen_name+"/"))
        totle = len(statuses)
        max_id = statuses[totle-1].id
        print "..."
    print screen_name+" complete"

if __name__ == '__main__':
    main()
