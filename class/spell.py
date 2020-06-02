class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()

    def getDescription(self):
        return 'No description'

    def execute(self):
        print(self.incantation)

class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning charm')

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'


spell = Spell('Accio', 'Summoning charm')
print(spell)

accio = Accio()
print(accio)
print(type(accio))

confundo = Confundo()
print(confundo)