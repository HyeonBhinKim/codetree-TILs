def dmp(m, lst):
    ans = 0
    while m >= 1:
        ans += lst[m-1]
        if m % 2:
            m -= 1
        else:
            m //= 2

    return ans



n, m = map(int, input().split())
A = list(map(int, input().split()))

print(dmp(m, A))