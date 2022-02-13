For this assignment, you are going to build a quiz application that asks for the year various events happened. Here are the events you must have in your quiz:

the start of the Revolutionary War - 1775
the United States Constitution signed - 1783
President Lincoln assassinated - 1865
Theodore Roosevelt's first day in office as President of the United States - 1901
the beginning of World War II - 1939
the first personal computer introduced - 1975
the Berlin Wall taken down - 1989
 
Requirements:

- Add three more events to the list above so there are exactly ten events
- Build the event information provided above as a list (array) of tuples where each tuple contains the event and the year.
- Build the questions dynamically rather than writing them out as part of the event. In other words, concatenate a statement like "In what year was " with the event and add a question mark at the end. Be sure the questions and the events are written so they make sense.
- Use `shuffle` from the `random` library to ensure the questions appear in a different order each time you run the program.
- Use input to allow the user to guess a year, be sure to convert their input to an integer before trying to compare it to the year
- If the year entered is exactly correct, add 10 points to the score. If it is within 5 years in either direction, add 5 points. If it is within 10 years in either direction, add 2 points. If it is within 20 years in either direction, add 1 point. Do not give any points if they are further than 20 years off. I would recommend using `if` and `elif` statements for this.
- Give a different response depending on how close to the correct answer the user's guess was, tell them the correct answer, and their new score.
- Ask each question until you have gone through all of them.
- Give a final score at the end and print out a comment on how they did overall based on their score.
- Add a try/except that will cleanly quit you out of the program without throwing an error if the user enters a value that cannot become an integer (for instance if they just hit <Enter> without putting in a date).
 

Additional Information:

- If you need to search online to better understand some of the aspects of Python required in the assignment, be sure to preface your search with "Python 3" since the syntax is occasionally different from previous versions of Python.
 

Submission:

Submit only the single python script, no other files should be needed or included.