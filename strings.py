name = 'Aaaaaa'
age = 42

# Concatenate
print('1: Hello, my name is ' + name + ' and I am ' + str(age))

# Arguments by position
print('2: Hello, my name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings
print(f'3: Hello, my name is {name} and I am {age}')

# Methods
s = 'hello World'

print('capitalize(): ', s.capitalize())
print('upper(): ', s.upper())
print('lower(): ', s.lower())
print('swapcase(): ', s.swapcase())

print('length: ', len(s))
print('count: ', s.count('o'))

print('replace: ', s.replace('world', 'everyone'), ', ', s)

print('split: ', s.split())
print('find: ', s.find('r'))
