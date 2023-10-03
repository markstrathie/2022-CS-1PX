# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 16:39:54 2022

@author: Mark
"""

def higher_order(f, my_list):
    new_list = []
    for i in range(len(my_list)):
        new_list.append(f(my_list[i]))
    return new_list

def testFun(i):
    i = i*2
    return i

test_list = [1,2,3]
print(higher_order(testFun,test_list))

#big O complexity of f is O(1). So complexity of higher_order is O(1) + O(n) = O(n)