import tweepy
import datetime
from textblob import TextBlob
from tweet_store import TweetStore
import json

#file_path = '../config/api.json'

#with open(file_path) as f:
#    twitter_api = json.loads(f.read())

#consumer_key = twitter_api['consumer_key']
#consumer_secret = twitter_api['consumer_secret']
#access_token = twitter_api['access_token']
#access_token_secret = twitter_api['access_token_secret']

consumer_key = 'OXnB5RRPuKzQVCxnrf3qWkBh7'
consumer_secret = 'WuEkWBvQRcAfbFBeUlqPdzQ3NiidKYj936tEMmCGMOeGRiGoS6'
access_token = '198385563-QXMsShRgyfus422srABQEmjk9QwI3EFdBVAmuaOx'
access_token_secret = '2pJAKHlAn4C3NJA3Jp01x5pXiBo5wp6XKdsr0VhXGJlOu'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
store = TweetStore()

class StreamListener(tweepy.StreamListener):

    def on_status(self, status):

        if ('RT @' not in status.text):
            blob = TextBlob(status.text)
            sent = blob.sentiment
            #polarity = sent.polarity
            #subjectivity = sent.subjectivity

            tweet_item = {
                'id_str': status.id_str,
                'text': status.text,
                #'polarity': polarity,
                #'subjectivity': subjectivity,
                'username': status.user.screen_name,
                'name': status.user.name,
                'profile_image_url': status.user.profile_image_url,
                'received_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            store.push(tweet_item)
            print("Pushed to redis:", tweet_item)

    def on_error(self, status_code):
        if status_code == 420:
            return False

stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=["pizza"])
#stream.filter(track=["@MiamiHEAT", "@Timberwolves", "#HEATCulture", "#AllEyesNorth", "#MIAvsMIN", "#HeatCulture", "nba", "lakers",])
