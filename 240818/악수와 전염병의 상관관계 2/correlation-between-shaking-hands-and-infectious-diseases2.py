N, K, P, T = map(int, input().split())
MAX_N = N + 1
n_lst = [0 for _ in range(MAX_N)] # 감염목록
n_lst[P] = 1
hs_lst = [0 for _ in range(MAX_N)] # 악수횟수

handshake = [0]*251

for _ in range(T):
    t, x, y = map(int, input().split())
    handshake[t] = [x, y]

for i in handshake:
    if i:
        # 감염되어있으면 악수 횟수 +1
        if n_lst[i[0]]:
            hs_lst[i[0]] += 1
        if n_lst[i[1]]:
            hs_lst[i[1]] += 1

        # i[0]이 감염되어있고 K번 이하로 악수했으면 i[1]을 감염
        if n_lst[i[0]] and hs_lst[i[0]] <= K:
            n_lst[i[1]] = 1

        # i[1]이 감염되어있고 K번 이하로 악수했으면 i[0]을 감염
        if n_lst[i[1]] and hs_lst[i[1]] <= K:
            n_lst[i[0]] = 1
            
        
n_lst = n_lst[1:MAX_N+1]

for i in n_lst:
    if i:
        print(1, end='')
    else:
        print(0, end='')