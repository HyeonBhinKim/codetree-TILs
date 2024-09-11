N = int(input())

arr = []

for _ in range(N):
    command = list(input().split())
    if len(command) > 1:
        command[1] = int(command[1])
    if command[0] == "push_back":
        arr.append(command[1])
    elif command[0] == "pop_back":
        arr.pop()
    elif command[0] == "get":
        print(arr[command[1]-1])
    else:
        print(len(arr))