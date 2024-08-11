n = int(input())
n_lst = []

for _ in range(n):
    n_lst.append(input())

n_lst.sort()

for i in n_lst:
    print(i)