people = ['John', 'Aaron', 'Elizabeth', 'Sarah', 'Blake']

for person in people:
  print(f'Current person: {person}')

print('-----------')
for person in people:
  if person == 'Aaron':
    continue
  elif person == 'Sarah':
    break
  print(f'Current person: {person}')

print('-----------')
for i in range(0, len(people)):
  print(f'{i}: {people[i]}')