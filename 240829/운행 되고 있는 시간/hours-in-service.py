N = int(input())

n_lst = [tuple(map(int, input().split()))for _ in range(N)]

ans = 0

for i in range(N):
	work = [0]*1001
	for j in range(N):
		if i == j:
			continue
		
		t1, t2 = n_lst[j]

		for t in range(t1+1, t2+1):
			work[t] = 1

	ans = max(ans, sum(work))

print(ans)