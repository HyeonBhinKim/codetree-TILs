def is_primenum(x):
    for i in range (2, int(x**0.5)+1):
    	if x % i == 0:
        	return False
    return True

def issumeven(n):
    sumten = 0
    while n >= 10:
        sumten += n%10
        n = n//10
    sumten += n
    
    if sumten % 2:
        return False
    else:
        return True
    
a, b = map(int, input().split())
cnt = 0

for i in range(a, b+1):
    if is_primenum(i):
        if issumeven(i):
            cnt += 1

print(cnt)