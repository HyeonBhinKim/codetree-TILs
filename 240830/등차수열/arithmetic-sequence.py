n = int(input())
n_lst = list(map(int, input().split()))

cnt = 0

for i in range(n):
    for j in range(i+1, n):
        ai, aj = n_lst[i], n_lst[j]
        k = (ai + aj) / 2
        if k == (ai + aj) // 2:
            cnt += 1

print(cnt)