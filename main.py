from textblob import TextBlob
import tweepy
import sys

#Auth
api_key = 'FMKyMEo9O9kG9nk7VHfGR1pli'
api_key_secret = 'oNKdRioupeAJRYlH3fMUihjB8lgfYiVEyyNceHJAYKeDPtLJ9b'
access_token = '1294624994287329280-0MlJBIGchblHVG266yiTpPTyVU2D0t'
access_token_secret = 'zy75xUANL4w8UBqV939HrvGqMFwmy03oOn6FLcUA91OS2'

auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
auth_handler.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth_handler)

#Keywords
keyword = input("Please enter a keyword or hashtag:")
nrOfTweets = input("Please enter how many tweets to analyze:")

def check_int(nrOfTweets):
    try:
        val = int(nrOfTweets)
    except ValueError:
        print("nope")

check_int(nrOfTweets)
#def percentage
 #   return 100 * float(part)/float(whole)


