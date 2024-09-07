N = int(input())

n_lst =[0] * N

cnt = 0
for i in range(N):
    n_lst[i] = int(input())
    cnt += n_lst[i]

avg = cnt // N

ans = 0

for j in range(N):
    tmp  = n_lst[j] - avg
    if tmp > 0:
        ans += tmp

print(ans)