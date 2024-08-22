def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
dirt = 0

N, T = map(int, input().split())
strs = input()
n_lst = []

for _ in range(N):
    tmp = list(map(int,input().split()))
    n_lst.append(tmp)

x, y = N//2, N//2

ans = n_lst[y][x]

for i in strs:
    if i == "F":
        nx, ny = x +dx[dirt], y + dy[dirt]
        if in_range(nx, ny):
            x, y = nx, ny
            ans += n_lst[y][x]
    elif i == "R":
        dirt = (dirt+1)%4
    else:
        dirt = (dirt+3)%4

print(ans)