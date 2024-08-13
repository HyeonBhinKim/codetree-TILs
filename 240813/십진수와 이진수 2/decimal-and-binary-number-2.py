from collections import deque

N = input()

digits = deque()

num = 0

for i in N:
    num = num*2 + int(i)

N = num*17

while True:
    if N < 2:
        digits.appendleft(N)
        break
    digits.appendleft(N%2)
    N //= 2

for i in digits:
    print(i, end='')