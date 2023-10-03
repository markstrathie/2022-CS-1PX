# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 18:14:10 2022

@author: Mark
"""

def has_more_words(string1, string2):
    try:
        assert type(string1) == type('a')
        assert type(string2) == type('a')
        split1 = string1.strip().split(sep=',')
        split2 = string2.strip().split(sep=',')
        length1 = len(split1)
        length2 = len(split2)
        if length1 > length2:
            return True
        else:
            return False
    except Exception as e:
        print('Error running code' + str(e))
    
print(has_more_words('banana,banana,popsicle', 'hat,egg,dog,cat'))