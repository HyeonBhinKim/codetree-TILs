MAX_R = 2001
OFFSET = 1000

n_lst = [[0]*MAX_R for _ in range(MAX_R)]

minx, miny = 2002, 2002
maxx, maxy = -1, -1

x1_1, y1_1, x2_1, y2_1 = map(int, input().split())

x1_1 += OFFSET
y1_1 += OFFSET
x2_1 += OFFSET
y2_1 += OFFSET

for i in range(x1_1, x2_1):
    for j in range(y1_1, y2_1):
            n_lst[i][j] = 1

x1_2, y1_2, x2_2, y2_2 = map(int, input().split())

x1_2 += OFFSET
y1_2 += OFFSET
x2_2 += OFFSET
y2_2 += OFFSET

for i in range(x1_2, x2_2):
    for j in range(y1_2, y2_2):
        if n_lst[i][j] == 1:
            n_lst[i][j] = 0


for i in range(MAX_R):
    for j in range(MAX_R):
        if n_lst[i][j] == 1:
            minx = min(minx, i)
            miny = min(miny, j)
            maxx = max(maxx, i)
            maxy = max(maxy, j)


if minx <= maxx and miny <= maxy:
    ans = (maxx + 1 - minx) * (maxy + 1 - miny)
else:
    ans = 0  # 남아 있는 부분이 없을 경우

print(ans)