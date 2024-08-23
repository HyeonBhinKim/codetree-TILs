import sys

N = int(input())

n_lst = [
    int(input()) for _ in range(N)
]

ans = sys.maxsize

for i in range(N):
    tmp = 0
    for j in range(N):
        if j-i >= 0:
            tmp += n_lst[j] * (j-i)
        else:
            tmp += n_lst[j] * (N+j-i)
    ans = min(ans, tmp)

print(ans)