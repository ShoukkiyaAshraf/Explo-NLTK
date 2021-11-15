# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 14:54:19 2021

@author: Shoukkiya Ashraf
"""
import nltk
import numpy as np
import string
import random

f = open('chatbot.txt','r',errors='ignore')

raw = f.read().lower()

# nltk.download('punkt')
# nltk.download('wordnet')

sent_tokens = nltk.sent_tokenize(raw) #converts to lines/sentences
word_tokens = nltk.word_tokenize(raw) #convets to words


