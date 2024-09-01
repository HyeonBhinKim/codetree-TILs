N = int(input())
strs = input()

ans = 0

for i in range(1, N-1):
    flag = False
    for j in range(N-i):
        if flag:
            break
        for k in range(j+1, N-i+1):
            if strs[j:j+i] == strs[k:k+i]:
                ans += 1    
                flag = True
                break
    if ans != i:
        break
        
print(ans+1)