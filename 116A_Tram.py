
#Tram

n = int(input()) # stops


capacity = 0
x = 0
for i in range(n):
    a,b= map(int,input().split()) #exit,enter
    x = x + (b-a)
    capacity= max(capacity,x)
    
print(capacity)