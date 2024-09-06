import sys

n = int(input())
n_lst = list(map(int, input().split()))
n_lst.sort()
abs_lst = sorted(n_lst, key=abs)

ans = -sys.maxsize

if n_lst[-3] > 0 and n_lst[-2] > 0 and n_lst[-1] > 0:
    ans = max(ans, n_lst[-3]*n_lst[-2]*n_lst[-1])
if n_lst[0] < 0 and n_lst[1] <0 and n_lst[-1] > 0:
    ans = max(ans, n_lst[0]*n_lst[1]*n_lst[-1])

ans = max(ans, abs_lst[0]*abs_lst[1]*abs_lst[2]) # 어차피 음수밖에 안나오는데, 0이 있으면 그게 최댓값

print(ans)