N, K = map(int, input().split())

n_lst = [0]*(N)
exp_lst = [0]*(1000001)

bomb = 0
num_exp = 0

for i in range(N):
    n_lst[i] = int(input())

for j in range(N):
    for k in range(j+1, N):
        if k-j > K:
            break
        if n_lst[j] == n_lst[k]:
            exp_lst[n_lst[j]] += 1
            exp_lst[n_lst[k]] += 1

for idx, exp in enumerate(exp_lst):
    if num_exp <= exp:
        num_exp = exp
        bomb = idx

print(bomb)