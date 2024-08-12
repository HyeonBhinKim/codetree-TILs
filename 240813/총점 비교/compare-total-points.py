n = int(input())

people = []

for _ in range(n):
    person = list(map(str, input().split()))
    person[1],person[2],person[3] = int(person[1]),int(person[2]),int(person[3])
    people.append(person)

people.sort(key=lambda x:x[1]+x[2]+x[3])

for i in people:
    print(i[0],i[1],i[2],i[3])