import datetime

class Person(object):

    def __init__(self, name):
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank + 1: ]
        except:
            self.lastName = name
        self.birthday = None

    def getName(self):
        return self.name

    def getLastName(self):
        return self.lastName

    def setBirthday(self, birthdate):
        self.birthdate = birthdate

    def getAge(self):
        if self.birthdate == None:
            raise ValueError
        else:
            return (datetime.date.today() - self.birthdate).days

    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        return self.name

me = Person('Michael Guttag')
print(me.getLastName())
print(me.getName())
me.setBirthday(datetime.date(1983, 10, 4))
print(me.getAge())