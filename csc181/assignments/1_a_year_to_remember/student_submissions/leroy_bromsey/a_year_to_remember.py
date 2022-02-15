import random
points = []
Year = [
    ("What year did the Revoultionary war start?", 1775),
    ("When was the United States Constitution signed?", 1783),
    ("When was President Lincoln assassinated?", 1865),
    ("What year was Theodore Roosevelt's first day in office as president?", 1901),
    ("When was the beginning of World War II?", 1939),
    ("In what year was the first personal computer introduced?", 1975),
    ("In what year was the Berlin Wall taken down?", 1989),
    ("When was the first submarine used?", 1776),
    ("Which year did Texas become a state? ", 1845),
    ("Which year the U.S. Stock Market faced the Black Monday? ", 1987)
]
random.shuffle(Year)
print("Guess the year these events occurred")
try:
    for q, a in Year:
        while True:
            r = input(f"\n{q}: ")
            if r.isdigit():
                r = int(r)
                break
            else:
                print("Wrong input, plese use numbers")
        difference = abs(r - a)
        if r == a:
            print("Correct!")
            points.append(10)
            print("You got 10 points")
        elif difference <= 5:
            print("You're really close!")
            points.append(5)
            print("You got 5 points!")
        elif difference <= 10:
            print("a little off by 10 years")
            points.append(2)
            print("you got 2 points")
        elif difference <= 20:
            print("Off by a lot")
            points.append(1)
            print("You got 1 point!")
        else:
            print("Yikes! out of the park with that answer")
            points.append(0)
            print("No points earned")
    final = sum(points)
    print("Your final score:",final)
except:
    print("May have enter words not a year, try again.")
