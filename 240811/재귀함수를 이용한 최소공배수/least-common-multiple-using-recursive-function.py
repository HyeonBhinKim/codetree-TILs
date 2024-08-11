n = int(input())
n_lst = list(map(int, input().split()))

def lcm(a, b):
    for i in range(max(a,b), a*b+1):
        if i%a == 0 and i%b == 0:
            return i

def find(n):
    if n == 0:
        return n_lst[n]
    
    return lcm(find(n-1), n_lst[n])


print(find(n-1))