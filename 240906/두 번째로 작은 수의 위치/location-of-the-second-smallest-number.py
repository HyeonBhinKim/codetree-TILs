n = int(input())

n_lst = list(map(int, input().split()))

sortlst = sorted(n_lst)

lowvalue = sortlst[0]

secondvalue = 0
cnt = 0
ans = -1

for i in range(n):
    if sortlst[i] == lowvalue:
        continue
    else:
        if not cnt:
            cnt += 1
            secondvalue = sortlst[i]
        else:
            if secondvalue != sortlst[i]:
                break
            else:
                cnt += 1
                break

if cnt == 1:
    ans = n_lst.index(secondvalue) + 1

print(ans)