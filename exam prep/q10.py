# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 18:37:21 2022

@author: Mark
"""

def recursive_binary_search(my_list, lo, hi, value):
    if len(my_list) < 1:
        return -1
    if lo > hi:
        return -1
    
    mid = (lo + hi) // 2
    mid_value = my_list[mid]
    
    if mid_value == value:
        return mid
    if mid_value > value:
        new_hi = mid - 1
        return recursive_binary_search(my_list, lo, new_hi,value)
    if mid_value < value:
        new_lo = mid + 1
        return recursive_binary_search(my_list, new_lo, hi,value)
    
test_list = [1,2,5,9,12,22,27,88,192,232]
print(recursive_binary_search(test_list, 0, len(test_list)-1,232))
        