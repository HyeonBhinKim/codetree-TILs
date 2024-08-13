N = int(input())
n_lst = []

for i in range(1, N+1):
    x, y = map(int, input().split())
    distance = abs(x) + abs(y)
    n_lst.append([i, distance])

n_lst.sort(key=lambda x:(x[1],x[0]))

for j in n_lst:
    print(j[0])