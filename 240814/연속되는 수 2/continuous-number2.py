N = int(input())

n_lst = [0] * 1001
targets = ''

for _ in range(N):
    target = input()
    targets += target

tmp = ''
cnt = 1

for i in range(N):
    if i == 0 or targets[i] == targets[i-1]:
        cnt += 1
    
    else:
        cnt = 1
    
    if n_lst[i] < cnt:
        n_lst[i] = cnt

        

print(max(n_lst))