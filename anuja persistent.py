# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 01:13:05 2022

@author: Pranali
"""

n = input()
s = input().split()
p = []
for i in s:
    if ((i != 'a') and (i != 'e') and (i != 'i') and (i != 'o') and (i != 'u') and (i != 'A') and (i != 'E') and (i != 'I') and (i != 'O') and (i != 'U')):
        p.append(i)
print(len(p))