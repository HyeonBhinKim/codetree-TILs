strs = input()
ls = len(strs)

cnt = 0
for i in range(ls-1):
    if strs[i:i+2] == "((":
        for j in range(i+1, ls-1):
            if strs[j:j+2] == "))":
                cnt += 1

print(cnt)