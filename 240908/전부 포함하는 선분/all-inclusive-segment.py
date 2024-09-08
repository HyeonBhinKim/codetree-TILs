n = int(input())

n_lst = [tuple(map(int, input().split())) for _ in range(n)]

ans = 100
for i in range(n):
    minx = 100
    maxx = 0
    for j in range(n):
        if i==j:
            continue
        x1, x2 = n_lst[j][0], n_lst[j][1]
        minx = min(minx, x1)
        maxx = max(maxx, x2)
    ans = min(ans, maxx-minx)

print(ans)