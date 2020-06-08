# -*- coding: utf-8 -*-
"""
Created on Fri May 29 11:41:05 2020

@author: mohit
"""
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
df = open("text.txt",encoding = 'utf-8')

sentence = []

for s in df:
  sentence.append(sent_tokenize(s))
#df = "It cannot be denied that the COVID-19 pandemic has caused some serious losses to many industries across the world, but in return, it has taught us new ways of living. As the crisis began to unfold and tighten its grip, global conglomerates adopted new methods of working such as ‘work from home’, wherever possible, to accomplish routine office tasks. The trend soon caught up and today, a large chunk of the global workforce, especially in the corporate and IT sector, is working from remote location.Remote working has its pros and cons. Data suggests that 12% remote workers experience distractions at home, 20% find communicating and collaborating a challenge, while 18% report not being able to unplug. On the other hand, some pros of this system include saving money and time spent on commuting, better work-life balance, working right from your comfort zone and more.Despite being the need of the hour, most of the companies do not have adequate infrastructure to implement a work from home"
#sentences = df.split(".")
sentences = []
for i in sentence:
    for j in i:
        sentences.append(j)
print("Hello World")
print("Modifying")
print("changing")
print("changing 1")
    


    