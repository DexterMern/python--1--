x = int(input('x:'))
y = int(input('y:'))
op = input('op:')
match op:
    case '+':
        print(x + y)
    case '-':
        print(x - y)
    case '*':
        print(x * y)
    case '/':
        print(x / y)
    case _:
        print('Invalid operator!!!')

