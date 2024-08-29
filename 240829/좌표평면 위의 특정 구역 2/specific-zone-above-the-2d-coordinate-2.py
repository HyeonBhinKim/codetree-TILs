N = int(input())
n_lst = [tuple(map(int, input().split()))for _ in range(N)]

ans = 1600000000

for i in range(N):
	maxx, maxy = 1, 1
	minx, miny = 40000, 40000
	for j, (x, y) in enumerate(n_lst):
        # i번째 점은 제외합니다.
		if j == i:
			continue
		maxx, maxy = max(x, maxx), max(y, maxy)
		minx, miny = min(x, minx), min(y, miny)

	ans = min(ans, (maxx-minx)*(maxy-miny))

print(ans)