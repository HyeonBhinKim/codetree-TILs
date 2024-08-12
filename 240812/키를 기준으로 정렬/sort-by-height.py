n = int(input())
people = []

for _ in range(n):
    person = list(map(str, input().split()))
    people.append(person)

people.sort(key=lambda x:x[1])

for i in people:
    print(' '.join(i))