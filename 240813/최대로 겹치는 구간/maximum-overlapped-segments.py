n = int(input())
n_lst = [0]*201

for _ in range(n):
    x1, x2 = map(int, input().split())
    x1, x2 = x1 + 100, x2 + 100
    for i in range(x1, x2):
        n_lst[i] += 1

print(max(n_lst))