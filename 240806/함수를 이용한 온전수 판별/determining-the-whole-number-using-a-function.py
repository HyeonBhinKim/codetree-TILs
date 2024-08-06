def perfectnumb(n):
    if n % 2 and (n%10) != 5 and (n % 3 != 0 or n % 9 ==0):
        return True
    else:
        return False

a, b = map(int, input().split())
cnt = 0

for i in range(a, b+1):
    if perfectnumb(i):
        cnt += 1

print(cnt)