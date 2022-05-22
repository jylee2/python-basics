# Like objects
person = {
  'first_name': 'John',
  'last_name': 'Doe',
  'age': 42
}
print(person, type(person))
print('first_name: ', person['first_name'])
print('last_name: ', person.get('last_name'))
print('keys: ', person.keys())
print('items: ', person.items())

person2 = person.copy()
person2['city'] = 'KL'
print('person2: ', person2)

del(person2['city'])
print('del: ', person2)

# List of dicts
people = [
  { 'name': 'Asdf', 'age': 20 },
  { 'name': 'Qwert', 'age': 50 }
]
print('people[1][name]: ', people[1]['name'])

