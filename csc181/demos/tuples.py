sally = ("Sally", 24, "Immortal")
print(sally)

jim = "Jim", 24, "Immortal"
print(jim)

george = ("George",)
print(george)

sally += jim
print(sally)

print(sally.count(24))
print(sally.index('Jim'))

(name, age, species) = ("Harry", 42, 'werewolf')
print(name, age, species)
age += 1
print(age)

molly = ("Molly", 37, "ghost")
name, age, species = molly
print(name, age, species)

(name, species) = (species, name)
print(name, species)