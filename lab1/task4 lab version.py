# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 16:16:14 2022

@author: Mark
"""

def comparedicts(dict1, dict2):
    keys = dict1.keys()
    diffList = []
    for x in keys:
        if dict1[x] != dict2[x]:
            diffList += [(x, dict1[x])]
            diffList += [(x, dict2[x])]
    if diffList == []:
        return
    else:
        diffSet = set(diffList)
        return diffSet

        

print(comparedicts( {"a": 1, "b": 3}, {"a": 1, "b": 2} ))