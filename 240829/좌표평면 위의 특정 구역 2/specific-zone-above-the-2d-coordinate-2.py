N = int(input())
count = [0]*N
n_lst = [tuple(map(int, input().split()))for _ in range(N)]

for i in range(N):
	maxx, maxy = 1, 1
	minx, miny = 40000, 40000
	for j in range(N):
		if j == i:
			continue
				
		x, y = n_lst[j]
		maxx, maxy = max(x,maxx), max(y, maxy)
		minx, miny = min(x, minx), min(y, miny)
		count[i] = (maxx-minx)*(maxy-miny)

print(min(count))