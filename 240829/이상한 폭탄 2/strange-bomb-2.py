N, K = map(int, input().split())

n_lst = [0]*(N)

bomb = -1

for i in range(N):
    n_lst[i] = int(input())

for j in range(N):
    for k in range(j+1, N):
        if k-j > K:
            continue
        if n_lst[j] == n_lst[k]:
            bomb = max(bomb, n_lst[j])

print(bomb)