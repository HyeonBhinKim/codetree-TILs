n_lst = list(map(int, input().split()))
n_lst.sort()

A = n_lst[0]
B = n_lst[1]
C = n_lst[-1] - A - B

print(A, B, C)