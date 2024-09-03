n = int(input())

ab_lst = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(1,10001):
    now = i
    flag = True
    
    for ai, bi in ab_lst:
        now *= 2
        if not (ai <= now <= bi):
            flag = False
            break

    if flag:
        print(i)
        break