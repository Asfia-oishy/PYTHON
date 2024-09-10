
T = int(input())

for _ in range(T):
    n,m = map(int,input().split())
    x = str(input()) #length n
    s = str(input()) #length m

    flag = False
    op = 0
    if(s==x):
        print(0)
        continue
    cnt =0
    while(True):
        if (len(x)>= m):
            start = 0
            end = start + m

            for j in range(len(x)-m+1):
                st = x[start:end]
                if st == s:
                    print(op)
                    flag = True
                    break
                start+=1
                end+=1
        if flag==True:
            break
        if len(x)>len(s):
            cnt+=1
        if cnt==2:
            break
        x=x+x
        op+=1
    if flag ==False:
        print(-1)


        
    


