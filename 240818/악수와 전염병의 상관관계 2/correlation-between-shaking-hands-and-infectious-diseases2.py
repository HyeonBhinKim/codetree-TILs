N, K, P, T = map(int, input().split())
MAX_N = N + 1
n_lst = [0 for _ in range(MAX_N)]
n_lst[P] = K + 1

handshake = [0]*251

for _ in range(T):
    t, x, y = map(int, input().split())
    handshake[t] = [x, y]

for i in handshake:
    if i:
        if n_lst[i[0]] > 1 or n_lst[i[1]] > 1:
            if n_lst[i[0]] > 1 and n_lst[i[1]] > 1:
                n_lst[i[0]] -= 1
                n_lst[i[1]] -= 1
            elif n_lst[i[0]] > 1 and n_lst[i[1]] == 0:
                n_lst[i[0]] -= 1
                n_lst[i[1]] = K + 1
            elif n_lst[i[0]] == 0 and n_lst[i[1]] > 1:
                n_lst[i[0]] = K + 1
                n_lst[i[1]] -= 1
        
n_lst = n_lst[1:MAX_N+1]

for i in n_lst:
    if i >= 1:
        print(1, end='')
    else:
        print(0, end='')