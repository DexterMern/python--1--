try:
    x = int(input('x: '))
    y = int(input('y: '))
    z = x / y

except (ZeroDivisionError, ValueError) as E:
    print(E.__class__.__name__)
except TypeError as t:
    print(t.__class__)
except:
    print('Err!')
print('hello')
# ........................
try:
    x = int(input('x: '))
    y = int(input('y: '))
    z = x / y
except Exception as Ex:
    print(Ex.__class__.__name__)
print('hello')
