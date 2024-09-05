A, B, x, y = map(int, input().split())

if A > B:
    A, B = B, A

if x > y:
    x, y = y, x

ab = B-A
xy = y-x

ax = abs(A-x)
by = abs(B-y)

if ab < ax+by:
    print(ab)
else:
    print(ax+by)