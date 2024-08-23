import sys

N = int(input())
n_lst = [
    list(map(int, input().split()))
    for _ in range(N)
]

ans = sys.maxsize

for i in range(1, N-1):
    y, x = n_lst[0][0], n_lst[0][1]
    tmp = 0
    for j in range(N):
        if i != j:
            tmp += abs(y-n_lst[j][0])+abs(x-n_lst[j][1])
            y, x = n_lst[j][0], n_lst[j][1]
    ans = min(ans, tmp)

print(ans)