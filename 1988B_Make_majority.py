T = int(input())

for _ in range(T):
	n = int(input())
	val = list(str(input()))
	c0=val.count('0')
	c1 = n-c0
	majority = '0'
	if c1>c0:
		majority = '1'

	flag =False
	for i in range(n):			
		if val[i]=='1':
			flag = False
		elif val[i]=='0' and flag == False:
			flag = True
			val[i] = majority
		else:
			val[i]= '-1'
		
	if val.count('0')==0:
		print("YES")
		continue
	
	if val.count('0')>= val.count('1'):
		print("NO")
	else:
		print("YES")