class Lab4:
    def __init__(self):
        self.x = 3
        self.y = 2
        self.sum = 5
    def methodA(self, x):
        self.y = self.sum + self.x - x
        self.sum = x - self.y
        d = Lab4()
        d.sum = self.sum + self.methodB(d)
        print(self.x, self.y, self.sum)
        return d
    def methodB(self, t, z = 4):
        y = 2
        t.x = self.x + self.sum
        y = y + t.x - t.y
        self.sum = t.x + t.y + y - z
        if z == 4:
            return y
        print(t.x, t.y, self.sum)
        p = t.methodA(y)
        print(t.x, self.y, p.sum)

obj = Lab4()
obj2 = obj.methodA(4)
obj.methodB(obj2, 10)
