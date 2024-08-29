N = int(input())

n_lst = [tuple(map(int, input().split()))for _ in range(N)]

minxy = 2002
x, y = 0, 0

for i in range(N):
	for j in range(i+1, N):
		tmpx = abs(n_lst[i][0] - n_lst[j][0])
		tmpy = abs(n_lst[i][1] - n_lst[j][1])
		tmpxy = ((tmpx**2) + (tmpy**2))**0.5
		if minxy > tmpxy:
			minxy = tmpxy
			x, y = tmpx, tmpy
		
print(x*x+y*y)