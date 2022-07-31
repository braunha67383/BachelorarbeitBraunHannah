import tweepy
import config
import pandas as pd

#@author: Hannah Braun
#Tweepy verbindet sich mit den Keys mit dem Twitteraccount
client = tweepy.Client(bearer_token=config.bearer_token)

#Festlegung der Begriffe, die nicht in dem Tweet vorkommen sollen; Deutsch als Sprache wird eingestellt
query = '(-drunk, -alcohol, -drunken) lang:de'

#csv-Datei wird erstellt
file_name = 'tweetsSorber.csv'

#"Tweet" als Spalte wird benannt
#Tweets werden gesucht, max. Anzahl der Tweets wird festgelegt
columns = ['Tweet']
data = []
for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=100).flatten(limit=20000):
    data.append([tweet.text])

#Daten werden in "tweetsSorber" gespeichert
df = pd.DataFrame(data, columns=columns)
df.to_csv('tweetsSorber.csv', mode='a', index=False, header=False)
