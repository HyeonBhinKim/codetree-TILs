import sys
from itertools import combinations


n = int(input())
n_lst = list(map(int, input().split()))

ans = -sys.maxsize

for ns in combinations(n_lst,3):
    i, j, k = ns
    ans = max(ans, i*j*k)

print(ans)