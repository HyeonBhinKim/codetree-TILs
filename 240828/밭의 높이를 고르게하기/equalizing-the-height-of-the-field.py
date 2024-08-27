N, H, T = map(int, input().split())

n_lst = list(map(int, input().split()))

min_val = 10001

for i in range(N-T+1):
    tmp_val = 0
    for j in range(i, i+T):
        tmp_val += abs(n_lst[j]-H)
    min_val = min(min_val, tmp_val)

print(min_val)