def sumfact(n):
    if n == 1:
        return 1
    
    return sumfact(n-1)+n

N = int(input())

print(sumfact(N))