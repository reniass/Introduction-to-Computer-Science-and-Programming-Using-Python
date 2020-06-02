class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """

    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object
            occurs 0 times in self. """
        self.vals = {}

    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1

    def __str__(self):
        s = ''
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i) + ":" + str(self.vals[i]) + "\n"
        return s

class Bag(Container):

    def remove(self, e):
        """ assumes e is hashable
            If e occurs one or more times in self, reduces the number of
            times it occurs in self by 1. Otherwise does nothing. """
        self.vals[e] -= 1

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        try:
            return self.vals[e]
        except:
            return 0

    def __add__(self, other):
        s = ''
        d = {}
        for i in self.vals.keys():
            d[i] = self.vals[i]
        for j in other.vals.keys():
            if j in d.keys():
                d[j] += other.vals[j]
            else:
                d[j] = other.vals[j]
        for k in d.keys():
            s += str(k)+':'+str(d[k])+'\n'

        return s

class ASet(Container):

    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        del self.vals[e]

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        if e in self.vals.keys():
            return True
        else:
            return False









a = Bag()
a.insert(4)
a.insert(4)
a.insert(6)
a.insert(9)

b = Bag()
b.insert(6)
b.insert(9)

print(a+b)