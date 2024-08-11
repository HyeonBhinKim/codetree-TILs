n, k, T = map(str, input().split())
n, k = int(n), int(k)

n_lst = []

def starts_with(a, b):
    if len(a) < len(b):
        return False
    
    return a[:len(b)] == b

for _ in range(n):
    tmp = input()
    if starts_with(tmp, T):
        n_lst.append(tmp)

n_lst.sort()

print(n_lst[k-1])