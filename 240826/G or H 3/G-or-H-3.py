N, K = map(int, input().split())

MAX_N = 10001
n_lst = [0] * MAX_N
ans = 0

for _ in range(N):
    loc, spel = tuple(input().split())
    loc = int(loc)
    if spel == 'G':
        n_lst[loc] = 1
    else:
        n_lst[loc] = 2

for i in range(1, MAX_N-K+1):
    tmp = sum(n_lst[i:i+K+1])
    ans = max(ans, tmp)

print(ans)