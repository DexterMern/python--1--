from random import randint

x = randint(1, 6)
y = randint(1, 6)
match (x, y):
    case (6, 6):
        print('won')
    case (1, 1) if 1 <= x <= 6 and 1 <= y <= 6:
        print('lose')
    case (6, y) if 1 <= x <= 6 and 1 <= y <= 6:
        print('repeat')
    case (x, 6) if 1 <= x <= 6 and 1 <= y <= 6:
        print('repeat')
    case (x, y) if 1 <= x <= 6 and 1 <= y <= 6:
        print('next')
    case _:
        print('Error!!')
# or-------------------
match {'x': x, 'y': y}:
    case {'x': 6, 'y': 6}:
        print('win')
    case {'x': 1, 'y': 1}:
        print('lose')
    case {'x': x, 'y': y}:
        print('next')
# you can write this
z = '6'
f = 6
match (z, f):
    case (int(), str()):
        print('YES')
    case _:
        print('No')
