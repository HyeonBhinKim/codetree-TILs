N, C, G, H = map(int, input().split())

n_lst = [tuple(map(int, input().split()))for _ in range(N)]

max_work = 0

for i in range(1001):
    tmp_work = 0
    for j in n_lst:
        Ta, Tb = j
        if i < Ta:
            tmp_work += C
        elif i <= Tb:
            tmp_work += G
        else:
            tmp_work += H
    
    max_work = max(max_work, tmp_work)

print(max_work)