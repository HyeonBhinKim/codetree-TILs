x1, y1, x2, y2 = list(map(int, input().split()))
a1, b1, a2, b2 = list(map(int, input().split()))

minx = min(x1, x2, a1, a2)
maxx = max(x1, x2, a1, a2)
miny = min(y1, y2, b1, b2)
maxy = max(y1, y2, b1, b2)

print((maxx-minx)*(maxy-miny))