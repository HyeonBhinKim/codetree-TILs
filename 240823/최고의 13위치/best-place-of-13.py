N = int(input())
n_lst = []

for _ in range(N):
    tmp = list(map(int, input().split()))
    n_lst.append(tmp)



ans = 0
for i in range(N):
    for j in range(N-2):
        cnt = arr[i][j] + arr[i][j+1] + arr[i][j+2]
    ans = max(ans, cnt)

print(ans)