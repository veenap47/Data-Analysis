# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 16:17:13 2022

@author: Dell
"""

def calc (x, op, y):
    try:
        if op == '+' :
            result = x + y
        elif op == '-':
            result = x - y
        elif op == '*':
            result = x * y
        elif op == '/':
            result = x / y
        
        else :
            print("Invalid Operator")
            
        return result    
    except:
        print("Cant divide by 0!")
        
    

res = calc(5,'/',0)
print(res)