#!/anaconda/bin/python

import oauth2 as oauth
import getTokens as gt
import psycopg2
import psycopg2.extras as e
from utils import *
import tweepy
from random import randint

ck = gt.consumer_key()
cs = gt.consumer_secret()
ak = gt.access_key()
acs = gt.access_secret()
consumer = oauth.Consumer(key=ck, secret=cs)
access_token = oauth.Token(key=ak, secret=acs)
client = oauth.Client(consumer, access_token)

auth = tweepy.OAuthHandler(ck,cs)
auth.set_access_token(ak,acs)
api = tweepy.API(auth)


try:
    con=psycopg2.connect(dbname='twitter', password='password',user='postgres')
except:
    print "I am unable to connect to the database"


curCount = con.cursor()
curVideoDetails = con.cursor(cursor_factory=e.DictCursor)
curCount.execute('select count(*) as count from youtube_videos')
videoCount = curCount.fetchall()

print videoCount

randomNumber = randint(1,int(videoCount[0][0]))

print randomNumber

getVideoDetailsSQL = 'select title, url, twitter_hashtags from youtube_videos where id = ' + str(randomNumber)
curVideoDetails.execute(getVideoDetailsSQL)
videoDetails=curVideoDetails.fetchall()

print videoDetails

tweetString = videoDetails[0]["title"]+' '+videoDetails[0]["url"]+' '+videoDetails[0]["twitter_hashtags"]+' #tweetbot'

print tweetString


api.update_status(tweetString)















