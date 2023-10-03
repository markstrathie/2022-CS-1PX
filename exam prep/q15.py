# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 17:21:32 2022

@author: Mark
"""

def count_frequent_word(my_string):
    word_dict = {}
    split = my_string.strip().split()
    for word in split:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    highest_value = word_dict[split[0]]
    highest_key = 'None'
    for key in word_dict:
        if word_dict[key] > highest_value:
            highest_value = word_dict[key]
            highest_key = key
    for key in word_dict:
        if word_dict[key] == highest_value and key != highest_key:
            highest_key += ' ' + key
            
    return highest_key

string = "dog dog cat egg"
print(count_frequent_word(string))