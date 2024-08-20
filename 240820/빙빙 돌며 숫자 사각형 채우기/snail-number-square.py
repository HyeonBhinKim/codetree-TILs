def in_range(x, y):
    return 0 <= x and x < m and 0 <= y and y < n

n, m  = map(int, input().split())
answer = [[0]*m for _ in range(n)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

y, x = 0, 0
dir_num = 0  # 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽

answer[y][x] = 1

for i in range(2, n * n + 1):
    # 현재 방향 dir를 기준으로 그 다음 위치 값을 계산합니다.
    nx, ny = x + dx[dir_num], y + dy[dir_num]
    
    # 더 이상 나아갈 수 없다면
    # 시계방향으로 90'를 회전합니다.
    if not in_range(nx, ny) or answer[ny][nx] != 0:
        dir_num = (dir_num + 1) % 4

    # 그 다음 위치로 이동한 다음 배열에 올바른 값을 채워넣습니다.
    x, y = x + dx[dir_num], y + dy[dir_num]
    answer[y][x] = i

for i in answer:
    print(*i)