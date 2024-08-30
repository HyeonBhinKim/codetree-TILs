X, Y = map(int, input().split())

ans = 0

for i in range(X, Y+1):
    tmp = 0
    while i:
        tmp += i%10
        i //= 10
    ans = max(ans, tmp)

print(ans)