# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 16:47:13 2022

@author: Mark
"""

def bubbleSort(myList):
    n = len(myList)
 
    # Iterate over each element
    for i in range(n):
 
        # Last i elements are already in order
        for j in range(0, n-i-1):
            # Swap if the element found is greater
            # than the next element
            if type(myList[j]) != type(myList[j+1]):
                if type(myList[j]) == str:
                    tmp = myList[j]
                    myList[j] = myList[j+1]
                    myList[j+1] = tmp
            elif myList[j] > myList[j+1] :
                 tmp = myList[j]
                 myList[j] = myList[j+1]
                 myList[j+1] = tmp


forSorting = [64, 34, 25, '12', 'eggs', 'beans', '11', '90']
 
bubbleSort(forSorting)
print(forSorting)