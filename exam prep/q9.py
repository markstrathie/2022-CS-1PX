# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 17:53:55 2022

@author: Mark
"""

def iterative_binary_search(my_list, value):
    hi = len(my_list) - 1
    lo = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if my_list[mid] < value:
            lo = mid + 1
        elif my_list[mid] > value:
            hi = mid - 1
        else:
            return mid
    return -1
        
test_list = [1,4,7,8,14,20,22,23,60]
print(iterative_binary_search(test_list,1))