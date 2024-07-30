#each attack use kora jabe 1+i*ci tomo turn e. 1+ bcz 1st turn e sobaike use krbo

T = int(input())

for _ in range(T):
    h,n = map(int,input().split())
    attacks = list(map(int,input().split()))
    cd = list(map(int, input().split()))  # coolDown
    cd = [(x, 1) for x in cd]
    h-=sum(attacks) #1st turn
    t =1

    while h>0:
        t+=1
        for i in range(len(cd)):
            val1 = cd[i][0]
            val2 = cd[i][1]
            if (val1*val2)+1 == t:
                h -= attacks[i]
                cd[i] = tuple([val1,val2+1])

    print(t)  
    attacks.clear()
    cd.clear()
