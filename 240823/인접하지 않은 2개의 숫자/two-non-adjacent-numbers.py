n = int(input())

n_lst = list(map(int, input().split()))

ans = 0

for i in range(n-2):
    for j in range(i+2, n):
        ans = max(ans, n_lst[i]+n_lst[j])

print(ans)