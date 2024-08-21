N, M = map(int, input().split())

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def is_colored(x, y):
    global N
    colored = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx, ny) and n_lst[nx][ny]:
            colored += 1
    
    # 편안한 상태는 인접 색칠칸이 3이어야 함
    if colored == 3:
        return True

    return False

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


n_lst = [[0]*N for _ in range(N)]

for _ in range(M):
    r, c = map(int, input().split())
    r, c = r-1, c-1
    n_lst[r][c] = 1

    if is_colored(r, c):
        print(1)
    else:
        print(0)