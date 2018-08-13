from eval import *

x = int(input('x = '))

ops = input('Operation(+, -, *, /): ')

y = int(input('y = '))

print('* ' * 10)
print('{} {} {} = {}'.format(x, ops, y, calc(x, y, ops)))
print('* ' * 10, end = '')