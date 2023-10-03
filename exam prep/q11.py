# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 18:48:03 2022

@author: Mark
"""
#Describe and justify the big-O time complexity of your function.

 #   Example: binary_search_ignore_strings(['z', 2, 'b', '10', 7, 10, 20], 10)
 #should return the value 5.

def iterative_binary_search(my_list, value):
    hi = len(my_list) - 1
    lo = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        while type(my_list[mid]) != int:
            mid += 1
            if mid == hi:
                mid = (lo + hi) // 2
            while type(my_list[mid]) != int:
                mid -= 1
        if my_list[mid] < value:
            lo = mid + 1
        elif my_list[mid] > value:
            hi = mid - 1
        else:
            return mid
    return -1
        
test_list = ['z', '2', 'b', '10', '7', '10', '20']
print(iterative_binary_search(test_list,28))