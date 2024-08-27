T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int,input().split()))
    # min_dist= 1000000
    # for i in range(len(arr)):
    #     for j in range(i+1,len(arr)):
    #         if abs(i-j)<min_dist:
    #             min_dist=abs(i-j)
    if n>2:
        print("NO")
    elif n==2:
        if abs(arr[0]-arr[1])>1:
            print("YES")
        else:
            print("NO")
    


               