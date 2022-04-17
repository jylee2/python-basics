numbers = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'grapes', 'pears']
numbersConstructor = list((1, 2, 3, 4, 5))

print(numbers, numbersConstructor)

# copy
new_fruits = fruits.copy()

print('fruits: ', fruits)
print('array element: ', fruits[1])
print('length: ', len(fruits))

fruits.append('mangos')
print('append: ', fruits)

fruits.remove('grapes')
print('remove: ', fruits)

fruits.insert(3, 'strawberries')
print('insert: ', fruits)

fruits.pop(3)
print('pop: ', fruits)

fruits.reverse()
print('reverse: ', fruits.reverse(), fruits)

fruits.sort()
print('sort: ', fruits.sort(), fruits)

fruits.sort(reverse=True)
print('reverse sort: ', fruits.sort(reverse=True), fruits)

# Dangerously mutate value
fruits[0] = 'AAAAAAAAAAA'
print('mutate: ', fruits)

print('new_fruits: ', new_fruits)