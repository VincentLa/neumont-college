import pickle
with open('temperature.pickle', 'rb') as f:
    temperature = pickle.load(f)

with open('test_temperature.pickle', 'rb') as f:
    test_temperature = pickle.load(f)

print(test_temperature)