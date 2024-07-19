def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return print(a * b // gcd(a, b))

n, m = map(int, input().split())

lcm(n, m)