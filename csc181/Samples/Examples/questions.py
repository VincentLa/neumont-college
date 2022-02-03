import random

qa = [
    ('What is your age: ', 38),
    ('What is your income: ', 48000),
    ('How long to you spend (in minutes) on social media a day: ', 116)
]

print("How average are you???")

random.shuffle(qa)

stats = {'average': 0, 'above':0, 'below':0}

try:

    for q, a in qa:
        
        while True:
            r = input(f"\n{q}")
            # if isinstance(r, int) or isinstance(r, float):
            if r.isdigit():
                r = int(r)
                break   
            else:
                print("Please answer with a number. Try again.")
            
        if r == a:
            print("Wow, you are exactly average!")
            stats['average'] += 1
        elif r > a:
            print("You are above average.")
            stats['above'] += 1
        else:
            print("You are below average.")
            stats['below'] += 1

    print()
    print('-' * 50)
    print("Here are your results:")
    print('-' * 50)
    print(f"Average: {stats['average']}")
    print(f"Above average: {stats['above']}")
    print(f"Below average: {stats['below']}")
    print('-' * 50)
    
except:
    print("Sorry something went wrong, please try again")