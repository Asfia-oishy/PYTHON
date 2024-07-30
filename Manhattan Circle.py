# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 15:58:57 2024

@author: Asfia Moon
"""

T = int(input())

for _ in range(T):
    n,m = map(int,input().split())
    L = []
    
    t = 0 #top bottom left right
    ni = 0
    mi = m-1
  
    for i in range(n):
        s = str(input())
        L.append(list(s))
        
    for i in range(n):
        for j in range(m):
            if L[i][j] == ".":
                continue
            if L[i][j] == '#' and t==0:
                top = tuple([i,j])
                left = top
                t=1
            else:
                if(i>=ni) and (j<=mi):
                    ni=i
                    mi =j
                    left = tuple([i,j])
                    
    if top == left:
        print(top[0]+1,top[1]+1)
    else:
        print(left[0]+1,top[1]+1)

        
            
        

            
    