# -*- coding: utf-8 -*-
"""
Created on Sun May 24 16:11:56 2020

@author: mohit
"""


import numpy as np
import pandas as pd
import nltk
nltk.download('punkt')
import re
#df = pd.read_csv("tennis_articles_v4.csv")
#print(df.head())
#print(df['article_text'][1])
from nltk.tokenize import sent_tokenize
#df = open("text.txt",encoding = 'utf-8')

#sentences = []
#for s in df:
#  sentences.append(sent_tokenize(s))
df = "It cannot be denied that the COVID-19 pandemic has caused some serious losses to many industries across the world, but in return, it has taught us new ways of living. As the crisis began to unfold and tighten its grip, global conglomerates adopted new methods of working such as ‘work from home’, wherever possible, to accomplish routine office tasks. The trend soon caught up and today, a large chunk of the global workforce, especially in the corporate and IT sector, is working from remote location.Remote working has its pros and cons. Data suggests that 12% remote workers experience distractions at home, 20% find communicating and collaborating a challenge, while 18% report not being able to unplug. On the other hand, some pros of this system include saving money and time spent on commuting, better work-life balance, working right from your comfort zone and more.Despite being the need of the hour, most of the companies do not have adequate infrastructure to implement a work from home"
sentences = df.split(".")
#sentences = [y for x in sentences for y in x] 
'''
df = open("text.txt",encoding = 'utf-8')

sentence = []

for s in df:
  sentence.append(sent_tokenize(s))
#df = "It cannot be denied that the COVID-19 pandemic has caused some serious losses to many industries across the world, but in return, it has taught us new ways of living. As the crisis began to unfold and tighten its grip, global conglomerates adopted new methods of working such as ‘work from home’, wherever possible, to accomplish routine office tasks. The trend soon caught up and today, a large chunk of the global workforce, especially in the corporate and IT sector, is working from remote location.Remote working has its pros and cons. Data suggests that 12% remote workers experience distractions at home, 20% find communicating and collaborating a challenge, while 18% report not being able to unplug. On the other hand, some pros of this system include saving money and time spent on commuting, better work-life balance, working right from your comfort zone and more.Despite being the need of the hour, most of the companies do not have adequate infrastructure to implement a work from home"
#sentences = df.split(".")
sentences = []
for i in sentence:
    for j in i:
        sentences.append(j)'''
word_embeddings = {}
f = open('glove.6B.100d.txt', encoding='utf-8')
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    word_embeddings[word] = coefs
f.close()
print(len(word_embeddings))

clean_sentences = pd.Series(sentences).str.replace("[^a-zA-Z]", " ")
clean_sentences = [s.lower() for s in clean_sentences]

nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

def remove_stopwords(sen):
    sen_new = " ".join([i for i in sen if i not in stop_words])
    return sen_new
clean_sentences = [remove_stopwords(r.split()) for r in clean_sentences]

sentence_vectors = []
for i in clean_sentences:
  if len(i) != 0:
    v = sum([word_embeddings.get(w, np.zeros((100,))) for w in i.split()])/(len(i.split())+0.001)
  else:
    v = np.zeros((100,))
  sentence_vectors.append(v)

sim_mat = np.zeros([len(sentences), len(sentences)])
from sklearn.metrics.pairwise import cosine_similarity
for i in range(len(sentences)):
  for j in range(len(sentences)):
    if i != j:
      sim_mat[i][j] = cosine_similarity(sentence_vectors[i].reshape(1,100), sentence_vectors[j].reshape(1,100))[0,0]
import networkx as nx

nx_graph = nx.from_numpy_array(sim_mat)
scores = nx.pagerank(nx_graph)
ranked_sentences = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)
for i in range(5):
  print(ranked_sentences[i][1])
  