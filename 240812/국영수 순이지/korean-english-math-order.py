n = int(input())
people = []

for _ in range(n):
    person = list(map(str, input().split()))
    people.append(person)

people.sort(key=lambda x:(x[1], x[2], x[3]), reverse=True)


for i in people:
    print(' '.join(i))