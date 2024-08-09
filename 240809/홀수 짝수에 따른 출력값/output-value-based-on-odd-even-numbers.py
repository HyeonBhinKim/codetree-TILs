def twoplus(n):
    if n <= 2:
        return n
    return twoplus(n-2) + n

N = int(input())
print(twoplus(N))