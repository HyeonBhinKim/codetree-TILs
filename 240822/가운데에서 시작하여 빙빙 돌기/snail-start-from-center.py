def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

n = int(input())

x, y = n//2, n//2
dirt = 0

n_lst = [[0]*n for _ in range(n)]

n_lst[y][x] = 1

for i in range(2, (n**2)+1):
    nx, ny = x + dx[dirt], y + dy[dirt]

    if not in_range(nx, ny) or n_lst[ny][nx] != 0:
        dirt = (dirt + 1) % 4
        nx, ny = x + dx[dirt], y + dy[dirt]

    x, y = nx, ny
    n_lst[y][x] = i

for i in n_lst:
    print(*i)