
T = int(input())

for _ in range(T):
    n,m = map(int,input().split())
    x = str(input())
    s = str(input())
    set1 = set(s)

    flag = False
    op = 0
    if(s==x):
        print(0)
        continue
    

    

    while(len(x)<=(5*max(m,n))):
        #print(x)
        if (len(x)>=len(s)):
            start = 0
            end = start + m

            for j in range(len(x)-m):
                st = x[start:end]
                if st == s:
                    print(op)
                    flag = True
                    break
                start+=1
                end+=1
        if flag==True:
            break

        x=x+x
        op+=1
    if flag ==False:
        print(-1)


        
    


