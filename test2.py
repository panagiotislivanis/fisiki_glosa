# -*- coding: utf-8 -*-
"""
Created on Fri May 19 17:08:07 2023

@author: panag
"""

import nltk
from nltk.book import *

# Specify the encoding when reading the text
all_words = [word.lower() for word in text3 if word.isalpha()]

unique_words = set(all_words)
num_unique_words = len(unique_words)
num_total_words = len(all_words)

print("Total number of words:", num_total_words)
print("Number of unique words:", num_unique_words)
