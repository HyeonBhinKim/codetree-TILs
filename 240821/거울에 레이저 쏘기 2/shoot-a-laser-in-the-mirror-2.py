dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1] # 동, 북, 서, 남

# y축 = 행, x축 = 열
def startpoint(N, K):
    K -= 1
        # return y, x, d 
    if K//N == 3:
        return (N-1)-K%N, 0, 0 # 동
    elif K//N == 2:
        return N-1, K%N, 1 # 북
    elif K//N:
        return K%N, N-1, 2 # 서
    else:
        return 0, (N-1)-K%N, 3 # 남

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

    # 동 / 북
    # 서 / 남
    # 남 \ 동
    # 북 \ 서

    # 동 \ 남
    # 서 \ 북
    # 남 / 서
    # 북 / 동

def dxy_right(x, y, d):
    d = (d+1)%4
    nx, ny = x + dxs[d], y+dys[d]
    return nx, ny, d

def dxy_left(x, y, d):
    d = (d-1+4)%4
    nx, ny = x + dxs[d], y+dys[d]
    return nx, ny, d


def reflect(x, y, d):
    # print('reflect', x, y, d)
    if not in_range(x, y):
        return 0
    else:
        if n_lst[y][x] == "/": #배열 y축 = 행, x축 = 열
            if d == 0 or d == 2:
                nx, ny, d = dxy_right(x, y, d)
            else:
                nx, ny, d = dxy_left(x, y, d)
            return reflect(nx, ny, d) + 1
        else:
            if d == 1 or d == 3:
                nx, ny, d = dxy_right(x, y, d)
            else:
                nx, ny, d = dxy_left(x, y, d)
            return reflect(nx, ny, d) + 1


N = int(input())

n_lst = [''for _ in range(N)]


for i in range(N):
    strs = input()
    strs = strs.replace('\\', '!') # / = / , \ = !
    n_lst[i] = strs

K = int(input())

y, x, d = startpoint(N, K)

print(reflect(x, y, d))