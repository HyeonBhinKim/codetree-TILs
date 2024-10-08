def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

n, t = map(int, input().split())
r, c, d = map(str, input().split())
x, y = int(r)-1, int(c)-1 # 1~n 까지니까 0 ~ n-1까지로

dx, dy = [0, 1, -1,  0], [1, 0,  0, -1]
D = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

dir_num = D[d]


while t:
    nx, ny = x + dx[dir_num], y + dy[dir_num]
    if in_range(nx, ny):  # 범위 체크
        x, y = nx, ny
    else:
        dir_num = 3 - dir_num # 방향 전환

    t -= 1

print(x+1, y+1)