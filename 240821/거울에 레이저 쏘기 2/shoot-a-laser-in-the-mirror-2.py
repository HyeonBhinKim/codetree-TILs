N = int(input())
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1] # 동, 북, 서, 남

# y축 = 행, x축 = 열
def startpoint(N, K):
    K = K - 1
        # return y, x, d 
    if K//N == 3: # 동쪽 +x
        return (N-1)-K%N, 0, 0 # 동 +x
    elif K//N == 2: 
        return N-1, (N-1)-K%N, 3 # -y
    elif K//N == 1: 
        return K%N, N-1, 2  # 서 -x
    else:
        return 0, K%N, 1 # +y

def in_range(x, y):
    return 0 <= x  and x < N and 0 <= y and y < N

    # 동에서 +x \ 보면 북으로 보고 +y right
    # 서 -x \ 남 -y right
    # 남 -y 3 \ 동 +x 0 right
    # 북 +y 1 \ 서 -x 2 right

    # 동 / -y
    # 서 / +y
    # 남 / -x
    # 북 / +x

def dxy_right(x, y, d):
    d = (d+1)%4
    nx, ny = x + dxs[d], y+dys[d]
    return nx, ny, d

def dxy_left(x, y, d):
    d = (d-1+4)%4
    nx, ny = x + dxs[d], y+dys[d]
    return nx, ny, d


def reflect(x, y, d):
    global N
    # print('reflect', x, y, d)
    if not in_range(x, y):
        return 0
    else:
        if n_lst[y][x] == "/": #배열 y축 = 행, x축 = 열
            nx, ny, d = dxy_left(x, y, d)
        else:
            nx, ny, d = dxy_right(x, y, d)
        return reflect(nx, ny, d) + 1



n_lst = [''for _ in range(N)]


for i in range(N):
    strs = input()
    strs = strs.replace('\\', '!') # / = / , \ = !
    n_lst[i] = strs

K = int(input())
y, x, d = startpoint(N, K)

print(reflect(x, y, d))