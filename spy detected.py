
T = int(input())

for _ in range(T):
    length = int(input())
    val = []
    val= list(map(int,input().split()))
    for i in range(length-1):
        if val[i]!=val[i+1]:
            if i!=length-2:
                if val[i]==val[i+2]:
                    print(i+2)
                    break
                else:
                    print(i+1)
                    break
            else:
                print(i+2)
                break

    
        