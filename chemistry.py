# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 11:38:13 2024

@author: Asfia Moon
"""
T = int(input())

for _ in range(T):
    n,k = map(int,input().split())
    s = str(input())
    sett = set(s)
    d = {}
    odd = 0
    for i in sett:
        d[i]=0
    
    for j in s:
        d[j]+=1
        
  
    
    for x in d.values():
        if x%2==0:
            continue
        odd+=1
    if k==odd or k==odd-1 or odd<k:
        print("YES")
    else :
        print("NO")
    
	
		
			