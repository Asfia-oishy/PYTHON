

"""
Created on Wed Jul 18 18:02:53 2024

@author: Asfia Moon
"""
    
T = int(input())

for _ in range(T):
    n = int(input()) #length
    arr = list(map(int,input().split()))
    mini = min(arr)
    maxi = max(arr)
    fl = True
    f = True
    min_c = arr.count(mini)
    max_c = arr.count(maxi)
   # print( min_c , max_c)
    if mini == maxi or n==2:
        print("NO")
        fl= False

    
    while fl:
        if max_c+min_c!=n:
            print("YES")
            for i in arr:
                if i==mini:
                    print("B", end="")
                else:
                    print("R", end="")
    
        elif max_c+min_c==n:
            print("YES")
            
            if max_c>1 and min_c==1:
                for i in arr:
                    if i==maxi and f:
                        f = False
                        print("B", end="")
                    else:
                        print("R", end="")
            elif max_c==1 and min_c>1:
                for i in arr:
                    if i==mini and f:
                        f = False
                        print("B", end="")
                    else:
                        print("R", end="")
            else:
                for i in arr:
                    if i==mini and f:
                        f = False
                        print("B", end="")
                    else:
                        print("R", end="")
        print()
        break
                
        
       
     
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

    