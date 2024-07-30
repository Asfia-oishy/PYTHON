# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 13:35:00 2024

@author: Asfia Moon
"""
    
T = int(input())

for _ in range(T):
    n,q =map(int,input().split())
    a = str(input())
    b = str(input())
    d={}
    char = 97
    
    for i in range(1,27):
        
        d[chr(char)]=0
        char+=1
    

    for i in range(q):
        op=0
        
        x,y = map(int,input().split())
        a1 = a[x-1:y]
        b1 = b[x-1:y]
        dd = d.copy()

      
        for j in a1:
            dd[j]+=1
        #print("before",dd)    
        for k in b1:
            if(dd[k]!=0):
                dd[k]-=1
            else:
                op+=1
        #print("after",dd) 
        print(op)
           

    



        
    