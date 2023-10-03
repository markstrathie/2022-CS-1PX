# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 17:21:32 2022

@author: Mark
"""

def count_unique_words(my_string):
    word_dict = {}
    split = my_string.strip().split()
    for word in split:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return len(word_dict)

string = "you'll do fookin nootin nootin"
print(count_unique_words(string))   