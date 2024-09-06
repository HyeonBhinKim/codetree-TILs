import sys

n = int(input())
n_lst = list(map(int, input().split()))
n_lst.sort()

ans = -sys.maxsize

if n_lst[-3] > 0 and n_lst[-2] > 0 and n_lst[-1] > 0:
    ans = max(ans, n_lst[-3]*n_lst[-2]*n_lst[-1])
if n_lst[-1] > 0 and n_lst[0] < 0 and n_lst[1] <0:
    ans = max(ans, n_lst[0]*n_lst[1]*n_lst[-1])

print(ans)