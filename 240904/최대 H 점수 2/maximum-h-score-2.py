N, L = map(int, input().split())
n_lst = list(map(int, input().split()))

ans = 0
# H값 1~100, 0은 어차피 통과
for H in range(1, 101):
    cnt = 0
    l_cnt = 0
    for num in range(N):
        if num >= H:
            cnt += 1
        elif l_cnt < L and num + 1 >= H:
            cnt += 1
            l_cnt += 1
        
        if cnt >= H:
            ans = H
            break

print(ans)