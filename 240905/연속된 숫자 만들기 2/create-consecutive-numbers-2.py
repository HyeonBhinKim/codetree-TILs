n_lst = list(map(int,input().split()))

notcontinue = True

if n_lst[0]+2 == n_lst[1]+1 == n_lst[2]:
    print(0)
    notcontinue = False

else:
    for i in range(1,3):
        if n_lst[i] == n_lst[i-1]+2:
            print(1)
            notcontinue = False
            break
    
if notcontinue:
    print(2)