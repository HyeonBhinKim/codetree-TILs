def in_range(x, y):
    return 0 <= x < M and 0 <= y < N

dxs, dys = [1, 1, 1, -1, -1, -1, 0, 0], [-1, 0, 1, -1, 0, 1, -1, 1]

N, M = map(int, input().split())

word_arr = [list(input()) for _ in range(N)]

ans = 0

for i in range(N):
    for j in range(M):
        if word_arr[i][j] != 'L':
            continue

        for dx, dy in zip(dxs, dys):
                    curt = 0
                    curx = j
                    cury = i
                    while True:
                        nx = curx + dx
                        ny = cury + dy
                        if in_range(nx, ny) == False:
                            break
                        if word_arr[ny][nx] != "E":
                            break
                        curt += 1
                        curx = nx
                        cury = ny
                    
                        if curt == 2:
                            ans += 1
                            break

print(ans)