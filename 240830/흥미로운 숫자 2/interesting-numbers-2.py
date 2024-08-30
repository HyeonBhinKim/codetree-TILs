def interstednumber(n):
    n_lst = [0]*(n+1)
    cnt_1 = 0
    cnt_m1 = 0
    n = str(n)
    for i in n:
        n_lst[int(i)] += 1
    
    for num in n_lst:
        if num == 1:
            cnt_1 += 1
        elif num > 1:
            cnt_m1 += 1
    
    if cnt_1 == 1 and cnt_m1 == 1:
        return True

    return False


X, Y = map(int, input().split())

cnt = 0

for i in range(X, Y+1):
    if interstednumber(i):
        cnt += 1

print(cnt)