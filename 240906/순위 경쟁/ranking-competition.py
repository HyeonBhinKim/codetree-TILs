def rank(a, b, c): # a 1, ab 2, b 3, bc 4, c 5, ac 6, abc 7
    if a > c:
        if a > b:
            return 1
        if a == b:
            return 2
    elif b > a:
        if b > c: 
            return 3
        if b == c:
            return 4
    elif c > b:
        if c > a:
            return 5
        if c == a:
            return 6
    elif a == b == c:
        return 7

    


n = int(input())

A, B, C = 0, 0, 0

ans = 0
for _ in range(n):
    p, score = input().split()
    score = int(score)

    if p == 'A':
        if rank(A,B,C) != rank(A+score,B,C):
            ans += 1
        A += score
    elif p == 'B':
        if rank(A,B,C) != rank(A,B+score,C):
            ans += 1
        B += score
    else:
        if rank(A,B,C) != rank(A,B,C+score):
            ans += 1
        C += score

print(ans)