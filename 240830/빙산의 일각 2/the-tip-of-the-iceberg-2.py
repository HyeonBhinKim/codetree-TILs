N = int(input())
h_lst = [int(input())for _ in range(N)]

max_h = max(h_lst)

ans = 0
for sea_level in range(1, max_h):
    cnt = 0
    icing = False
    for h in h_lst:
        if h > sea_level:
            if not icing:
                icing = True
                cnt += 1
        else:
            icing = False
    
    ans = max(cnt, ans)

print(ans)