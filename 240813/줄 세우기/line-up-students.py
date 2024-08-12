N = int(input())
people = []

for i in range(1, N+1):
    person = [i]
    person += list(map(int, input().split()))
    people.append(person)

people.sort(key=lambda x:(-x[1],-x[2],x[0]))

for j in people:
    print(j[1],j[2],j[0])