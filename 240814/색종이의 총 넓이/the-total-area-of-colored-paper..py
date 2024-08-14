N = int(input())

OFFSET = 100
MAX_R = 201
ans = 0

n_lst = [[0]*MAX_R for _ in range(MAX_R)]

for _ in range(N):
    x1, y1 = map(int, input().split())
    x1 += OFFSET
    y1 += OFFSET
    for i in range(x1, x1+8):
        for j in range(y1, y1+8):
            if n_lst[i][j] == 0:
                ans += 1
                n_lst[i][j] = 1

print(ans)