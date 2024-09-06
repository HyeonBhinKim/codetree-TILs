def rank(a, b): # A 1, AB 2, B 3 
    if a > b:
        return 1
    elif a == b:
        return 2
    elif a < b:
        return 3


n = int(input())

A = 0
B = 0

ans = 0
for _ in range(n):
    p, score = input().split()
    score = int(score)

    if p == "A":
        if rank(A, B) != rank(A+score, B):
            ans += 1
        A += score
    else:
        if rank(A, B) != rank(A, B+score):
            ans += 1
        B += score
    
print(ans)