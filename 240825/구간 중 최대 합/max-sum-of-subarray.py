n, k = map(int, input().split())

n_lst = list(map(int, input().split()))

ans = 0
for i in range(n-k+1):
    ans = max(ans, sum(n_lst[i:i+k]))

print(ans)