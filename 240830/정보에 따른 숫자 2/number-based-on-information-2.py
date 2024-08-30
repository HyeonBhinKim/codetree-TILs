T, a, b = map(int, input().split())

# S는 1, N은 2
# alpha_lst = [0]*1001

s_lst = []
n_lst = []
for _ in range(T):
    alpha, loc = input().split()
    loc = int(loc)
    if a<=loc<=b and alpha =='S':
        s_lst.append(loc)
    elif a<=loc<=b and alpha =='N':
        n_lst.append(loc)

cnt = 0

for i in range(a, b+1):
    for s in s_lst:
        for n in n_lst:
            if abs(s-i) <= abs(n-i):
                cnt += 1
    
print(cnt)
    # for j in range(a, b+1):
    #     if alpha_lstp[j] == 1:
    #         s_lst.append(j)
    #     elif alpha_lst[j] == 2:
    #         n_lst.append(j)