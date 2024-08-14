n, t = map(int, input().split())

n_lst = list(map(int, input().split()))

ans, cnt = 0, 0

for i in range(n):
    if n_lst[i] > t:
        cnt += 1
    else:
        cnt = 0

    ans = max(ans, cnt)

print(ans)