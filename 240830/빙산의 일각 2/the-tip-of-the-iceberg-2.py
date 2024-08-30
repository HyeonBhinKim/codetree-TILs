N = int(input())

h_lst = [int(input())for _ in range(N)]

max_h = max(h_lst)

cnt = 0

for i in range(1, max_h):
    tmp = 0
    for j in range(1, N):
        if h_lst[j-1]-i > 0 and h_lst[j]-i == 0:
           tmp += 1
        if j == N-1 and h_lst[j]-i > 0:
            tmp += 1

    cnt = max(cnt, tmp) 

print(cnt)