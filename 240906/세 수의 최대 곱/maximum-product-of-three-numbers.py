import sys

n = int(input())
n_lst = list(map(int, input().split()))
n_lst.sort()

ans = -sys.maxsize

if ans[-3] > 0 and ans[-2] > 0 and ans[-1] > 0:
    ans = max(ans, ans[-3]*ans[-2]*ans[-1])
if ans[-1] > 0 and ans[0] < 0 and ans[1] <0:
    ans = max(ans, ans[0]*ans[1]*ans[-1])

print(ans)