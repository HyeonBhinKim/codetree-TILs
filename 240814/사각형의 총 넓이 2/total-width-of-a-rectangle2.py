OFFSET = 100

N = int(input())

n_lst = [[0]*201 for _ in range(201)]

ans = 0

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET
    for i in range(x1, x2):
        for j in range(y1, y2):
            if n_lst[i][j] == 0:
                n_lst[i][j] = 1
                ans += 1

print(ans)