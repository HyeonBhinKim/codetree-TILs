N, K = map(int, input().split())

n_lst = [int(input()) for _ in range(N)]

n_lst.sort()

ans = 0

for idxi, i in enumerate(n_lst):
    tmp = 0
    for idxj, j in enumerate(n_lst):
        if idxi <= idxj and abs(j - i) <= K:
            tmp += 1
    ans = max(ans, tmp)

print(ans)