import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
import torch
import transformers as ppb
from sklearn.dummy import DummyClassifier

#@author: Hannah Braun
#Training und Testing der AI

#tsv-Datei wird geöffnet
df = pd.read_csv('CleanedTweets.tsv', delimiter='\t', header=None)

#maximale Anzahl der verwendeten Daten wird festgelegt
batch_1 = df[:1000]
print(batch_1[1].value_counts())

#Vortrainiertes Model/Tokenizer wird geladen
model_class, tokenizer_class, pretrained_weights = (ppb.BertModel, ppb.BertTokenizer, 'bert-base-uncased')
tokenizer = tokenizer_class.from_pretrained(pretrained_weights)
model = model_class.from_pretrained(pretrained_weights)

#Tokenizer
tokenized = batch_1[0].apply((lambda x: tokenizer.encode(x, add_special_tokens=True)))

#Padding
max_len = 0
for i in tokenized.values:
    if len(i) > max_len:
        max_len = len(i)

padded = np.array([i + [0] * (max_len - len(i)) for i in tokenized.values])

#Masking
attention_mask = np.where(padded != 0, 1, 0)

#Start Deep-Learning
input_ids = torch.tensor(padded)
attention_mask = torch.tensor(attention_mask)

with torch.no_grad():
    last_hidden_states = model(input_ids, attention_mask=attention_mask)

#bert.pkl befindet sich auf Google-Drive, falls der Code ausgeführt werden soll, bitte diesen herunterladen und in Project einfügen https://drive.google.com/file/d/1sGmyJUhaxRXrRtwoCFntZtidjZikVleA/view?usp=sharing

#Modell speichern
#torch.save(last_hidden_states, 'bert.pkl')

#Modell laden
#last_hidden_states = torch.load('bert.pkl')

#Auswahl Daten, die weiterverarbeitet werden
features = last_hidden_states[0][:, 0, :].numpy()

#Aufteilung Training-/Testdaten
labels = batch_1[1]
train_features, test_features, train_labels, test_labels = train_test_split(features, labels)

#Training des Modells
lr_clf = LogisticRegression()
lr_clf.fit(train_features, train_labels)

#classifier.pkl befindet sich auf Google-Drive, falls der Code ausgeführt werden soll, bitte diesen herunterladen und in Project einfügen https://drive.google.com/file/d/1sGmyJUhaxRXrRtwoCFntZtidjZikVleA/view?usp=sharing

#Modell speichern
#torch.save(lr_clf, 'classifier.pkl')

#Modell laden
#lr_clf = torch.load('classifier.pkl')

#Auswertung
#Genauigkeit AI
print(lr_clf.score(test_features, test_labels))

#Vergleich mit einem Dummy-Klassifikator
clf = DummyClassifier()
scores = cross_val_score(clf, train_features, train_labels)
print("Dummy classifier score: %0.3f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
