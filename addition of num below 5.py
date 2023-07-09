# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 07:12:19 2022

@author: Pranali
"""

def recursiveRange(n):
    if n == 0:
        return n
    else:
        return n + recursiveRange(n-1)
    
print(recursiveRange(6))