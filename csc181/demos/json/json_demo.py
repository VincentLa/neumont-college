import json

bob = '{"name":"Bob", "age": 21, "species": "zombie"}'

new_bob = json.loads(bob)
print(new_bob)
print()

newer_bob = json.dumps(new_bob)
print(newer_bob)
print()

monsters = [
    {
        "name": "Harry",
        "species": "werewolf"
    },
    {
        "name": "Suzette",
        "species": "vampire"
    },
    {
        "name": "Bob",
        "species": "zombie"
    }
]

file = open('monsters.json', 'w')
file.write(json.dumps(monsters))
file.close()

file = open('monsters.json', 'r')
new_monsters = json.loads(file.read())
file.close

print(new_monsters)
print(new_monsters[1]['name'])