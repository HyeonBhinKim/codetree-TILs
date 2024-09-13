n = int(input())
n_lst = list(map(int, input().split()))

for i in range(1,n):
    key = n_lst[i]
    # print(key, "key")
    j = i - 1
    while j >= 0 and n_lst[j] > key:
        # print(n_lst[j], n_lst[j+1], 'n_lst[j], n_lst[j+1]')
        n_lst[j + 1] = n_lst[j]
        # print(n_lst[j+1],'n_lst[j+1]')        
        # print(j, 'j')
        j -= 1
        # print(j, 'j')

    # print(j+1,n_lst[j+1], 'n_lst[j+1]')
    n_lst[j+1] = key


print(*n_lst)