N = int(input())

def numbering(n):
    if n == 0:
        return
    
    numbering(n-1)
    print(n, end=" ")
    if n==N:
        print()
        numbering2(n)

def numbering2(n):
    if n == 0:
        return
    
    print(n, end=" ")
    numbering2(n-1)



numbering(N)