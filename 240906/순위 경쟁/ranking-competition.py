n = int(input())
    
# 학생 점수 초기화
scores = {'A': 0, 'B': 0, 'C': 0}

# 초기 명예의 전당 상태
hall_of_fame = set(['A', 'B', 'C'])  # 처음에는 모두 명예의 전당에 올라감
change_count = 0

for _ in range(n):
    c, s = input().split()
    s = int(s)
    
    # 점수 업데이트
    scores[c] += s
    
    # 현재 최고 점수 찾기
    max_score = max(scores.values())
    
    # 현재 명예의 전당 업데이트
    current_hall_of_fame = {name for name, score in scores.items() if score == max_score}
    
    # 조합 변화 체크
    if current_hall_of_fame != hall_of_fame:
        change_count += 1
        hall_of_fame = current_hall_of_fame  # 명예의 전당 업데이트

print(change_count)