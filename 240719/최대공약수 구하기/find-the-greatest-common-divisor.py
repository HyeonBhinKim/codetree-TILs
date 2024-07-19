def gcm(n, m):
    mini = min(n, m)
    maax = max(n, m)
    answer = 1
    minisqrt = int(mini**0.5)
    for i in range(1, minisqrt+1):
        if mini%i == 0:
            if maax%(mini//i) == 0:
                answer = max(answer, mini//i)
            if maax%i == 0:
                answer = max(answer, i)

    print(answer)

a, b = map(int,input().split())
gcm(a, b)