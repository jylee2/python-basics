class User:
  def __init__(self, name, age): # self is like this
    self.name = name
    self.age = age

  def introduce(self):
    return f'Hi, I am {self.name}'

john = User('John Doe', 42)
print('john: ', type(john), john.name)
print('introduce: ', john.introduce())

class Customer(User):
  def __init__(self, name, age, always_right): # self is like this
    self.name = name
    self.age = age
    self.always_right = True

  def set_always_right(self, always_right):
    self.always_right = always_right

karen = Customer('Karen', 33, True)
print('karen: ', type(karen), karen.always_right)
karen.set_always_right(False)
print('karen.always_right: ', karen.always_right)
