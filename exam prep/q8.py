# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 17:19:46 2022

@author: Mark
"""

def just_a(my_string):
    a_words = []
    split = my_string.strip().split()
    for word in split:
        if word[:1] == 'a':
            a_words.append(word)
    return a_words

test_string = "you'll do fookin nootin ant and dec"
print(just_a(test_string))