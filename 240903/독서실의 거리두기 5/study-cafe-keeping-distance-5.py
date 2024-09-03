N = int(input())
chairs = input()

maximum = 0
zero = 0
for person in chairs:
    if person == '1':
        zero = 0
        maximum = maximum//2 + 1
    else:
        zero += 1
        maximum = max(zero, maximum)

print(maximum)