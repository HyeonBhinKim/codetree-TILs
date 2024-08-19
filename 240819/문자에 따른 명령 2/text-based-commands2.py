N = input()

x, y = 0, 0
dir_num = 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

for i in N:
    if i == "R":
        # rotate direction
        dir_num = (dir_num + 1) % 4
    elif i == "L":
        # rotate direction
        dir_num = (dir_num - 1 + 4) % 4
    else:
        # move
        x, y = x + dx[dir_num], y + dy[dir_num]

print(x, y)