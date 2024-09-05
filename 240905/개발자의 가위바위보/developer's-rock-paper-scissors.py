N = int(input())
    #     11 12 13  21 22 23 31 32 33 
RSP_lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for _ in range(N):
    p1, p2 = map(int, input().split())
    if p1 == p2:
        continue
    elif p1 == 1:
        RSP_lst[p2-1] += 1
    elif p1 == 2:
        RSP_lst[p1+p2] += 1
    else:
        RSP_lst[p2+5] += 1
  
    # 12 23 31
    # 13 32 21

if RSP_lst[1] + RSP_lst[5] + RSP_lst[6] >= RSP_lst[2] + RSP_lst[3] + RSP_lst[7]:
    print(RSP_lst[1] + RSP_lst[5] + RSP_lst[6])
else:
    print(RSP_lst[2] + RSP_lst[3] + RSP_lst[7])