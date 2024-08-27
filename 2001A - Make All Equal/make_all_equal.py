
T=int(input())

for _ in range(T):
    n=int(input())
    arr=list(map(int,input().split()))
    d = {}
    for i in range(1,n+1):
        d[i]=0
    
    for i in arr:
        d[i]+=1
    max_cnt = max(d.values())
    print(n-max_cnt)

    
    