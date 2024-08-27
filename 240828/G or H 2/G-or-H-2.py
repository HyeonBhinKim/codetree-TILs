N = int(input())

MAX_N = 101
n_lst = [0] * MAX_N
min_loc = 101
max_loc = 0
ans = 0

for _ in range(N):
    loc, spel = tuple(input().split())
    loc = int(loc)
    max_loc = max(max_loc, loc)
    min_loc = min(min_loc, loc)
    if spel == 'G':
        n_lst[loc] = 1
    else:
        n_lst[loc] = -1

for i in range(min_loc, max_loc+2):
    for j in range(min_loc, max_loc+2):
        if ((1 or -1) in n_lst[i:j+1]) and sum(n_lst[i:j+1]) == 0:
            ans = j - i

print(ans)