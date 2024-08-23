import sys

N = int(input())

n_lst = [
    int(input()) for _ in range(N)
]

ans = sys.maxsize

for i in range(N):
    tmp = 0
    for j in range(N):
        dist = (j + n - i) % n
		tmp += dist * n_lst[j]
    ans = min(ans, tmp)

print(ans)