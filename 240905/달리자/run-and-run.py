import sys

input = sys.stdin.readline

n = int(input())
a_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))

cnt = 0

moving_lst = [0]*n

for i in range(n):
    moving_lst[i] = a_lst[i] - b_lst[i]


for m in range(n-1):
    for g in range(m+1, n):
        if moving_lst[m] > 0 and moving_lst[g] < 0:
            moving_lst[g] += moving_lst[m]
            cnt += moving_lst[m]*(g-m)
            moving_lst[m] = 0

print(cnt)