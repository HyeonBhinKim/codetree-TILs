class Person:
    def __init__(self, name, address, city):
        self.name = name
        self.address = address
        self.city = city

n = int(input())
people = []

for _ in range(n):
    data = input().split()
    name = data[0]
    address = data[1]
    city = data[2]
    person = Person(name, address, city)
    people.append(person)

# 이름을 기준으로 사전순 정렬
people.sort(key=lambda x: x.name)

# 가장 느린 사람의 정보 출력
slowest_person = people[-1]
print(f"name {slowest_person.name}")
print(f"addr {slowest_person.address}")
print(f"city {slowest_person.city}")