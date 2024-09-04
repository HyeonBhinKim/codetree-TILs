n = int(input())

n_lst = [tuple(map(int, input().split()))for _ in range(n)]

overlap = False

for i in range(n):
    new_lst = n_lst[:i]+n_lst[i+1:n]
    overlaps = [0]*101
    for x1, x2 in new_lst:
        for o in range(x1, x2+1):
            overlaps[o] += 1
    
    if max(overlaps) == n-1:
        overlap = True
        break

if overlap:
    print("Yes")
else:
    print("No")