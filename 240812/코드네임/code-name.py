class Agent:
    def __init__(self, name='', score=0):
        self.name = name
        self.score = score

agents = []
for _ in range(5):
    name, score = tuple(input().split())
    score = int(score)
    agents.append(Agent(name, score))

# 최소 점수를 갖는 유저 찾기
min_idx = 0
for i in range(1, 5):
    if agents[min_idx].score > agents[i].score:
        min_idx = i

print(agents[min_idx].name, agents[min_idx].score)