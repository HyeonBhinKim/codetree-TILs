n = int(input())
n_lst = list(map(int, input().split()))

n_lst.sort()
ans = 1000000000
for i in range(n):
    ans = min(ans, n_lst[i+n]-n_lst[i])

print(ans)