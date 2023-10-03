# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 16:16:14 2022

@author: Mark
"""

def comparedicts(dict1, dict2):
    keys1 = dict1.keys()
    keys2 = dict2.keys()
    diffList = []
    print(keys1)
    for i in range(len(keys1)):
        if keys1[i] != keys2[i]:
            diffList += [(keys1[i], dict1[keys1[i]])]
            diffList += [(keys2[i], dict2[keys2[i]])]
        for x in keys1:
            if dict1[x] != dict2[x]:
                diffList += [(x, dict1[x])]
                diffList += [(x, dict2[x])]
    if diffList == []:
        return
    else:
        diffSet = set(diffList)
        return diffSet

        

print(comparedicts( {"a": 1, "b": 2}, {"a": 1, "b": 2} ))