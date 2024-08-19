def in_range(x, y, n):
    return 0 <= x and x < n and 0 <= y and y < n


n = int(input())
ans = 0
n_lst = []

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

for _ in range(n):
    tmp = list(map(int, input().split()))
    n_lst.append(tmp)

for i in range(n):
    for j in range(n):
        cnt = 0
        for m in range(4):    
            if in_range(i+dx[m], j+dy[m], n) and n_lst[i+dx[m]][j+dy[m]] == 1:
                cnt +=1
        if cnt >= 3:
            ans += 1

print(ans)