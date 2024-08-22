def in_range(x, y):
    return 0 <= x < m and 0 <= y < n

n, m = map(int, input().split())

nm_lst = [[0]*m for _ in range(n)]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

x, y = 0, 0
dir_t = 0

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

nm_lst[y][x] = "A"

for i in range(1, n*m):
    nx, ny = x + dx[dir_t], y + dy[dir_t]

    if not in_range(nx, ny) or nm_lst[ny][nx] != 0:
        dir_t = (dir_t+1)%4
        nx, ny = x + dx[dir_t], y + dy[dir_t]

    x, y = nx, ny
    nm_lst[y][x] = alphabet[i%26]

for j in nm_lst:
    print(' '.join(j))
    # print(*j)