N, S = map(int, input().split())

n_lst = list(map(int, input().split()))

ans = 100000

for i in range(N):
    for j in range(i+1, N):
        tmp = sum(n_lst) - n_lst[i] - n_lst[j]
        ans = min(ans, abs(S-tmp))

print(ans)