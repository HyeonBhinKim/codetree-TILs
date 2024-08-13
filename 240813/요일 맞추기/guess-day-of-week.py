m1, d1, m2, d2 = map(int, input().split())

#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', "Sat", "Sun"]

elasps_days = 0

if m1 <= m2:
    for i in range(m1, m2):
        elasps_days += num_of_days[i]
    elasps_days += d2 - d1

else:
    for i in range(m2+1, m1):
        elasps_days += num_of_days[i]
    elasps_days += d1 - d2    

print(days[elasps_days%7])