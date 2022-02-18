# Writes files
file = open('test1.txt', 'w')
file.write("hello\n")
file.write("this is a test\n")
file.close()
# Reads file 
file = open('test1.txt', 'r')
content = file.read()
file.close()
print(content)
# Adds line to file
file = open('test1.txt', 'a')
file.write('add one more line to the file\n')
file.close()
with open('test1.txt', 'w') as file:
    file.write('Wow the with works')