n, m = map(int, input().split())
ab_lst = []
for  _ in range(m):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    ab_lst.append([a,b])
    
ans = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        comb = 0
        for a, b in ab_lst:
            if i == a and j == b:
                comb += 1
        ans = max(ans, comb)


print(ans)