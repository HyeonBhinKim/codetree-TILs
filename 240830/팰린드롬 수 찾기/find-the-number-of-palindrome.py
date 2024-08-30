def palindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    return False



X, Y = map(int, input().split())

cnt = 0

for i in range(X, Y+1):
    if palindrome(i):
        cnt += 1

print(cnt)