X, Y = map(int, input().split())

ans = 0

# for i in range(X, Y+1):
#     tmp = 0
#     while i:
#         tmp += i%10
#         i //= 10
#     ans = max(ans, tmp)

def digit_sum(n):
    if n<10:
        return n
    
    return digit_sum(n//10)+n%10

for i in range(X, Y+1):
    ans = max(ans, digit_sum(i))

print(ans)