from textblob import TextBlob
import tweepy

auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
auth_handler.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth_handler)

# Keywords
keyword = 'tweepy'#input("Please enter a keyword or hashtag:")
nrOfTweets = 10 #input("Please enter how many tweets to analyze:")


def check_int(nrOfTweets):
    try:
        val = int(nrOfTweets)
    except ValueError:
        print("This is not a number")


check_int(nrOfTweets)

tweets = tweepy.Cursor(api.search_tweets(q=keyword, lang = 'en' , count = nrOfTweets))

for tweet in tweets:
    print(tweet.text)