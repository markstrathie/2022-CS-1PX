# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 16:41:43 2022

@author: Mark
"""

def swap(myList, i, j):
    tmp = myList[j]
    myList[j] = myList[i]
    myList[i] = tmp

def findMinimumInd(myList):
    if len(myList) <=0:
        return None
    smallestInd = 0
    for i in range(len(myList)):
        if myList[i] < myList[smallestInd]:
            smallestInd = i
    return smallestInd

def selectionRecursive(myList):
#     print ("\n\n\n sorting list: ")
#     print (myList)
    size = len(myList)
    if size <= 1:
        return myList
    else:
        smallestInd = findMinimumInd(myList)
        swap(myList, 0, smallestInd)
        return selectionRecursive(myList[1:]) + [myList[0]]


myList = [6, 2, 3, 7, 9, 1, 4, 10, 8, 5]
myList = selectionRecursive(myList)
print(myList)