# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 17:34:38 2024

@author: Asfia Moon
"""

T = int(input())
keys = []
found = 0

for _ in range(T):
    c = str(input())
    keys.clear()
    f = False

    for i in c:
        if i == 'r' or i == 'g' or i == 'b':
            keys.append(i)

        else:
            if i == 'R':
                if keys.count('r') == 0:
                    f =True
                    print("No")
                    break
            if i=='G':
                if keys.count('g')==0:
                    f =True
                    print("No")
                    break
            if i=='B':
                if keys.count('b')==0:
                    f =True
                    print("No")
                    break
    if(f == False):
        print("YES")

            
        