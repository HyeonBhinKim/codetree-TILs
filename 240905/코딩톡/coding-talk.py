import sys
input = sys.stdin.readline

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n, m, p = map(int, input().split())
alphabet = alphabet[:n]
alphabet = list(map(str, alphabet))

msg = []

for _ in range(m):
    alpha, num = map(str, input().split())
    # num = int(num)
    msg.append((alpha))


for i in range(p-1, m):
    read = msg[i]
    if read in alphabet:
        alphabet.remove(read)

print(*alphabet)