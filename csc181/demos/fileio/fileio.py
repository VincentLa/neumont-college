file = open('test.txt', 'w')
file.write('Hello\n')
file.close()

file = open('test.txt', 'a')
file.write('World')
file.write('World')
file.close()

file = open('test.txt', 'r')
print(file.read())
file.close()

file = open('test.txt', 'r')
print(file.read(10))
file.close()