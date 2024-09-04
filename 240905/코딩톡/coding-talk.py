import sys
input = sys.stdin.readline

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n, m, p = map(int, input().split())
alphabet = alphabet[:n]
alphabet = list(map(str, alphabet))

msg = []

for _ in range(m):
    alpha, num = map(str, input().split())
    num = int(num)
    msg.append((alpha, num))

if msg[p-1][1]:
    for i in range(p-1, m):
        read = msg[i][0]
        if i != 0 and msg[i-1][1] == msg[i][1]:
            if msg[i-1][0] in alphabet:
                alphabet.remove(msg[i-1][0])

        if read in alphabet:
            alphabet.remove(read)
            
    print(*alphabet)
else:
    print()