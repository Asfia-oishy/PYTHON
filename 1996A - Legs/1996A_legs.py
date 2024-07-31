# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 12:59:06 2024

@author: Asfia Moon
"""
import math
T = int(input())

for _ in range(T):
    n = int(input())
    
    if n<4:
        animals = 1

    if n%4==0:
        animals = (n/4)
    elif n>4:
        chicken = int((n%4)/2)
        cows = int(n/4)
        animals = chicken + cows
    print(int(animals))