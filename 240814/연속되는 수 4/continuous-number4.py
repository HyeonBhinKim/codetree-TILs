N = int(input())

n_lst = [int(input())for _ in range(N)]

ans, cnt = 0, 0

for i in range(N):
    if i > 0 and n_lst[i] > n_lst[i-1]:
        cnt += 1
    else:
        cnt = 1
    
    ans = max(ans, cnt)

print(ans)