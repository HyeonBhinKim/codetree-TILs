def ones(row,col):
    for _ in range(row):
        print('1'*col)

m, n = map(int, input().split())
ones(m,n)