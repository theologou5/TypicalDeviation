import time
import tweepy
from tweepy import OAuthHandler

consumer_key = 'AarU4x3nAGhKGWpDJXXUvQ7MT'
consumer_secret = '7sIhYgGO9elNJLpo9WhpHZBCHMedVYx0hrbVii4trHJyTMMRWr'
access_token = '2212480195-53JWT5tg1Mn2pY76kga5QcDVGvKbcZD5Uh4FkH1'
access_secret = '81cFXqWszsj0z0c7LkQ4mqraQ4ja73l7bYiPhjzDV8BYS'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

twittername1=raw_input('Give the first twitter name: ')
twittername2=raw_input('Give the second twitter name: ')

twitteruser1=[]
page1=0
for page in tweepy.Cursor(api.followers_ids,id=twittername1,count=5000).pages():
    if (tweepy.TweepError):
        time.sleep(60)
        page1+= 1
        twitteruser1.extend(page)
    else:
        page1+= 1
        twitteruser1.extend(page)
twitteruser2=[]
page2=0
for page in tweepy.Cursor(api.followers,id=twittername2,count=5000).pages():
    if (tweepy.TweepError):
        time.sleep(60)
        page2+= 1
        twitteruser2.extend(page)
    else:
        page2+= 1
        twitteruser2.extend(page)
if list(set(twitteruser1).intersection(twitteruser2))==[]:
    print "there are no common followers"
else:
    CommonFollowers=[]
    CommonFollowers.extend(set(twitteruser1).intersection(twitteruser2))
    for i in CommonFollowers:
        print CommonFollowers[i]
