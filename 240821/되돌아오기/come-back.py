# 변수 선언 및 입력
N = int(input())

# 시작 위치를 기록합니다.
y, x = 0,0

# 동, 서, 남, 북 순으로 dx, dy를 정의합니다.
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

# 답을 저장합니다.
ans = -1

# 지금까지 걸린 시간을 기록합니다.
elapsed_time = 0

# move_d 방향으로 t 만큼 이동하는 함수입니다.
# 만약 시작지에 도달하면 true를 반환합니다.
def move(move_d,t):
    global x, y
    global ans, elapsed_time
    
    for _ in range(t):
        y, x = y + dy[move_d], x + dx[move_d]

        # 이동한 시간을 기록합니다.
        elapsed_time += 1

        # 시작지로 다시 돌아오면,
        if x == 0 and y == 0:
            # 답을 갱신해줍니다.
            ans = elapsed_time
            return True
        
    return False


# 움직이는 것을 진행합니다.
for _ in range(n):
    d, t = tuple(input.split())
    t = int(t)
    # 각 방향에 맞는 번호를 붙여줍니다.
    if d = "E":
        move_d = 0
    elif d = "S":
        move_d = 1
    elif d = "N":
        move_d = 2
    else:
        move_d = 3


    # 주어진 방향대로 t 만큼 위치를 이동해봅니다.
    done = move(move_d,t)

    # 시작 위치에 도달했다면, 종료합니다.
    if done:
        break

print(ans)