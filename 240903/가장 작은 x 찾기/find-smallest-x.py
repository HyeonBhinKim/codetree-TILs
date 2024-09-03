n = int(input())

a1, b1 = map(int, input().split())
ab_lst = [tuple(map(int, input().split())) for _ in range(n-1)]

for i in range(a1, b1+1):
    now = i * 2
    flag = True
    
    for ai, bi in ab_lst:
        now *= 2
        if not (ai <= now <= bi):
            flag = False
            break

    if flag:
        print(i)