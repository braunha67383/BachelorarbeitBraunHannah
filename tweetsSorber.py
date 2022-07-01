import tweepy
import config
import pandas as pd

client = tweepy.Client(bearer_token=config.bearer_token)

query = '(-drunk, -alcohol, -drunken) lang:de'

file_name = 'tweetsSorber.csv'

columns = ['Tweet']
data = []
for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=100).flatten(limit=10000):
    data.append([tweet.text])

df = pd.DataFrame(data, columns=columns)
df.to_csv('tweetsSorber.csv', mode='a', index=False, header=False)