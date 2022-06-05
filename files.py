# Write/Overwrite file
myFile = open('myFile.txt', 'w')

print('Name: ', myFile.name)
print('Is closed: ', myFile.closed)
print('Mode: ', myFile.mode)

myFile.write('Hello there. ')
myFile.close()

# Append
myFile = open('myFile.txt', 'a')
myFile.write('General Kenobi.')
myFile.close()

# Read
myFile = open('myFile.txt', 'r+')
text = myFile.read(100)
print('text: ', text)
