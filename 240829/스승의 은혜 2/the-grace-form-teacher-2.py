N, B = map(int, input().split())

n_lst = [int(input())for _ in range(N)]

n_lst.sort()
ans = 0

for i in range(N):
    n_lst[i] //= 2
    cnt = 0
    tmp = 0
    for k in range(N):
        cnt += 1
        tmp += n_lst[k]
        if tmp > B:
            cnt -= 1
            break
    ans = max(ans, cnt)
            
    n_lst[i] *= 2

print(ans)