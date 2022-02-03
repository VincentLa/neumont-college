class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.species = 'human'
    
    def says(self):
        print(self.name + ' says, "Hi, how are ya? Nice weather we\'re having"')
    

joe = Person('Joe', 28)
joe.age = 29
print(joe.name, joe.age, joe.species)
joe.says()
print()

class Monster(Person):
    def __init__(self, name, age, species):
        Person.__init__(self, name, age)
        self.species = species
    
    def says(self):
        print(self.name + ' says, "Grrrr!"')

harry = Monster('Harry', 42, 'werewolf')
print(harry.name, harry.age, harry.species)
harry.says()
    