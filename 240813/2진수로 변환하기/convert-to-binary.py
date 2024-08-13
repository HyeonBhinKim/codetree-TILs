from collections import deque

n = int(input())
digits = deque()

while True:
    if n < 2:
        digits.appendleft(n)
        break
    digits.appendleft(n%2)
    n //=2

for digit in digits:
    print(digit, end="")