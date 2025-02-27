def div(x, y, n):
    try:
        s = x + y
        result = s / n
    except TypeError as te:
        print(te.__class__.__name__)
    except ZeroDivisionError as zde:
        print(zde.__class__.__name__)
    else:
        print(result)
    finally:
        print('ok')


div(4, 2, 2)


# ..............................
def div(x, y, n):
    try:
        s = x + y
        result = s / n
    except TypeError as te:
        print(te.__class__.__name__)
    except ZeroDivisionError as zde:
        print('**', zde.__class__.__name__)


def funce():
    try:
        a = int(input('a: '))
        b = int(input('b: '))
        c = int(input('c: '))
        div(a, b, c)
    except TypeError as te:
        print(te.__class__.__name__)
    except ValueError as ve:
        print(ve.__class__.__name__)
    except ZeroDivisionError as zde:
        print(zde.__class__.__name__)


# .................................
def div(x, y, n):
    try:
        s = x + y
        d = s / n
        print(d)
    except ZeroDivisionError as zde:
        raise RuntimeError('Oops!') from zde


div(4, 0, 0)
