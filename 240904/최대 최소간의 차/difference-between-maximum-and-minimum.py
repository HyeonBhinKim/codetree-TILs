import sys

n, k = map(int, input().split())
n_lst = list(map(int, input().split()))
max_n = max(n_lst)
min_n = min(n_lst)

ans = sys.maxsize

# 기준
for i in range(min_n, max_n+1):
    tmp = 0
    for num in n_lst:
        if i <= num <= i+k:
            continue
        elif num < i:
            tmp += abs(i - num)
        else:
            tmp += abs(i+k - num)
    
    ans = min(ans, tmp)

print(ans)