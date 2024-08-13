from collections import deque

a, b = map(int, input().split())
n = input()

digits = deque()

num = 0
for i in n:
    num = num*a + int(i)

while True:
    if num < b:
        digits.appendleft(num)
        break
    digits.appendleft(num%b)
    num //= b

for i in digits:
    print(i, end='')