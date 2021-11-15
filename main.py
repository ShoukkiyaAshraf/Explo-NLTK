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

# Normalizing tokens

lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
