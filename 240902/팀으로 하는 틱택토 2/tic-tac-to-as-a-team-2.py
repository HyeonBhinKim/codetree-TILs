n_lst = [(list((map(int, input()))))for _ in range(3)]

ans = 0

#   123.    456.    789.    147.    258.    369.    159.        357.
#   0:012   1:012   2:012   012:0   012:1   012:2   00:11:22    02:11:20

winning_lst = [
    [(0,0),(0,1),(0,2)],
    [(1,0),(1,1),(1,2)],
    [(2,0),(2,1),(2,2)],
    [(0,0),(1,0),(2,0)],
    [(0,1),(1,1),(2,1)],
    [(0,2),(1,2),(2,2)],
    [(0,0),(1,1),(2,2)],
    [(0,2),(1,1),(2,0)]
    ]

comb = []

for n in range(8): 
    numbers = [0]*10
    cnt2 = 0
    cnt1 = 0
    each2 = 0
    each1 = 0
    for y,x in winning_lst[n]:
        numbers[n_lst[y][x]] += 1
    
    for each in numbers:
        if each == 2:
            cnt2 += 1
            each2 = each
        elif each == 1:
            cnt1 += 1
            each1 = each    

    if cnt2 == 1 and cnt1 == 1:
        if not (each1, each2) in comb:
            ans += 1
            comb.append([each1, each2])


print(ans)