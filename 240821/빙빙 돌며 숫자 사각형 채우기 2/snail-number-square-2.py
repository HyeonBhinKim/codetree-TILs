def in_range(x, y):
    return 0 <= x < m and 0 <= y < n

dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]

n, m = map(int, input().split())

num_lst = [[0]*m for _ in range(n)]

x, y = 0, 0
dir_num = 0

num_lst[y][x] = 1

for i in range(2, n*m+1):
    nx, ny = x + dx[dir_num], y + dy[dir_num]

    if not in_range(nx, ny) or num_lst[ny][nx] != 0:
        dir_num = (dir_num + 1) % 4
        nx, ny = x + dx[dir_num], y + dy[dir_num]
    
    x, y = nx, ny

    num_lst[y][x] = i

for j in num_lst:
    print(*j)