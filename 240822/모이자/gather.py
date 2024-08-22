n = int(input())
n_lst = list(map(int, input().split()))

minimum = 10000

for i in range(n):
    tmp = 0
    for j in range(n):
        tmp += abs(n_lst[j]*(j-i))
    minimum = min(minimum, tmp)

print(minimum)