import sys

n = int(input())
n_lst = list(map(int, input().split()))

ans = -sys.maxsize

for i in range(n-2):
    for j in range(i+1, n-1):
        cnt = 0
        for k in range(j+1, n):
            if n_lst[i] < 0:
                cnt +=1
            if n_lst[j] < 0:
                cnt +=1
            if n_lst[k] < 0:
                cnt +=1
            if not cnt%2:
                tmp = n_lst[i]*n_lst[j]*n_lst[k]
                ans = max(ans, tmp)


print(ans)