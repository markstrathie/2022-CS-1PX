# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 11:39:10 2022

@author: Mark
"""

def gnomesort(myList):
    length = len(myList) - 1
    pos = 0
    while pos <= length:
        if pos == 0 or myList[pos] <= myList[pos-1]:
            pos += 1
        else:
            tmp = myList[pos]
            myList[pos] = myList[pos-1]
            myList[pos-1] = tmp
            pos -= 1

forSorting = [64, 34, 25, 12, 22, 22, 11, 90]
 
gnomesort(forSorting)
print(forSorting)