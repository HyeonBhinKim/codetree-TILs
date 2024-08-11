def hdn(n):
    if n <= 0 :
        return 1
    elif n == 1:
        return 2
    elif n == 2:
        return 4
    
    return (hdn(n-1)*hdn(n-2))%100

N = int(input())
print(hdn(N))