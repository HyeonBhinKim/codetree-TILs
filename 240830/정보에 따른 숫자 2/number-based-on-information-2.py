T, a, b = map(int, input().split())

# S는 1, N은 2
alpha_lst = [0]*1001

for _ in range(T):
    alpha, loc = input().split()
    loc = int(loc)
    if alpha =='S':
        alpha_lst[loc] = 1
    else:
        alpha_lst[loc] = 2

cnt = 0

for i in range(a, b+1):
    nears = 1001
    nearn = 1001
    for j in range(1001):
        if alpha_lst[j] == 1 and abs(i-j) < nears:
            nears = abs(i-j)
        elif alpha_lst[j] == 2 and abs(i-j) < nearn:
            nearn = abs(i-j)
    if abs(i-nears) <= abs(i-nearn):
        cnt += 1

print(cnt)