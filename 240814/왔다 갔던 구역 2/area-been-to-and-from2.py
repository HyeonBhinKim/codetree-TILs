n = int(input())
n_lst = [0]*201
idx = 100
ans = 0

for _ in range(n):
    x, d = map(str, input().split())
    if d == 'R':
        for i in range(int(x)):
            if idx == 200:
                idx = -1
            n_lst[idx] += 1
            if n_lst[idx] == 2:
                ans += 1
            idx += 1
    else:
        for i in range(int(x)):
            if idx == -201:
                idx = 0
            idx -= 1
            n_lst[idx] += 1
            if n_lst[idx] == 2:
                ans += 1

print(ans)