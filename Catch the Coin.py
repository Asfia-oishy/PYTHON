# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 16:55:01 2024

@author: Asfia Moon
"""

n = int(input())
 
for i in range(n):
    
    x,y = map(int,input().split())
    
    if y<-1:
        print("NO")
    else:
        print("YES")