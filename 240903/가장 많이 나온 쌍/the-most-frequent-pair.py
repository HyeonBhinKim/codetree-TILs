n, m = map(int, input().split())
ab_lst = [list(map(int, input().split()))for _ in range(m)]


ans = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        comb = 0
        for a, b in ab_lst:
            if a > b:
                a, b  = b, a
            if i == a and j == b:
                comb += 1
        ans = max(ans, comb)

print(ans)