n, m = map(int, input().split())
A = [0] + list(map(int, input().split()))

def arrsum(a1, a2):
    return sum(A[a1:a2+1])

for _ in range(m):
    a1, a2 = map(int, input().split())
    print(arrsum(a1, a2))