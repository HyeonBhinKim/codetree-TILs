n = int(input())

n_lst = list(map(int, input().split()))

for i in range(n-1):
    mini = i
    for j in range(i+1, n):
        if n_lst[mini] > n_lst[j]:
            mini = j
    n_lst[i], n_lst[mini] = n_lst[mini], n_lst[i]



print(*n_lst)