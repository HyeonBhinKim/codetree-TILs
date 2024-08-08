def fivo(n):
    if n <= 0:
        return 0
    elif n <= 2:
        return 1
    
    return fivo(n-1)+fivo(n-2)

N = int(input())
print(fivo(N))