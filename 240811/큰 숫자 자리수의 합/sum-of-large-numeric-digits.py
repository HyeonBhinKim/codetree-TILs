def tds(n):
    if n < 10:
        return n
    return tds(n//10) + n%10
    

n_lst = list(map(int, input().split()))
multi = 1

for i in n_lst:
    multi *= i

print(tds(multi))