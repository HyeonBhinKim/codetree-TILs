n, m = map(int, input().split())
n_lst = list(map(int, input().split()))
mn_lst = [0] + n_lst
ans= 0

for i in range(1, n+1):
    cnt = 0
    target = i
    total = 0
    while cnt < m:
        cnt += 1
        total += mn_lst[target]
        target = mn_lst[target]
    ans = max(ans, total)

print(ans)