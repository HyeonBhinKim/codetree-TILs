N, L = map(int, input().split())
n_lst = list(map(int, input().split()))

ans = 0
# 기준 H값 1~100, 0은 어차피 통과 // 어차피 N개 이상으로는 기준을 벗어날 필요가 없다.
for H in range(1, N+1):
    cnt = 0
    l_cnt = 0
    for num in n_lst:
        if num >= H:
            cnt += 1
        elif l_cnt < L and num + 1 >= H:
            cnt += 1
            l_cnt += 1

        if cnt >= H:
            ans = H
            break

print(ans)