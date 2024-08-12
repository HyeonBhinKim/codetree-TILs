people = []

for _ in range(5):
    name, height, weight = tuple(input().split())
    people.append([name, int(height), float(weight)])

people.sort()
print("name")
for i in people:
    print(i[0],i[1],i[2])
print()
people.sort(key=lambda x:-x[1])
print("height")
for i in people:
    print(i[0],i[1],i[2])