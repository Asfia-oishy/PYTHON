# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 13:55:21 2024

@author: Asfia Moon
"""
T = int(input())

for _ in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = a.copy()
    
    flag = False
    last_num = b[n]
    steps=0
    
    if a.count(last_num)!=0 :
        steps+=1 #copy added
        flag= True

    mini = 1000000000000000
    for j in range(n):
        if flag == False: 
            if (last_num>=a[j] and last_num<=b[j]) or (last_num>=b[j] and last_num<=a[j]):
                steps+=1
                flag= True
        diff = b[j] - a[j]
        min_dis1 = abs(last_num -a[j])
        if min_dis1<mini:
            mini = min_dis1
        min_dis2 = abs(last_num - b[j])
        if min_dis2<mini:
            mini = min_dis2
        #print(mini)
        a[j]+=diff
        steps+=abs(diff)
    if flag == False:
        steps+=(mini+1)
        
    print(steps)
 

        
  
        
    
      
            
            

            
    