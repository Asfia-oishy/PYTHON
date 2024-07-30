# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 17:50:33 2024

@author: Asfia
"""

T = int(input())
 
for _ in range(T):
   n = int(input())
   arr = list(map(int, input().split()))
   result = 0
   prefix_sum = [0] * n
   prefix_sum[0] = arr[0]
  
   for i in range(1, n):
       prefix_sum[i] = prefix_sum[i - 1]+arr[i]
  
   max_ = arr[0]
   for i in range(n):
       if (i == 0 and arr[i] == 0):
           result+=1
       else:
           max_= max(arr[i],max_)
 
           if prefix_sum[i]- max_ == max_:
               result+=1
               
   print(result)