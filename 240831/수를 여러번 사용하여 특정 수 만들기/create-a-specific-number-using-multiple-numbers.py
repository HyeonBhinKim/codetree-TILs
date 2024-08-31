# 입력 받기
A, B, C = map(int, input().split())

# 가능한 최대 값을 저장할 변수
max_value = 0

# A와 B의 조합으로 만들 수 있는 값을 모두 찾기
for i in range(C // A + 1):  # A를 0번부터 C // A 번까지 더함
    for j in range((C - i * A) // B + 1):  # 남은 값에서 B를 0번부터 더함
        current_value = i * A + j * B
        if current_value <= C:
            max_value = max(max_value, current_value)

# 결과 출력
print(max_value)