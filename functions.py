# Define function
def sayHello(name = 'Default Name'):
    print(f'Hello {name}')


sayHello('Asdf')


def getSum(num1, num2):
    total = num1 + num2
    return total


print('getSum', getSum(1, 2))


getSum2 = lambda num1, num2 : num1 + num2
print('getSum2', getSum2(10, 20))
