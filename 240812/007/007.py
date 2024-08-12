class Bond:
    def __init__(self, code, point, time):
        self.secret = code
        self.meeting = point
        self.time = time


a, b, c = map(str, input().split())
codetree = Bond(a, b, c)

print('secret code :', codetree.secret)
print('meeting point :', codetree.meeting)
print('time :', codetree.time)