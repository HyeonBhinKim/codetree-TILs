N = int(input())
pigeons = [0]*(11)
moved = [False]*(11)

ans = 0
for _ in range(N):
    pigeon, loc = map(int, input().split())
    if moved[pigeon] == False:
        moved[pigeon] = True
        pigeons[pigeon] = loc
    else:
        if pigeons[pigeon] != loc:
            ans += 1
            pigeons[pigeon] = loc

print(ans)