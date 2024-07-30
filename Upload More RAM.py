"""
Created on Wed Jul 17 18:02:53 2024

@author: Asfia Moon
"""
    
T = int(input())

for _ in range(T):
    n,k = map(int,input().split())
    

    i=0         
    while n>0:
        time = k*i + 1
        i+=1
        n-= 1
    print(time)  
        
    