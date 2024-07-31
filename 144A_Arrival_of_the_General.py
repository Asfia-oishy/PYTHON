

num = int(input())

h = list(map(int,input().split())) #heights

mini = min(h)
maxi = max(h)

length = len(h)

flag1 = False
flag2 = False

for i in range(len(h)):
    if (h[length-1-i])==mini and flag1==False:
        min_index = length-1-i
        flag1 = True
        
    if(h[i]==maxi) and flag2 == False:
        max_index = i
        flag2= True

if max_index < min_index:
    time = max_index + (length-1-min_index)
else:
    time = max_index + (length-1-min_index) -1
print(time)
    
        
        
