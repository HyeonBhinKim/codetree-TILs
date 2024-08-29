N, B = map(int, input().split())

n_lst = []

for _ in range(N):
    p, s = map(int, input().split())
    tot = p+s
    n_lst.append([tot,p,s])
    
ans = 0

for i in range(N):
    tmp = [n_lst[j]for j in range(N)]
    tmp[i][1] //= 2
    tmp[i][0] = tmp[i][1]+tmp[i][2]

    tmp.sort(key=lambda x :x[0])
    # print(tmp)

    budget = 0
    cnt = 0

    for k in range(N):
        if budget + tmp[k][0] > B:
            break
        budget += tmp[k][0]
        cnt += 1
    ans = max(ans, cnt)

print(ans)