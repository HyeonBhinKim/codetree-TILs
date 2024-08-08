def onetime(n):
    if n == 1:
        return 0
    
    if n % 2:
        return onetime(n//3) + 1
    else:
        return onetime(n//2) + 1


N = int(input())
print(onetime(N))