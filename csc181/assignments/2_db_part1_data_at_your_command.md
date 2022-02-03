For this lab, you are going to start creating a command line database application. You will be able to use two commands at this point

- py db.py -a [your content to add to the text file]            (append to text file)
- py db.py -l                                                                          (list everything in the text file)

Requirements:

- The database will append whatever comes after '-a' in the command line arguments to a text file called 'data.txt'
- Use the '-l' to list the contents of the text file
- If the user passes in too few or incorrect arguments, print the proper usage for the application on the screen and exit the application so they can try again.
- If the database text file (in this case 'data.txt') doesn't exist yet use a try/except to handle this edge case. In particular, if the file doesn't exist, and "-l" is passed, print a message that says "File does not exist yet". If "-a" is passed, create the file, add the content to the text file, and say "new file created, content added". 
- When adding something to the text file and the text file already exists, print a message that says, "content added."


Submission:

- Submit as a file that contains your python script.

Additional Resources:

- args and options that get passed to a python file: https://www.tutorialspoint.com/python3/python_command_line_arguments.htm


