# Python has functions for creating, reading, updating, and deleting files.

# Open a file

myFile = open('myfile.txt', 'w')  # w - write mode

# Get some info

print('name: ', myFile.name)
print('is opened: ', myFile.closed)
print('opening mode: ', myFile.mode)

# Write to file

myFile.write('Jeg elsker Python')
myFile.write(' og JavaScript,')
myFile.close()

# Append to a file

myFile = open('myfile.txt', 'a')  # a - append mode
myFile.write(' Jeg liker React ogsa')

# Read from file

myFile = open('myfile.txt', 'r+')  # r+ - read mode
text = myFile.read(100)
print(text)
