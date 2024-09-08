n_lst = list(map(int, input().split()))
n_lst.sort()
A, B, C = n_lst[0], n_lst[1], n_lst[2]
D = n_lst[-1] - A - B - C

print(A, B, C, D)