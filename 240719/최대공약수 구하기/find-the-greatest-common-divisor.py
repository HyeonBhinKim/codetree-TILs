def gcm(n, m):
    answer = 1
    ngcm = int(n**0.5)
    mgcm = int(m**0.5)
    mini = min(ngcm, mgcm)
    for i in range(1, mini+1):
        if n%i == 0:
            if m%(n//i) == 0:
                answer = max(answer, n//i)
            if m%i == 0:
                answer = max(answer, i)

    print(answer)

a, b = map(int,input().split())
gcm(a, b)