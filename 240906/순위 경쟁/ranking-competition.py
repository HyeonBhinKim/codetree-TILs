def rank(a, b, c): # a 1, ab 2, b 3, bc 4, c 5, ac 6, abc 7
    return_val = 0
    maxval = max([score1, score2, score3]) 
    
    # 다음과 같이 하면 상태들을 서로 겹치지 않고 정리할 수 있습니다.
    # 1. A가 명예의 전당에 올라가 있는 경우 상태에 1을 더합니다.
    if score1 == maxval:
        return_val += 1

    # 2. B가 명예의 전당에 올라가 있는 경우 상태에 2를 더합니다.
    if score2 == maxval:
        return_val += 2
    
    # 3. C가 명예의 전당에 올라가 있는 경우 상태에 4를 더합니다.
    if score3 == maxval:
        return_val += 4
    
    return return_val

    


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