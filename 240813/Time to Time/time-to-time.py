def time(a, b, c, d):
    ca = c - a
    db = d - b
    return 60*ca + db

a, b, c, d = map(int, input().split())

print(time(a,b,c,d))