# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 19:51:19 2024

@author: Asfia Moon
"""
T = int(input())

for _ in range(T):
    num = int(input())
    p =""
    while 1:
        mod = num % 26
        div = int(num/26)
        
        if num<=28:
            p=p+"aa"
            last=chr((num-2)+97-1)
            print(p+last)
            break
        elif div!=0:
            if div==3 and mod==0:                
                p="zzz"
            elif div==2:
                p="z"
                if (num%26)!=0:
                    p+='z'
                    last = chr(mod +97-1)
                    p = p+last
                else:
                    p="zya"
                    
            else:
                p="z"
                p+=chr(mod-1 +97-1)
                p+='a'
            print(p[::-1])
            break
        
            
