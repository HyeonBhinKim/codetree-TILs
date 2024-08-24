def who_win(go, i, j, who):
    win = [who, who, who, who, who]
    
    # 세로 검사
    if i <= N - 5 and go[i][j] == who and all(go[i+k][j] == who for k in range(5)):
        return i + 3, j + 1, who, True
    
    # 가로 검사
    if j <= N - 5 and go[i][j:j + 5] == win:
        return i + 1, j + 3, who, True
    
    # 대각선 검사
    if i <= N - 5 and j <= N - 5 and all(go[i + k][j + k] == who for k in range(5)):
        return i + 3, j + 3, who, True
    
    # 반대 대각선 검사
    if i <= N - 5 and j >= 4 and all(go[i + k][j - k] == who for k in range(5)):
        return i + 3, j - 1, who, True

    return 0, 0, 0, False


N = 19
go = [list(map(int, input().split())) for _ in range(N)]

flag = False
who = 0
y, x = 0, 0

for i in range(N):
    if flag:
        break
    for j in range(N):
        if go[i][j] != 0:
            y, x, who, flag = who_win(go, i, j, go[i][j])
        if flag:
            break

if flag:
    print(who)
    print(y, x)  # y는 세로줄, x는 가로줄
else:
    print(0)