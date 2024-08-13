m1, d1, m2, d2 = map(int, input().split())
purpose = input()

def num_of_days(m, d):
    # 계산 편의를 위해 월마다 몇 일이 있는지를 적어줍니다. 
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0
    
    # 1월부터 (m - 1)월 까지는 전부 꽉 채워져 있습니다.
    for i in range(1, m):
        total_days += days[i]
    
    # m월의 경우에는 정확이 d일만 있습니다.
    total_days += d
    
    return total_days   


days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', "Sat", "Sun"]

diff = num_of_days(m2,d2) - num_of_days(m1, d1)

ans = diff//7

if diff%7==6:
    ans += 1
elif diff%7==5 and purpose in days[:6]:
    ans += 1
elif diff%7==4 and purpose in days[:5]:
    ans += 1
elif diff%7==3 and purpose in days[:4]:
    ans += 1
elif diff%7==2 and purpose in days[:3]:
    ans += 1
elif diff%7==1 and purpose in days[:2]:
    ans += 1
elif diff%7==0 and purpose in days[:1]:
    ans += 1

print(ans)