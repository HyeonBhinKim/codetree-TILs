def tnpo(n):
    if n == 1:
        return 0
    
    if n % 2:
        return tnpo(3*n +1) + 1
    else:
        return tnpo(n//2) + 1
    

N = int(input())
print(tnpo(N))