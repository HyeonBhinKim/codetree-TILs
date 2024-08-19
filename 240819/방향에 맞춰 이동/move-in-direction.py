N = int(input())

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1] # 동, 남, 서, 북

x, y = 0, 0

for _ in range(N):
    d, t = map(str, input().split())
    t = int(t)

    for i in range(t):
        if d == "E":
            x += dx[0]
        elif d == "S":
            y += dy[1]
        elif d == "W":
            x += dx[2]
        else:
            y += dy[3]
    
print(x, y)