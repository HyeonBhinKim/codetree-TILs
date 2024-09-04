a, b = map(int, input().split())
c, d = map(int, input().split())

clean = [0]*101

for i in range(a+1, b+1):
    clean[i] = 1
for j in range(c+1, d+1):
    clean[j] = 1

print(sum(clean))