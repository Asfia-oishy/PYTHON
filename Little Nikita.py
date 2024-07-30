# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 17:11:22 2024

@author: Asfia Moon
"""

T = int(input())

for _ in range(T):
    n,m = map(int, input().split())
    
    if n<m:
        print("No")
    elif (n-m) % 2 == 0:
        print("Yes")
    else:
        print("No")