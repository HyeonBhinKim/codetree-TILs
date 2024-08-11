def strangeN(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2    
    return strangeN(n//3)+strangeN(n-1)


N = int(input())
print(strangeN(N))