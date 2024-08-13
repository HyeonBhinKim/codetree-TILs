n = int(input())
n_lst = [0]*101

for _ in range(n):
    x1, x2 = map(int, input().split())
    for i in range(x1, x2+1):
        n_lst[i] += 1

print(max(n_lst))