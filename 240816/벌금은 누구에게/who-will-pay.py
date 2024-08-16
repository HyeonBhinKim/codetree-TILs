N, M, K =  map(int, input().split())
MAX_N = 101

n_lst = [0 for _ in range(MAX_N)]

for _ in range(M):
    n = int(input())
    n_lst[n] += 1
    if n_lst[n] == K:
        print(n)
        break
    elif _ == M-1:
        print(-1)