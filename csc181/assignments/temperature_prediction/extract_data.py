# Will require something like
# /Users/vincentla/.pyenv/versions/3.9.7/bin/python -m pip install pandas
# in terminal.
# Hopefully just pip install works for most users.
import pickle

import pandas as pd

df = pd.read_excel('weather_data.xlsx')
temperatures = df.Temperature.tolist()
temperatures = [int(t[:2]) for t in temperatures]

print(len(temperatures))

temperature = temperatures[0:96]
test_temperature = temperatures[-72:]

with open('temperature.pickle', 'wb') as f:
    pickle.dump(temperature, f)

with open('test_temperature.pickle', 'wb') as f:
    pickle.dump(test_temperature, f)
