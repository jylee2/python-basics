# Tuples are ordered, unchangeable and allows duplicate members
fruits = ('Apples', 'Oranges', 'Grapes')
print('fruits: ', fruits)

fruits2 = ('Apples')
print('fruits2: ', fruits2, type(fruits2))

fruits3 = ('Apples',)
print('fruits3: ', fruits3, type(fruits3))

# Should bomb TypeError: 'tuple' object does not support item assignment
# fruits[1] = 'AAAAA'
try:
  fruits[1] = 'AAAAA'
except:
  print('An exception occurred')

del fruits2
# print('del fruits2: ', fruits2)

################################################################
# Sets are unordered, unindexed and does not allow duplicate members
fruits_set = {'Apples', 'Oranges', 'Mango'}
apples_in_fruits = 'Apples' in fruits_set
print('apples_in_fruits: ', apples_in_fruits)

fruits_set.add('Grape')
print('fruits_set.add(): ', fruits_set)

fruits_set.remove('Grape')
print('fruits_set.remove(): ', fruits_set)
