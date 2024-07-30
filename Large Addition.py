"""
Created on Wed Jul 18 18:02:53 2024

@author: Asfia Moon
"""
    
T = int(input())

for _ in range(T):
    num = int(input())
    f= True
    L = list(str(num))
    lenn = len(L)
    for i in range(lenn-1):
        low = 5
        high = 9
        a =int(L[lenn-i-1])  
        #print(a)
        if (a==9 and i==0) or int(L[0])>1 or (int(L[i])==0 and i!=0):
            f = False
            print("NO")
            break         
        a = 10+a  
        while (low+high)!=a:    
            if low+high<a:
                
                low+=1
                if low>10 and i!=0 and f:
                    f=False
                    print("NO")
                    break
            else:
                high-=1
                if high<5 and f:
                    f = False
                    print("NO")
                    break   
    if f:
        print("YES")

        
        