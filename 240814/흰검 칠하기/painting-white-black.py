n = int(input())
n_lst = [[0, 0] for _ in range(200001)]  # 검, 흰
BW_lst =  [''] * 200001
idx = 100000
ans = [0, 0, 0] # 검, 흰, 회 인줄 알았는데 흰, 검, 회 순서네

for _ in range(n):
    x, d = map(str, input().split())
    x = int(x)
    if d =="R":
        for i in range(x): 
            if BW_lst[idx] != 'G':
                if BW_lst[idx] != 'B':
                    n_lst[idx][0] += 1
                    BW_lst[idx] = 'B'
                if n_lst[idx][0] >= 2 and n_lst[idx][1] >= 2:
                    ans[2] += 1
                    BW_lst[idx] = 'G'
            if i == 0:
                idx += 1
            elif i < x-1: 
                idx += 1
    else:
        for i in range(x): 
            if BW_lst[idx] != 'G':
                if BW_lst[idx] != 'W':
                    n_lst[idx][1] += 1
                    BW_lst[idx] = 'W'
                if n_lst[idx][0] >= 2 and n_lst[idx][1] >= 2:
                    ans[2] += 1
                    BW_lst[idx] = 'G'
            if i == 0:
                idx -= 1
            elif i < x-1:
                idx -= 1
    
for i in BW_lst:
    if i == "B":
        ans[1] += 1
    elif i == "W":
        ans[0] += 1

print(*ans)