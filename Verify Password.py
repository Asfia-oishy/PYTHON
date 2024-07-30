# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 18:02:53 2024

@author: Asfia Moon
"""
    
T = int(input())

for _ in range(T):
    l = int(input())  # length

    pword = str(input())
    flag = False
    for i in range(len(pword)-1):
        if pword[i] <= pword[i+1]:
            if (ord(pword[i])>=48 and ord(pword[i])<=57) or (ord(pword[i])>=97 and ord(pword[i])<=122):
                continue
        
            else:
                print("NO")            
                flag = True
                break
        else :
            if flag == False:
                flag = True          
                print("NO")
          
    if flag == False:
        print("YES")
        flag = True
                
                    
        
        
 
            

             
    
