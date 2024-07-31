T = int(input())
for _ in range(T):
  a,b,c = map(int,input().split())
  if c>b:
    b = (c-b) + c
  if (a==b):
    print(3)
  else:
    if a<b:
      print(1)
    else:
      print(2)
   
  