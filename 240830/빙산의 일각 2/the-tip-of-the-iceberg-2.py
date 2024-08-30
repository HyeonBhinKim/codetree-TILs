N = int(input())
h_lst = [int(input())for _ in range(N)]

max_h = max(h_lst)

cnt = 0
for i in range(1, max_h):
    tmp = 0
    icing = False
    for j in h_lst:
        if j > i:
            if not icing:
                icing = True
                tmp += 1
        else:
            icing = False
    
    cnt = max(cnt, tmp)

print(cnt)