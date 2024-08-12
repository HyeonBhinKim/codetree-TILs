class Weather:
    def __init__(self, date, day, sky):
        self.date = date
        self.day = day
        self.sky = sky
        
        
# 변수 선언 및 입력
n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
rainyday = list()
for date, day, sky in arr:
    if sky == 'Rain':
        rainyday.append(Weather(date, day, sky))
         

target_idx = 0
for i, rain in enumerate(rainyday):
    if rain.date < rainyday[target_idx].date:
        target_idx = i

rainday = rainyday[target_idx]

# 결과 출력
print(f'{rainday.date} {rainday.day} {rainday.sky}')