# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 17:16:13 2022

@author: Mark
"""

def dict_s_sum(myDict):
    s_sum = 0
    try:
        for key in myDict:
            if type(key) == str:
                s_sum += sum(myDict[key])
        return s_sum
    except Exception as e:
        print('Issue with input: ' + str(e))
        return s_sum

testDict = {'sausage':[1,2,3,4], 'eggs': [1,2,3], 'soup':[5,5,5], 3:[1,2,3]}
print(dict_s_sum(testDict))