n_lst = list(map(int, input().split()))

if n_lst[0]+2 == n_lst[1]+1 == n_lst[2]:
    print(0)
elif n_lst[-1] - n_lst[1] >= n_lst[1] - n_lst[0]:
    print(n_lst[-1] - n_lst[1] - 1)
else:
    print(n_lst[1] - n_lst[0] - 1)