class fraction(object):

    def __init__(self, numerator, denominator):
        self.numerator  = numerator
        self.denominator = denominator

    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)

    def getNumer(self):
        return self.numerator

    def getDenom(self):
        return self.denominator

    def __add__(self, other):
        newNumer = self.numerator * other.denominator + other.numerator * self.denominator
        newDenom = self.denominator * other.denominator
        return fraction(newNumer, newDenom)

    def __sub__(self, other):
        newNumer = self.numerator * other.denominator
        newDenom = self.denominator * other.numerator
        return fraction(newNumer, newDenom)


oneHalf = fraction(1, 2)
print(oneHalf)