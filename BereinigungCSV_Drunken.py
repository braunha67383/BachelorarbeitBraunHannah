import csv
import re

#@author: Hannah Braun
#Die von Tweepy gesammelten Tweets müssen bereinigt werden, um Fehler zu vermeiden

#csv-Datei "tweetsDrunken" mit den Tweets wird geöffnet und in utf-8 umgewandelt
#csv-Datei "CleanedTweetsDrunken" als Speicherort wird geöffnet
in_file = open("tweetsDrunken.csv", "rt", errors="ignore", encoding="utf-8")
reader = csv.reader(in_file)
out_file = open("CleanedTweetsDrunken.csv", "wt", errors="ignore")
writer = csv.writer(out_file)

#Jeder Tweet wird einzeln reihenweise aufgerufen und bereinigt
#Gesuchte Wörter, Links, Verlinkungen anderer Personen und # werden entfernt
for row in reader:
        newrow = [re.sub(r"(https)\S+|(@)\S+|drunken|Drunken|DRUNKEN|Drunk|drunk|DRUNK|Alcohol|alcohol|ALCOHOL|#", "", s) for s in row]
        writer.writerow(newrow)

#Files werden geschlossen
in_file.close()
out_file.close()