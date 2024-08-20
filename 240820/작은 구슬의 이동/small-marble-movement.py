def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

n, t = map(int, input().split())
r, c, d = map(str, input().split())
x, y = int(r)-1, int(c)+1

dx, dy = [1, 0, 0, -1], [0, -1, 1, 0]

D = {
    "U": 0,
    "D": 3,
    "R": 2,
    "L": 1
}

dir_num = D[d]


while t+1:
    nx, ny = x + dx[dir_num], y + dy[dir_num]
    if not in_range(nx, ny):  # check whether position is out of grid
        dir_num = 3 - dir_num # change direction
    
    # move
    x, y = x + dx[dir_num], y + dy[dir_num]

    t -= 1

print(x+1, y+1)