N = int(input())
x_lst = [[]for _ in range(11)]
y_lst = [[]for _ in range(11)]

for _ in range(N):
    x, y = map(int, input().split())
    x_lst[x].append(y)
    y_lst[y].append(x)

for i in range(3):
    maxline = 0
    dotEA = 0
    where = ''
    for j in range(11):
        if dotEA < (len(x_lst[j]) or len(y_lst[j])):
            if len(x_lst[j]) > len(y_lst[j]):
                dotEA = len(x_lst[j])
                where = 'x'
            else:
                dotEA = len(y_lst[j])
                where = 'y'
            maxline = j

    if where == 'x':
        for k in x_lst[maxline]:
            y_lst[k].remove(maxline)
        x_lst[maxline] = []
    else:
        for k in y_lst[maxline]:
            x_lst[k].remove(maxline)
        y_lst[maxline] = []



for l in range(11):
    if len(x_lst[l]) != 0 or len(y_lst[l]) !=0:
        print(-1)
        break
    if l == 10:
        print(1)