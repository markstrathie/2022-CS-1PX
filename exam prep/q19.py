# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 11:39:10 2022

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

def findk(myList,k):
    smallestInd = findMinimumInd(myList)
    if smallestInd == 0:
        k = k + 1
        return findk(myList[1:],k)
    else:
        return k

def selectionRecursive(myList):
    size = len(myList)
    if size <= 1:
        return myList
    else:
        smallestInd = findMinimumInd(myList)
        swap(myList, 0, smallestInd)
        return [myList[0]] + selectionRecursive(myList[1:])
    
def selectionSorted(myList):
    k = findk(myList, 0)
    myList = myList[:k] + selectionRecursive(myList[k:])
    return k, myList

myList = [1,2,3,4,5,6,9,8,7,10,11,23]
print(selectionSorted(myList))