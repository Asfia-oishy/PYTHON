# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 00:45:04 2024

@author: Asfia Moon
"""
    
T = int(input())

for _ in range(T):
    a = list(map(int,input().split()))
    dis = 100000000000000000000000
    for i in a:  
        f_i = abs(i-a[0])+abs(i-a[1])+abs(i-a[2])
        if f_i<dis:
            dis = f_i
    print(dis)
        
