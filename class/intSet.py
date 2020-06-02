'''
class intSet(object):

    def __init__(self):
        self.vals = []

    def insert(self, e):
        if  not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        return e in self.vals

    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + 'not found.')

    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}'

'''

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        i_s = []
        s = ''
        if len(self.vals) >= len(other.vals):
            for el in other.vals:
                if el in self.vals:
                    i_s.append(el)
            print(i_s)
            if len(i_s) == 0:
                return '{}'
            else:
                i_s.sort()
                return '{' + ','.join([str(el) for el in i_s]) + '}'
        else:
            for el in self.vals:
                if el in other.vals:
                    i_s.append(el)
            print(i_s)
            if len(i_s) == 0:
                return '{}'
            else:
                i_s.sort()
                return '{' + ','.join([str(el) for el in i_s]) + '}'

    def __len__(self):
        elements = 0
        for el in self.vals:
            elements += 1
        return elements


set1 = intSet()
set1.insert(-20)
set1.insert(-16)
set1.insert(-15)
set1.insert(-12)
set1.insert(-10)
set1.insert(7)
set1.insert(11)
set1.insert(14)
set1.insert(18)
print(set1)
print(__len__(set1))


set2 = intSet()
set2.insert(-20)
set2.insert(-17)
set2.insert(-16)
set2.insert(-9)
set2.insert(-5)
set2.insert(-4)
set2.insert(-2)
set2.insert(4)
set2.insert(15)
set2.insert(19)
print(set2)

print(set1.intersect(set2))