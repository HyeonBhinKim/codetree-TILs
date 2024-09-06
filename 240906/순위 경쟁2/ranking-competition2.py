n = int(input())

rank = 0 # 시작시 0, A 1, AB 2, B 3 

change = False

A = 0
B = 0

ans = 0
for _ in range(n):
    p, score = input().split()
    score = int(score)

    if p == "A":
        A += score
    else:
        B += score
    
    if A > B and rank != 1:
        change = True
        ans += 1
        rank = 1
    elif A == B and rank != 2 and change:
        ans += 1
        rank = 2
    elif A < B and rank != 3:
        change = True
        ans += 1
        rank = 3
    
print(ans)