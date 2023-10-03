# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 11:39:10 2022

@author: Mark
"""

def gnomesorted(myList):
    length = len(myList) - 1
    posSorted = 1
    while posSorted <= length and myList[posSorted] >= myList[posSorted-1]:
            posSorted += 1
    posSorted -= 1
    pos = posSorted
    while pos <= length:
        if pos == 0 or myList[pos] >= myList[pos-1]:
            pos += 1
        else:
            tmp = myList[pos]
            myList[pos] = myList[pos-1]
            myList[pos-1] = tmp
            pos -= 1
    return posSorted

forSorting = [1,2,3,4,5,1,2,3,3,3,1,2,3,4]
 
print(gnomesorted(forSorting))
print(forSorting)