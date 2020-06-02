class Weird(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return x

    def getY(self):
        return y

class Wild(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y
"""
point1 = Weird(6, 7)

print(point1.x)

point1 = Wild(3, 4)
print(point1.getX())
"""
X = 7
Y = 8

w1 = Weird(X,  Y)
print(w1.x)

