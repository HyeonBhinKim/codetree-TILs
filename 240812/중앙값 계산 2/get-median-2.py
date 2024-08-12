def middlevalue(n, arr):
    oddvalue = []
    for i in range(1, n+1, 2):
        tmp = sorted(arr[:i])
        oddvalue.append(tmp[(i//2)])

    return oddvalue


N = int(input())
n_lst = list(map(int, input().split()))

ans = middlevalue(N, n_lst)

print(*ans)