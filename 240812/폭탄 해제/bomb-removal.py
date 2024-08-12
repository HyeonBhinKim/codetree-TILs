class Bomb:
    def __init__(self, code, color, time):
        self.code = code
        self.color = color
        self.time = time
    

code, color, time = tuple(input().split())

defuse = Bomb(code, color, time)

print('code :', defuse.code)
print('color :',defuse.color)
print('second :', defuse.time)