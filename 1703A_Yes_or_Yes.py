T = int(input())
for _ in range(T):
	val = str(input())
	if (val[0] == 'Y' or val[0] == 'y') and (val[1] == 'E' or val[1] == 'e') and (val[2] == 'S' or val[2] == 's'):
		print("YES")
	else:
		print("NO")