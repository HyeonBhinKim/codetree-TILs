from collections import deque

N, B = map(int, input().split())
digits = deque()

while True:
    if N < B:
        digits.appendleft(N)
        break
    digits.appendleft(N%B)
    N //= B

for i in digits:
    print(i, end='')