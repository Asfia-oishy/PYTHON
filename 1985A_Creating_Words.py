"""
Created on Wed Jul 18 18:02:53 2024

@author: Asfia Moon
"""

T = int(input())

for _ in range(T):
    a,b = map(str,input().split())
    #print( a,b)
    a = list(a)
    b= list(b)
    
    tmp =a[0]
    a[0]=b[0]
    b[0]=tmp
    
    a = "".join([str(i) for i in a])
    b = "".join([str(i) for i in b])
    
    
    
    print(a,b)