# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 14:50:21 2022

@author: Mark
"""

def oddSum(myList):
    if len(myList) == 0:
        return 0
    else:
        odd_sum = myList[0]
        return odd_sum + oddSum(myList[2:])
    
sumList = [69,384984984,1,34325325,1,34325,1,34,1,1,1,1,1,1,1,1,231413431]
print(oddSum(sumList))