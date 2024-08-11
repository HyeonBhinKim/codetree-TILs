n = int(input())
n_lst = list(map(int, input().split()))

def lcm(a, b):
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    return a * b // gcd

def find(n):
    if n == 0:
        return n_lst[n]
    
    return lcm(find(n-1), n_lst[n])


print(find(n-1))