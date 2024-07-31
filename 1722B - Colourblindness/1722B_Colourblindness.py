
#AsfiaMoon
T = int(input())

for _ in range(T):
	n = int(input())
	r1 = str(input())
	r1 =r1.replace('G','B')
	r2= str(input())
	r2= r2.replace('G','B')
	if r1==r2:
		print("YES")
	else:
		print("NO")





