# encoding=utf-8
import twitter


def test_api():
    api = twitter.Api(consumer_key='EKEMZjnkpUu7p8CbICyFKnUfD',
                      consumer_secret='lKnVGbM4V8fTwwBjy7uVwo1IyQBpgUBzB0r9R6wAvUmGaNdBwe',
                      access_token_key='720077099688706048-KYyr0iV9aF5vsBl0yQGrjLB8sXBizmr',
                      access_token_secret='D7kbKR9N1rHdYmtnUa6CdPs9qt1gNy8rEsdAIFBoC4Rhu')

    statuses = api.GetUserTimeline(screen_name='eonline', count='200')
    if len(statuses) >= 200:
        #     进行下一次循环
        pass
    for s in statuses:
        print s


test_api()
