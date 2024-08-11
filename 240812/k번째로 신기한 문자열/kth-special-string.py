n, k, T = map(str, input().split())
n, k = int(n), int(k)

n_lst = []

for _ in range(n):
    tmp = input()
    for idx, s in enumerate(T):
        if tmp[idx] != s:
            tmp = ''
            break
    if tmp:
        n_lst.append(tmp)

n_lst.sort()    
print(n_lst[k-1])