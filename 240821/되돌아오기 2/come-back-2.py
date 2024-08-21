move_str = input()

ans = -1
elasped_time = 0

y, x = 0, 0

move_d = 0

dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]

for i in move_str:
    if i == "F":
        y, x = y+dy[move_d], x+dx[move_d]
    elif i == "R":
        move_d = (move_d + 1) % 4
    else:
        move_d = (move_d - 1 + 4) % 4
    
    elasped_time += 1

    if y == 0 and x == 0:
        ans = elasped_time
        break

print(ans)