n = int(input())

n_lst = list(map(int, input().split()))

for _ in range(n):
    for i in range(n-1):
        if n_lst[i] > n_lst[i+1]:
            n_lst[i], n_lst[i+1] = n_lst[i+1], n_lst[i]

print(*n_lst)