# Date and time

import datetime 

todaysDate = datetime.date.today()

print(todaysDate)

print(todaysDate.month)

niceDate = f"{todaysDate.month}/{todaysDate.day}/{todaysDate.year}"

print(niceDate)

print(type(todaysDate))
