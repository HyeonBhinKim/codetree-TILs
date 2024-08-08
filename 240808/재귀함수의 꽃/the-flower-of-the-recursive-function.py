def numbering(n):
    if n == 0:
        return
    print(n, end=' ')
    numbering(n-1)
    print(n, end=' ')


N = int(input())
numbering(N)