def interstednumber(n):
    n_lst = {}
    n = str(n)
    for i in n:
        if int(i) in n_lst:
            n_lst[int(i)] += 1
        else:
            n_lst[int(i)] = 1
    # if len(n_lst) > 2:
    #     return False
    cnt1 = 0
    cntm = 0
    for i in n_lst:
        if i == 1:
            cnt1 += 1
        else:
            cntm += 1
        if cnt1 == 1 and cntm == 1:
            return True
    return False


X, Y = map(int, input().split())

cnt = 0

for i in range(X, Y+1):
    if interstednumber(i):
        cnt += 1

print(cnt)