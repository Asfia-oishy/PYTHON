# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 00:55:03 2024

@author: Asfia
"""

T = int(input())

for _ in range(T):
    n,f,k = map(int,input().split()) # cubes,fav,remove
    a = list(map(int,input().split()))
    fav_val = a[f-1]
    a.sort(reverse=True)
    flag = False # to check fav val position
    if a.count(fav_val)==1:
        if a.index(fav_val)<= (k-1):
            print("yes")
        else:
            print("no")
    else:
        for i in range(n):
            if a[i]==fav_val:
                ind=i
                if i<=k-1:
                    flag= True
        if ind<=k-1:
            print("yes")
        elif flag==True and ind>k-1:
            print("maybe")
        else:
            print("no")
        
    