def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

n = int(input())

x, y = n // 2, n // 2
dirt = 0  # 방향은 오른쪽에서 시작

n_lst = [[0] * n for _ in range(n)]

n_lst[y][x] = 1  # 시작 위치에 1 채우기

tmp = cnt = 1
bi = 2

for i in range(2, n**2 + 1):
    # 다음 위치로 이동
    x, y = x + dx[dirt], y + dy[dirt]

    if not in_range(x, y):  # 범위를 벗어난 경우
        # 이전 위치로 되돌리기
        x -= dx[dirt]
        y -= dy[dirt]
        dirt = (dirt + 1) % 4  # 방향을 바꿈
        x, y = x + dx[dirt], y + dy[dirt]  # 새로운 방향으로 이동

    n_lst[y][x] = i  # 현재 위치에 숫자 채우기

    cnt -= 1
    if cnt == 0:  # 방향 바꿈
        bi -= 1
        if bi:
            cnt = tmp
        else:
            bi = 2
            tmp += 1
            cnt = tmp
        dirt = (dirt + 1) % 4  # 방향 전환

# 결과 출력
for row in n_lst:
    print(*row)