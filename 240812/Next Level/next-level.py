class Nextlevel:
    def __init__(self, ID = 'codetree', LEVEL = '10'):
        self.ID = ID
        self.LEVEL = LEVEL

name, Lv = tuple(input().split())

nextl = Nextlevel()
print("user", nextl.ID, "lv", nextl.LEVEL)
nextl = Nextlevel(name, Lv)
print("user", nextl.ID, "lv", nextl.LEVEL)