import json

userJSON = '{"first_name": "John", "last_name": "Doe", "age": 42}'

# parse to dict/object
user_dict = json.loads(userJSON)
print('user: ', user_dict)
print('first_name: ', user_dict['first_name'])

car = {
  'make': 'Toyota',
  'model': 'Camry',
  'year': 2020
}
carJSON = json.dumps(car)
print('carJSON: ', carJSON)