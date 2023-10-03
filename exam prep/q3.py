# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 15:57:00 2022

@author: Mark
"""

def productFun(x,y):
    try:
        if type(x) != int or type(y) != int:
            print('The input values must both be integers')
            return 0
        elif x < 0 or y <0:
            print('The input values must both be positive')
            return 0
        elif y == 0:
            return 0
        else:
            product = x
            return product + productFun(x,y-1)
    except Exception as e:
        print('There has been the following error: ' + str(e))
        return
    
print(productFun(2,399))