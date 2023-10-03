# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 16:15:10 2022

@author: Mark
"""

def higher_order(f, my_dict):
    newDictionary = {}
    for key in my_dict:
        if type(my_dict[key]) == type([]):
            newDictionary[key] = f(my_dict[key])
        else:
            newDictionary[key] = my_dict[key]
    return newDictionary

def testFun(myList):
    for i in range(len(myList)):
        myList[i] = 2*myList[i]
    return myList
        
testDict = {'egg':2, 'toast':[5,5,3,2,1] }
print(higher_order(testFun,testDict))