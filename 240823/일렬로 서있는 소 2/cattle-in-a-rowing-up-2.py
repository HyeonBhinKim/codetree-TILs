N = int(input())
n_lst = list(map(int, input().split()))
cnt = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if i < j < k and n_lst[i] <= n_lst[j] <= n_lst[k]:
                cnt += 1

print(cnt)