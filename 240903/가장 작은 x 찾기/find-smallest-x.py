n = int(input())

ab_lst = [tuple(map(int, input().split())) for _ in range(n-1)]

for i in range(10001):
    now = i
    flag = True
    
    for ai, bi in ab_lst:
        now *= 2
        if not (ai <= now <= bi):
            flag = False
            break

    if flag:
        print(i)