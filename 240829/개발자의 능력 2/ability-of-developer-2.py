n_lst = list(map(int, input().split()))

n_lst.sort()

a = n_lst[0]+n_lst[-1]
b = n_lst[1]+n_lst[-2]
c = n_lst[2]+n_lst[-3]

min_diff = max(a,b,c)-min(a,b,c)

print(min_diff)