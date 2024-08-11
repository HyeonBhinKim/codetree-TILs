n, k, T = map(str, input().split())
n, k = int(n), int(k)

n_lst = []

# a가 b로 시작하는지를 확인합니다.
def starts_with(a, b):
    # b의 길이가 더 길 수는 없습니다.
    if len(a) < len(b):
        return False
    
    # b의 길이만큼 살펴보며, a와 문자열이 완벽히 동일한지 확인합니다.
    return a[:len(b)] == b

for _ in range(n):
    word = input()
    if starts_with(word, T):
        n_lst.append(word)

n_lst.sort()    
print(n_lst[k-1])