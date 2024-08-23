a = list(input())

if '0' in a:
    a[a.index('0')] = '1'
else:
    a[len(a)-1] = '0'

ans = 0

for i in a:
    ans = ans*2 + int(i)

print(ans)