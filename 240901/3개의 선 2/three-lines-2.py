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
        if dotEA < len(x_lst[j]):
            dotEA = len(x_lst[j])
            where = 'x'
            maxline = j

        if dotEA < len(y_lst[j]):
            dotEA = len(y_lst[j])
            where = 'y'
            maxline = j

    # print("x_lst", x_lst)
    # print("y_lst", y_lst)


    if where == 'x':
        # print('where안임', where)
        for k in x_lst[maxline]:
            y_lst[k].remove(maxline)
        x_lst[maxline] = []
    else:
        # print('where안임', where)
        for k in y_lst[maxline]:
            x_lst[k].remove(maxline)
        y_lst[maxline] = []


# print("x_lst", x_lst)
# print("y_lst", y_lst)
for l in range(11):
    if len(x_lst[l]) != 0 or len(y_lst[l]) !=0:
        print(0)
        break
    if l == 10:
        print(1)