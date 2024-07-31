# floor number
import math
T = int(input())

for _ in range(T):
    n,x = map(int,input().split())
    if n<=2:
        print(1)
    else:
        
       n = n-2
       n = math.ceil(n/x)
       n =n +1 # (flr-1)x + 2 = house_num
       print(n)