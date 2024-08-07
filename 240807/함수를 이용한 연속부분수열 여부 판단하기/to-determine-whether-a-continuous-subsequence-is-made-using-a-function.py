n1, n2 = map(int, input().split())

n1_lst = input()
n2_lst = input()

n1_lst = n1_lst.replace(" ", '')
n2_lst = n2_lst.replace(" ", '')

if n1 < n2 :
    print("No")
else:
    if n2_lst in n1_lst:
        print("Yes")
    else:
        print("No")