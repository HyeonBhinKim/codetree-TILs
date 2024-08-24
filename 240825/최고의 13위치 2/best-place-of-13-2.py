N = int(input())

n_lst = [list(map(int, input().split())) for _ in range(N)]

ans = 0

for i in range(N):
    for j in range(N-2):
        for k in range(N):
            for l in range(N-2):
                tmp = 0
                if not (i == k and (j <= l <= j + 2 or l <= j <= j + 2)):
                    tmp += sum(n_lst[i][j:j+3])
                    tmp += sum(n_lst[k][l:l+3])
                    ans = max(ans, tmp)

print(ans)