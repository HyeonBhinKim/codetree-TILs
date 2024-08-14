n = int(input())

MAX_R = 201
OFFSET = 100

n_lst = [[0]*MAX_R for _ in range(MAX_R)]
ans = 0

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET

    if _:
        if _ % 2:
            for i in range(x1, x2):
                for j in range(y1, y2):
                    if n_lst[i][j] == 0:
                        n_lst[i][j] = 1
                        ans += 1
        
        else:
            for i in range(x1, x2):
                for j in range(y1, y2):
                    if n_lst[i][j] == 1:
                        n_lst[i][j] = 0
                        ans -= 1

    else:
        pass

print(ans)