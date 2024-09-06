import sys

n = int(input())
n_lst = list(map(int, input().split()))
n_lst.sort()
abs_lst = sorted(n_lst, key=abs)

ans = -sys.maxsize

if 0 in n_lst:
    ans = 0
if n_lst[-3] > 0 and n_lst[-2] > 0 and n_lst[-1] > 0:
    ans = max(ans, n_lst[-3]*n_lst[-2]*n_lst[-1])
if n_lst[0] < 0 and n_lst[1] <0 and n_lst[-1] > 0:
    ans = max(ans, n_lst[0]*n_lst[1]*n_lst[-1])

ans = max(ans, abs_lst[0]*abs_lst[1]*abs_lst[2])

print(ans)