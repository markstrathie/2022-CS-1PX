# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 18:19:25 2022

@author: Mark
"""

def reverse_list(myList):
    if len(myList) == 0:
        return []
    elif len(myList) == 1:
        return myList
    else:
        return [myList[len(myList)-1]] + reverse_list(myList[:len(myList)-1])
    
myList = [1,2,3,3243244]
print(reverse_list(myList))