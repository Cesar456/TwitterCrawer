# encoding=utf-8
import twitter
import json
import xmltodict

def test_api():
    api = twitter.Api(consumer_key='EKEMZjnkpUu7p8CbICyFKnUfD',
                      consumer_secret='lKnVGbM4V8fTwwBjy7uVwo1IyQBpgUBzB0r9R6wAvUmGaNdBwe',
                      access_token_key='720077099688706048-KYyr0iV9aF5vsBl0yQGrjLB8sXBizmr',
                      access_token_secret='D7kbKR9N1rHdYmtnUa6CdPs9qt1gNy8rEsdAIFBoC4Rhu')

    statuses = api.GetUserTimeline(screen_name='eonline', count='200')

test_api()
