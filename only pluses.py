

T = int(input())
for _ in range(T):
    a,b,c=map(int,input().split())
    
    values = [a, b, c]

    for i in range(5):
        values.sort()
        values[0]+=1
        
    
    print(values[0]*values[1]*values[2])

