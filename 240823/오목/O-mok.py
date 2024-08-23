def who_win(go, i, j, who):
    win = [who, who, who, who, who]
    who_col = [go[i][j],go[i+1][j],go[i+2][j],go[i+3][j],go[i+4][j]]
    who_diag = [go[i][j],go[i+1][j+1],go[i+2][j+2],go[i+3][j+3],go[i+4][j+4]]
    if go[i][j:j+5] == win:
        return i+3, j+3, who, True
    elif who_col == win:
        return i+3, j+3, who, True
    elif who_diag == win:
        return i+3, j+3, who, True
    return 0, 0, 0, False


N = 19
# go = list(map(int, input().split()) for _ in range(N))
go = [list(map(int, input().split())) for _ in range(N)]

flag = False

who = 0
y, x = 0, 0

for i in range(N-5):
    if flag:
        break
    for j in range(N-5):
        if go[i][j] != 0:
           y, x, who, flag = who_win(go, i, j, go[i][j])
        if flag:
            break
if flag:
    print(who)
    print(x, y) # x인 가로줄부터 출력
else:
    print(who)