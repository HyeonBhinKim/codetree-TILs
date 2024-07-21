def ThrSixNine(n,m):
    cnt = 0
    for i in range(n, m+1):
        if i%3 == 0 or any(digit in str(i) for digit in ("3", "6", "9")):
            cnt += 1
    return cnt


a, b = map(int, input().split())

print(ThrSixNine(a,b))