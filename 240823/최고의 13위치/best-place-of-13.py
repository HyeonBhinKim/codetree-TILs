N = int(input())
n_lst = []

for _ in range(N):
    tmp = list(map(int, input().split()))
    n_lst.append(tmp)



ans = 0
for i in range(N):
    cnt = 0
    for j in range(N-2):
        if n_lst[i][j] == 1:
            cnt += 1
        if n_lst[i][j+1] == 1:
            cnt += 1
        if n_lst[i][j+2] == 1:
            cnt += 1

        ans = max(ans, cnt)
        cnt = 0

print(ans)