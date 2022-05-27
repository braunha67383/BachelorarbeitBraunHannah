import tweepy
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']
bearer_token = config['twitter']['bearer_token']
print(bearer_token)

#authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
try:
    api.verify_credentials()
    print("success")
except:
    print("failed")

public_tweets = api.home_timeline()

for public_tweet in public_tweets:
    print(public_tweet)