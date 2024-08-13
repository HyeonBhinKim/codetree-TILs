N = int(input())
n_lst = []

for i in range(1, N+1):
    h, w = map(int, input().split())
    n_lst.append([h, w, i])

n_lst.sort(key=lambda x:(x[0], -x[1]))

for j in n_lst:
    print(*j)