N = int(input())

scam = [list(map(int,input().split()))for _ in range(N)]

ans = 0
for i in range(1, 4): # 1~3
    rock = [0, 0, 0, 0]
    rock[i] = 1
    cnt = 0
    for a, b, c in scam:
        rock[a], rock[b] = rock[b], rock[a]
        if rock[c] == 1:
            cnt += 1
    ans = max(ans, cnt)

print(ans)