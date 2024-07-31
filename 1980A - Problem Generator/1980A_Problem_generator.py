#asfia_moon : problem generator

T = int(input())

for _ in range(T):
	n,m = map(int,input().split()) #len,round
	a = input()
	prob = { 'A' : 0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0}
	for i in a:
		prob[i]+=1
	sum =0
	for j in prob.values():
		if j < m:
			sum+= m-j
	print(sum)
			
		
	